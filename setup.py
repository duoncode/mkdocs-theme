from setuptools import setup, find_packages

VERSION = '0.1.0'

setup(
    name="mkdocs_conia",
    version=VERSION,
    url='https://github.com/coniadev/mkdocs-conia',
    license='MIT',
    description='Default mkdocs theme for Conia projects',
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
