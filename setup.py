from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="src",
    version="0.0.1",
    author="Gopichandyarra",
    author_email="Gopichandyarra.1@gmail.com",
    description="A small package for ANN implementation",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Gopichandyarra/ANN-Implementation",
    packages=['src'],
    python_requirements=">=3.7",
    install_requires=[
        'tensorflow',
        'matplotlib',
        'seaborn',
        'numpy', 
        'pandas',
        'PyYAML'
    ]
) 