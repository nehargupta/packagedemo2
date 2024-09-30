from setuptools import setup, find_packages

setup(
    name="package_publishing2",
    version="0.1",
    packages=find_packages(),
    install_requires=[
          'scikit-learn>=1.6.0',
          'scipy>=0.14',
          'pandas>=0.11.0',
          'numpy>=1.6.1'
    ],
    author="Neha",
    author_email="nehargupta@cmu.edu",
    description="A simple example private package",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/nehargupta/packagedemo2",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)