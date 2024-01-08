from setuptools import setup, find_packages
import os


def get_requirements(file_path):
    requirements = []
    with open(file_path) as file:
        requirements = file.readlines()
        requirements = [req.replace("\n", "") for req in requirements]
        if "-e ." in requirements:
            requirements.remove("-e .")
    return requirements


PROJECT_NAME = <YOUR_PROJECT_NAME>
VERSION = "0.0.0"
DESCRIPTION = <ENTER_DESCRIPTION_HERE>
AUTHOR = "NarenBot"
AUTHOR_EMAIL = "narendas10@gmail.com"

setup(
    name=PROJECT_NAME,
    version=VERSION,
    description=DESCRIPTION,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    package_dir={"": "src"}, # "src"
    packages=find_packages(where="src"), # "where='src'"
    install_requires=get_requirements("requirements.txt"),
)
