from setuptools import setup, find_packages

VERSION = '0.1.0-dev'

setup(
    name="mkdocs-conia",
    version=VERSION,
    url='https://github.com/coniadev/mkdocs-conia',
    license='MIT',
    description='Default theme for GitBook for Mkdocs',
    author='ebene fünf GmbH',
    author_email='conia@ebenefuenf.de',
    packages=find_packages(),
    include_package_data=True,
    entry_points={
        'mkdocs.themes': [
            'conia = theme',
        ]
    },
    zip_safe=False
)
