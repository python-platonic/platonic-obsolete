import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="platonic-sorted",
    version="0.0.2",
    author="Anatoly Scherbakov",
    author_email="altaisoft@gmail.com",
    description=(
        "Sorted containers mix-ins and algorithms"
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
            'coverage'
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
