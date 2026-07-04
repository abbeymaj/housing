# Importing packages
from typing import List
from setuptools import setup, find_packages

# Setting up a global variable for the editable install option
HYPHEN_E_DOT = "-e ."

# Creating a function to read the requirements from a file
def get_requirements(file_path: str) -> List[str]:
    '''
    This function will return the list of packages that are specified in the 
    requirements file.
    ==========================================================================
    ---------------
    Parameters:
    ---------------
    file_path : str : This is the path to the requirements.txt file.
    
    ---------------
    Returns:
    ---------------
    List - List[str] - This is the list of packages that need to be installed
    for the project, which is specified in the requirements.txt file.
    ==========================================================================
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]
    
    # Checking if the HYPHEN_E_DOT is present in the requirements list and 
    # removing it if found
    if HYPHEN_E_DOT in requirements:
        requirements.remove(HYPHEN_E_DOT)
    
    return requirements

# Creating the setup to install packages listed in requirements.txt
setup(
    name='housing',
    author='Abbey Majumdar',
    version='0.0.1',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)
