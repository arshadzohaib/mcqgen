from setuptools import find_packages, setup

setup(
    name="mcqgenerator",
    version="0.0.1",
    author="Arshad Zohaib",
    author_email="arshadzohaib315@gmail.com",
    install_requires=[
        "langchain",
        "langchain-community",
        "streamlit",
        "python-dotenv",
        "PyPDF2",
        "ollama"
    ],
    packages=find_packages()
)