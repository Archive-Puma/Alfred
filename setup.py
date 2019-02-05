import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()


requirements = []
with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setuptools.setup(
    name="alfred",
    version="0.6.0",
    author="Kike Fontan (@CosasDePuma)",
    author_email="alfred@kike.online",
    description="Just another programming language",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/cosasdepuma/alfred",
    packages=setuptools.find_packages(),
    packages_data={'src': ['parser.out','parsetab.py']},
    include_package_data=True,
    entry_points={"console_scripts": "alfred = src:main"},
    license="MIT",
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)