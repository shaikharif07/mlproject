# to use ml application as a package & deploy on PyPI
from setuptools import find_packages,setup
from typing import List

#in requirement.txt it is an indication to run setup file
auto_trig = '-e .'

#function will return a list of req
def get_requirements(file_path:str)->List[str]:
    requirements = []
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n", " ") for req in requirements]    

        if auto_trig in requirements:
            requirements.remove(auto_trig)
    
    return requirements


setup(
#metadata of project
name = 'mlproject',
version='0.0.1',
author='Arif',
author_email='arif8108shaikh@gmail.com',
packages= find_packages(),
install_requires = get_requirements('requirements.txt')
#since few can be installed manually
# install_requires = ['pandas','numpy','seaborn']
#when many present use function
)

#src folder with __init__.py file makes sure it can be built as a package 
