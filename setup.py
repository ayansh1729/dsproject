from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT = '-e .'

def get_requirements(path: str) -> List[str]:
    """
    This function will return a list of requirements
    """
    requirements = []
    with open(path) as file:
        requirements = file.read().split('\n')  

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)

    return requirements

setup(
    name='dsproject',
    version='0.0.1',
    author='Ayansh',
    author_email='ayanshsingh707@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
)
