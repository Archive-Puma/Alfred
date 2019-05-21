from setuptools import setup, find_packages

try:
    with open("README.md", "r") as r, open("VERSION", "r") as v:
        long_description = r.read()
        version = v.readline().strip()
except FileNotFoundError:
    long_description = ''
    version = '0.0.1.dev5'

setup(
    name="alfred-lang",
    version=version,
    author="Kike Fontan (@CosasDePuma)",
    author_email="kikefontanlorenzo@gmail.com",
    description="Just another programming language",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/CosasDePuma/Alfred",
    packages=find_packages(),
    entry_points={"console_scripts": "alfred=src.alfred:main"},
    data_files=[('', ['VERSION','README.md'])],
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
