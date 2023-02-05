import os

from setuptools import setup, find_packages

import Sample

try:
    long_description = open('README.rst', 'rt').read()
except IOError:
    long_description = ''

def load_pkg_dependencies():
    pkgDeps = list()
    
    if os.path.exists('requirements.txt'):
        reqsList = None
        with open('requirements.txt') as fp:
            reqsList = fp.readlines()
            
        if reqsList:
            for req in reqsList:
                reqSpec = req.strip()
                if reqSpec:
                    pkgDeps.append(reqSpec)
                    
    return pkgDeps  


pkg_dependencies = load_pkg_dependencies()
pkg_scripts = []
pkg_datalist = ['Conf/*.conf', 'version.txt']


setup(
    name=Sample.__name__,
    version=Sample.__version__,

    description=Sample.__description__,
    long_description=long_description,

    author='Manjit Kumar',
    author_email='manjitp46@gmail.com',


    classifiers=[],

    platforms=['Any'],
    scripts=pkg_scripts,
    provides=[],
    install_requires=pkg_dependencies,
    namespace_packages=[],
    packages=find_packages(),
    include_package_data=True,
    package_data={'Sample' : pkg_datalist},

    zip_safe=False,
)

