from setuptools import find_packages, setup

setup(
    name="appify",
    version="0.0",
    entry_points={"console_scripts": ["appify=appify.__main__:main"]},
    author="Aarni Koskela",
    author_email="akx@iki.fi",
    license="MIT",
    install_requires=[],
    python_requires=">=3.6",
    packages=find_packages(include=("appify*",)),
)
