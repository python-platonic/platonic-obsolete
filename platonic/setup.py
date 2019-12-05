import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="platonic",
    version="2.0.0",
    author="Anatoly Scherbakov",
    author_email="altaisoft@gmail.com",
    description=(
        "A library of common data structures with implementable backends."
    ),
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/anatoly-scherbakov/platonic',
    packages=setuptools.find_packages(),
    install_requires=[
        'typing_inspect'
    ],
    extras_require={
        'dev': [
            'pytest',
            'boto3',
            'boto3_type_annotations'
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
