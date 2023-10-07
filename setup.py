from setuptools import setup, find_packages

setup(
    name="safe_print",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "colorama"
    ],
    author="SyntaxSurge",
    author_email="syntaxsurge@gmail.com",
    description="A utility for safely printing with optional color formatting and logging to file.",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    license="MIT",
    url="https://github.com/syntaxsurge/safe_print",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
)
