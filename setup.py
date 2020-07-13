from setuptools import setup, find_packages

with open("requirements.txt") as f:
    reqs = f.read().splitlines()

description = "Bootstrap statistics package."
long_description = ""
setup(
    name="ezbootstrap",
    description=description,
    long_description=long_description,
    version="0.0.1",
    url="https://github.com/Ruairi-osul/ezbootstrap",
    author="Ruairi O'Sullivan",
    author_email="ruairi.osullivan.work@gmail.com",
    license="GNU GPLv3",
    keywords="statistics scientific-computing data data-science",
    project_urls={"Source": "https://github.com/Ruairi-osul/ezbootstrap"},
    packages=find_packages(),
    python_requires=">=3.3",
    install_requires=reqs,
)
