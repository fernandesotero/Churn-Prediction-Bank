'''
Script to build the project as a package
'''

from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT = '-e .'

def get_requirements(file_path: str) -> List[str]:
    '''
    Function to return the list of packages in requirements.txt.

    Parameters
    ----------
    @param file_path: Path of requirements.txt file [type: string].

    Return
    ------
    @return requirements: List of strings containing the packages for the project.  
    '''
    requirements = []
    with open(file_path) as file:
        requirements = file.readlines()
        requirements = [req.strip() for req in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
    
    return requirements


# Defining the setup
setup(
    name='bank-churn-prediction',
    version='0.0.1',
    author='Daniel Fernandes',
    author_email='fernandesotero@proton.me',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=get_requirements('requirements.txt')
)