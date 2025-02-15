from setuptools import setup, find_packages
from typing import List

def get_requirements(file_path: str) -> List[str]:
    requirments=[]
    with open(file_path, 'r') as file:
        requirments = file.readlines()
        requirments=[requirment.replace('\n','') for requirment in requirments]
    return requirments

    

setup(
    name="my_project",  # Name of the package
    version="0.1.0",  # Version number
    author="abubakar",
    author_email="your.email@example.com",
    description="A brief description of the project",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/my_project",  # Project URL (GitHub, GitLab, etc.)
    packages=find_packages(),  # Automatically find all packages in the project directory
    install_requires=get_requirements('requirment.txt'),  # List of dependencies
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
