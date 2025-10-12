'''essential part for packaging and distributing python prijects  it define the configuration of project like meta data dependencies and more'''



from setuptools import find_packages , setup
# find_package search all folder and find __inut__.py and when it find this the parent folder will become package and setu[ os for al details]
from typing import List

def get_requirements()->List[str]:
    #Thsi function returns list of requirements
    requirement_list: list[str] = []
    try:
        with open('requirements.txt' , 'r') as file:
            #Read lines from file
            lines = file.readlines()
            #Process each line
            for line in lines:
                requirement = line.strip()
                ##ignore empty lines and -e.
                if requirement and requirement!= '-e .':
                    requirement_list.append(requirement)
    except FileNotFoundError:
        print("file not found") 
    return requirement_list
print(get_requirements())                   


setup(

    name = "NetworkSecurity",
    version="0.0.1",
    author="Ankush",
    author_email="sehrawatankush0@gmail.com",
    packages= find_packages(),
    install_requires= get_requirements()

)