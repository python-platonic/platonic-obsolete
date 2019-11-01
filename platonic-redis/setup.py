import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="platonic-redis",
    version="0.0.1",
    author="Anatoly Scherbakov",
    author_email="altaisoft@gmail.com",
    description=(
        "Redis backend for Mapping."
    ),
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/anatoly-scherbakov/platonic',
    packages=setuptools.find_packages(),
    install_requires=[
        'redis'
    ],
    extras_require={
        'dev': [
            'pytest',
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
