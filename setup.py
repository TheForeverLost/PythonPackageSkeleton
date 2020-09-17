import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="SamplePythonSkeleton", # Replace with your own username
    version="0.0.1",
    author="Alan John",
    author_email="alanpjohn@outlook.com",
    description="A small example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/TheForeverLost/PythonPackageSkeleton",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        "requests","pytest" 
    ],#optional
    python_requires='>=3.6',
)