# Localization Management Code for GitHub Actions

This GitHub Action is designed to simplify the localization process for Laravel, Vue, and Flutter applications. It automates the generation of translation files in multiple languages, and supports variables in translations for easy customization.

## Features

- Generates translation files for Laravel, Vue, and Flutter
- Supports multiple languages
- Allows for customization through the use of variables in translations
- Automatic release of translation files as artifacts

## Getting Started

To use this GitHub Action, you will need to add the following code to your workflow:

```
CODE HERE
```

### Input Parameters

- `path`: The path to the directory containing your translation files. This should be relative to your repository's root directory.
- `laravel`: Set this to `true` if you want to generate Laravel translation files.
- `vue`: Set this to `true` if you want to generate Vue translation files.
- `flutter`: Set this to `true` if you want to generate Flutter translation files.

### Output

This GitHub Action automatically creates artifacts containing your generated translation files. These artifacts can be downloaded and used for localization purposes.

## Examples

Here's an example workflow that generates translation files for Laravel, Vue, and Flutter:

```
CODE HERE
```

## Contributions

Contributions to this GitHub Action are welcome. Please open a pull request with any improvements or bug fixes.

## License

This project is licensed under the [MIT License](LICENSE).
