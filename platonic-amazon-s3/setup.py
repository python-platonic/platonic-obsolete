import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="platonic-amazon-s3",
    version="0.0.1",
    author="Anatoly Scherbakov",
    author_email="altaisoft@gmail.com",
    description=(
        "S3 backend for some of platonic data structures."
    ),
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/anatoly-scherbakov/platonic',
    packages=setuptools.find_packages(),
    install_requires=[

    ],
    extras_require={
        'dev': [
            'pytest',
            'boto3'
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
