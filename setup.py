from setuptools import setup, find_packages

VERSION = '0.1.4'

with open('README.md', 'rt', encoding='utf8') as f:
    README = f.read()

setup(
    name="mkdocs-conia",
    version=VERSION,
    url='https://github.com/coniadev/mkdocs-conia',
    license='MIT',
    description='Default mkdocs theme for Conia projects',
    long_description=README,
    long_description_content_type='text/markdown',
    author='ebene fünf GmbH',
    author_email='conia@ebenefuenf.de',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'mkdocs>=1.3',
        'mkdocs-macros-plugin>=0.7',
    ],
    entry_points={
        'mkdocs.themes': [
            'conia = theme',
        ]
    },
    zip_safe=False
)
