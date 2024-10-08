from setuptools import setup, find_packages
from typing import List


hyphen_e_dot = '-e .'

def get_requirements(file_path:str)->List[str]:
    """
    This function will return the list of requirements
    """
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements]

        if hyphen_e_dot in requirements:
            requirements.remove(hyphen_e_dot)



setup(
    name='mlproject',
    version='0.1',
    author='Md Ayan Arshad',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)

"""
1. This script helps package your project, automatically detecting the Python packages and reading dependencies from requirements.txt.
2. It removes '-e .' if present in the requirements, which allows for the editable installation of your own project.
3. When someone runs pip install . or python setup.py install, this file will help install the project and its dependencies.
"""