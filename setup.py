import setuptools
import os

version = "0.0." + os.getenv("AZURE_BUILDID", "unknown")

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="test-wheel-package-LingchenZhu",
    version=version,
    author="Lingchen Zhu",
    author_email="zhulingchen@gmail.com",
    description="A very simple example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/zhulingchen/test-wheel",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)