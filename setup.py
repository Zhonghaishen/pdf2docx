#!/usr/bin/env python
# -*- coding: utf-8 -*-


from setuptools import find_packages, setup

EXCLUDE_FROM_PACKAGES = ["build", "dist", "test"]

def load_requirements(fname):
    try:
        from pip._internal.req import parse_requirements
    except ImportError:
        from pip.req import parse_requirements
    reqs = parse_requirements(fname, session="test")
    return [str(ir.req) for ir in reqs]


setup(
    name="pdf2docx",    
    version="1.0.0",
    keywords = ["pdf-to-word", "pdf-to-docx"],
    description="parse PDF files to docx",
    long_description = "parse PDF file with PyMuPDF and generate docx with python-docx",
    license = "GPL v3", 
    author="dothinking",
    author_email="train8808@gmail.com",
    url="https://github.com/dothinking/pdf2docx",
    packages=find_packages(exclude=EXCLUDE_FROM_PACKAGES),
    include_package_data=True,    
    zip_safe=False,
    install_requires=load_requirements("requirements.txt"),
    python_requires=">=3.6",
    entry_points={
        "console_scripts": [
            "pdf2docx=pdf2docx.main:main"
            ]},
)