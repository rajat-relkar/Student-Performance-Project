from setuptools import find_packages, setup
from typing import List

'''
Note: -e . in requirements.txt will automatically trigger setup.py
But it should not be read by get_requirements()
'''

HYPEN_E_DOT = '-e .'
def get_requirements(filepath:str)->List[str]:
    '''
    This function returns the list of required python libraries
    '''
    requirements=[]
    with open(filepath) as fileObj:
        requirements = fileObj.readlines()
        requirements = [req.replace("\n", " ") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

setup(
    name='Student Performance Project',
    version='0.0.1',
    author='Rajat Relkar',
    author_email='relkarrajat@gmail.com',
    packages=find_packages(),
    install_requires = get_requirements('requirements.txt')
)