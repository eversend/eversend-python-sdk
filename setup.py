from setuptools import setup, find_packages

VERSION = '1.0.0' 
DESCRIPTION = 'Eversend Python SDK'
with open("README.md", "r") as fp:
    LONG_DESCRIPTION = fp.read()

# Setting up
setup(
    name="eversend", 
    version=VERSION,
    author="Eversend",
    author_email="info@eversend.co",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    url="https://github.com/eversend/eversend-python-sdk",
    license="MIT",
    packages=find_packages(exclude=["tests", "tests.*"]),
    python_requires=">=3.5",
    install_requires=[
        'requests >= 2.20; python_version >= "3.0"',
        'requests[security] >= 2.20; python_version < "3.0"',
        'cache3',

    ],
    keywords=['eversend api payments'],
    classifiers= [
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ]
)