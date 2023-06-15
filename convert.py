import pandas as pd
from io import StringIO
import json,re,os
import argparse

def ArgParser():
    ap = argparse.ArgumentParser()
    ap.add_argument("-input", "--excell", default=None, help="path to excell file directory")
    ap.add_argument("-flutter", "--flutter", default=None, help="generate flutter arb file?")
    ap.add_argument("-laravel", "--laravel", default=None, help="generate laravel json format file?")
    ap.add_argument("-vue", "--vue", default=None, help="generate vue json format file?")
    args = vars(ap.parse_args())
    return args

def convertDictToJson(dict,outputFile):
    with open(outputFile, "w",encoding='utf-8') as file:
        json_formatted_str = json.dumps(dict, ensure_ascii=False,indent=2)
        json_formatted_str = json_formatted_str.replace('\\"', '"')  # Unescape double quotes
        json_formatted_str = json_formatted_str.replace('\\\\n', '\\n')  # Unescape escaped newlines
        file.write(json_formatted_str)
        file.close()

def convertVariableForPhp(string):
    pattern = re.compile(r'\{([^}]+)\}')
    return pattern.sub(r':\1', string)

def convertVariableForMobile(string):
    pattern = re.compile(r'\{([^}]+)\}')
    return pattern.sub(r'%s', string)  

def convert(args):
    excell_path = args["excell"]
    generate_flutter = args["flutter"]
    generate_vue = args["vue"]
    generate_laravel = args["laravel"]
    base_dicts={}

    if(excell_path != None):
        #convert xlsx to csv file
        df = pd.read_excel(excell_path)
        csv_string = df.to_csv(encoding='utf-8')
        df = pd.read_csv(StringIO(csv_string), index_col=0)

        #convert csv to json
        json_str = df.to_json(orient='records', force_ascii=False)
        data=json.loads(json_str)
        flutter_dicts={}
        for item in data[0]:
            if(item == 'key'):
                continue
            for value in data:
                base_dicts[value['key']]=value[item]
            if(generate_vue.lower() == 'true'):
                convertDictToJson(base_dicts,f'vue_{item}.json')
            if(generate_flutter.lower() == 'true'):     
                for key,value in base_dicts.items():
                    flutter_dicts[key]=convertVariableForMobile(value)
                convertDictToJson(flutter_dicts,f'flutter_{item}.arb')      
            if(generate_laravel.lower() == 'true'):         
                for key,value in base_dicts.items():
                    base_dicts[key]=convertVariableForPhp(value)      
                convertDictToJson(base_dicts,f'laravel_{item}.json')      
                
    
  

if __name__ == '__main__':
    args=ArgParser()
    convert(args)
    
