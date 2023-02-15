import pandas as pd
from io import StringIO
import json,re,os
import argparse

def ArgParser():
    ap = argparse.ArgumentParser()
    ap.add_argument("-input", "--excell", default=None, help="path to excell file directory")
    args = vars(ap.parse_args())
    return args

def convertDictToJson(dict,outputFile):
    with open(outputFile, "w",encoding='utf-8') as file:
        json_formatted_str = json.dumps(dict, ensure_ascii=False,indent=2)
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
    fa_dicts={}
    fa_dicts_php={}
    fa_dicts_mobile={}

    if(excell_path != None):
        #convert xlsx to csv file
        df = pd.read_excel(excell_path)
        csv_string = df.to_csv(encoding='utf-8')
        df = pd.read_csv(StringIO(csv_string), index_col=0)

        #convert csv to json
        json_str = df.to_json(orient='records', force_ascii=False)
        data=json.loads(json_str)

        #generate fa dict 
        for item in data:
            fa_dicts[item['key']]=item['fa']

        for key,value in fa_dicts.items():
            fa_dicts_php[key]=convertVariableForPhp(value)

        for key,value in fa_dicts.items():
            fa_dicts_mobile[key]=convertVariableForMobile(value)

        #generate front end persian file    
        convertDictToJson(fa_dicts,'front_fa.json')

        #generate back end persian file    
        convertDictToJson(fa_dicts_php,'back_fa.json')

        #generate back end persian file    
        convertDictToJson(fa_dicts_mobile,'lan_fa.arb')    

if __name__ == '__main__':
    args=ArgParser()
    convert(args)
    