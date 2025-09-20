from setuptools import setup, find_packages
import logging

hyper_e_dot = 'e .'
def get_requirements(path):
    
    with open(path, 'r') as f:
        requirements = f.readlines()
        requirements = [req.replace('\n',' ') for req in requirements]
        
        if hyper_e_dot in requirements:
            requirements.remove(hyper_e_dot)
            
            
setup(
    fullname="Computer vision project",
    version="0.1",
    author="Aziz Ashfak",
    author_email="azizashfak@gamil.com",
    description="This ia a computer vision project. We will be using OpenCV and other libraries to perform image processing and object detection.",
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
)