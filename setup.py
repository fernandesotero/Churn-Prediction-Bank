'''
Script to build the project as a package
'''

from setuptools import find_packages, setup
from typing import List, list


HYPHEN_E_DOT = '-e .'
def get_requirementes(file_path: str) -> List[str]:
    '''
        Function to return the list of packages in requirements.txt.

        Parameters
        ----------
        @param file_path: Path of requirements.txt file [type: string].

        Return
        ------
        @return requirements: List of strings containing the packages for the project.  
    ''' 
    requirements = list()
    with open(file_path) as file:
        requirements = file.readline()
        requirements = [req.replace('\n', '') for req in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
    
    return requirements


# Defining the setup.
setup(
    name = 'Bank Chrun Prediction',
    version = '0.0.1',
    author = 'Daniel Fernandes',
    author_email = 'fernandesotero@proton.me',
    packages = find_packages(),
    install_requires = get_requirementes('requirements.txt')
)
