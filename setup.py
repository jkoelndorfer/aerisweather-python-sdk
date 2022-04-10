#!/usr/bin/env python3

"""
aerisweather setup
------------------

The packaging configuration for the AerisWeather Python SDK.
"""

from os import path

from setuptools import setup

thisdir = path.dirname(path.abspath(__file__))

with open(path.join(thisdir, "README.md"), "r") as f:
    readme = f.read()

source_url = "https://www.github.com/aerisweather/python_sdk"

install_requires = [
    "requests >= 2.0.0, < 3.0.0",
]

if __name__ == "__main__":
    setup(
        name="aerisweather",
        setup_requires=["setuptools_scm"],
        use_scm_version=True,
        description="The AerisWeather Python SDK",
        long_description=readme,
        long_description_content_type="text/markdown",
        author="John Koelndorfer",
        author_email="jkoelndorfer@aerisweather.com",
        url=source_url,
        include_package_data=True,
        package_data={"": ["LICENSE", "py.typed", "README.md"]},
        package_dir={"aerisweather": "aerisweather"},
        python_requires=">=3.6.0",
        install_requires=install_requires,
        classifiers=[
            "Development Status :: 2 - Pre-Alpha",
            "License :: OSI Approved :: MIT License",
            "Natural Language :: English",
            "Operating System :: OS Independent",
            "Programming Language :: Python :: 3 :: Only",
            "Programming Language :: Python :: 3.6",
            "Programming Language :: Python :: 3.7",
            "Programming Language :: Python :: 3.8",
            "Programming Language :: Python :: 3.9",
            "Programming Language :: Python :: 3.10",
            "Topic :: Internet :: WWW/HTTP",
            "Topic :: Scientific/Engineering :: Atmospheric Science",
            "Topic :: Software Development :: Libraries",
        ],
        project_urls={
            "Source": source_url,
        },
    )
