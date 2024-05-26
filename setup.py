# setup.py

from setuptools import setup, find_packages
import text_summarizar

setup(
    name="text_summarizer",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "nltk",
        "scikit-learn",
    ],
    author="Your Name",
    author_email="your.email@example.com",
    description="A package for summarizing text and extracting key phrases",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/text_summarizer",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
