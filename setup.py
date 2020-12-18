import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="test-wheel-package-LingchenZhu",
    version="0.0.1",
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