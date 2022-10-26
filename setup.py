from setuptools import setup, find_packages

VERSION = '0.0.1' 
DESCRIPTION = 'Eversend Python SDK'
LONG_DESCRIPTION = 'Python SDK for Eversend merchant users to integrate in their'

# Setting up
setup(
    name="eversend", 
    version=VERSION,
    author="Eversend",
    author_email="info@eversend.co",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    url="https://github.com/eversend/eversend-python-sdk",
    license="MIT",
    packages=find_packages(exclude=["tests", "tests.*"]),
    python_requires=">=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*",
    install_requires=[
        'requests >= 2.20; python_version >= "3.0"',
        'requests[security] >= 2.20; python_version < "3.0"',
    ],
    keywords=['eversend api payments'],
    classifiers= [
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ]
)