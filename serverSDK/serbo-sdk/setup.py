from setuptools import setup, find_packages

setup(
    name="serbot-sdk",
    version="1.0.0",
    author="👨‍💻Dipenkumar Padhiyar",
    author_email="dipen0padhiyar@gmail.com",
    description="A Python SDK for monitoring server metrics and websites.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/dipenpadhiyar/",
    packages=find_packages(),
    install_requires=[
        "psutil>=5.9.0",
        "requests>=2.25.1"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
