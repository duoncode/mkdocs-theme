MkDocs Conia Theme
==================

This is a theme for MkDocs which is mainly used in [Conia](https://conia.dev) projects 

## Installation

Install the package from PyPi using `pip`:

    pip install mkdocs-conia

Add the theme to your `mkdocs.yml` file:

    theme:
        name: conia

## Styles

Install Dart Sass via `npm install -g sass`. During develompment:

    sass --watch styles:theme

## Deploy to PyPi

Install `twine` if not already done. Bump version number, then:

    sass --style compressed styles:theme
    python setup.py bdist_wheel
    twine upload dist/*
