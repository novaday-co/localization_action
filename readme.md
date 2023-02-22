# Localization Management Code for GitHub Actions

This GitHub Action is designed to simplify the localization process for Laravel, Vue, and Flutter applications. It automates the generation of translation files in multiple languages, and supports variables in translations for easy customization.

## Features

- Generates translation files for Laravel, Vue, and Flutter
- Supports multiple languages
- Allows for customization through the use of variables in translations

## Getting Started

To use this GitHub Action, you will need to add the following code to your workflow:

```
- name: Generate Localization Files
        uses: novaday-co/localization_action@1.0.0
        with:
          input_file: yourExcell.xlsx
          generate_flutter: true
          generate_laravel: true
          generate_vue: true
```

### Input Parameters

| Parameter  | Status  | Description  |
| ------------ | ------------ | ------------ |
| input_file  |  required  | The path to the directory containing your translation files. This should be relative to your repository's root directory.  |
| generate_flutter  | optional  |  Set this to `false` if you don't want to generate Flutter translation files. the default value of this parameter is 'true'. |
| generate_laravel  |  optional | Set this to `false` if you don't want to generate Laravel translation files. the default value of this parameter is 'true'.  |
| generate_vue  | optional  | Set this to `false` if you don't want to generate Vue translation files. the default value of this parameter is 'true'.   |


### Output

This GitHub Action automatically creates your generated translation files. These files can be used for localization purposes.
## Examples

Here's an example workflow that generates translation files for Laravel, Vue, and Flutter And releases translation files as artifacts

```
name: "Localization Management Sample"

on:
  push:
    branches: [master]

jobs:
  development:
    name: 🎉 Convert Action
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        uses: actions/checkout@v3
		
      - name: Generate Localization Files
        uses: novaday-co/localization_action@1.0.0
        with:
          input_file: myFile.xlsx
          generate_flutter: true
          generate_laravel: true
          generate_vue: true
		  
      - name: Push To Releases
        uses: ncipollo/release-action@v1
        with:
          artifacts: '*.json,*.arb'
          tag : ${{ github.run_number }}
          token : ${{ secrets.TOKEN }}
```

## Contributions

Contributions to this GitHub Action are welcome. Please open a pull request with any improvements or bug fixes.

## License

This project is licensed under the [MIT License](LICENSE).
