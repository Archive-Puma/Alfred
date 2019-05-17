from setuptools import setup, find_packages

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name="alfred",
    version="0.0.1.dev0",
    author="Kike Fontan (@CosasDePuma)",
    author_email="kikefontanlorenzo@gmail.com",
    description="Just another programming language",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/CosasDePuma/Alfred",
    packages=find_packages(),
    entry_points={"console_scripts": "alfred=src.alfred:main"},
    license="MIT",
    install_requires=[
        "ply>=3.11"
    ],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Programming Language :: Python :: 3.6",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        'Intended Audience :: Education',
        'Intended Audience :: Science/Research',
        "Topic :: Text Processing :: General",
        'Topic :: Education',
        'Topic :: Software Development',
        'Topic :: Software Development :: Libraries',
        "Topic :: Software Development :: Libraries :: Python Modules"
    ],
)
