from setuptools import find_packages,setup
from typing import List
requirement_list:List[str]=[]
def get_requirements()->List[str]:
    """ 
    This function will return list of requriments
    
    """

    try:
        with open("requirements.txt",'r') as file:
            #load lines from the file
            lines=file.readlines()
            # Process each line
            for line in lines:
                requirement=line.strip( )
                #ignore empty lines and -e .
                if requirement and requirement!='-e .':
                    requirement_list.append(requirement)

    except FileNotFoundError:
        print("Requirements.txt file not found")

    return requirement_list

setup(
    name='Network_Security_System',
    version="0.0.1",
    author="Nithin kuamr",
    author_email="saragadamnithinkumar@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements()

)