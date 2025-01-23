from setuptools import setup, find_packages

setup(
    name="wireless_localization_frs_uofu",                     # Your package name
    version="0.1.0",                      # Package version
    author="University of Utah",                   # Your name
    author_email="mumtahinhabibrafi66@gmail.com", # Your email
    description="A library to fetch my dataset in JSON/CSV format.", # Short description
    long_description=open("README.md").read(),  # Long description from README
    long_description_content_type="text/markdown",  # Content type of the README
    url="https://github.com/mhrafi66/wireless_localization_frs_uofu/tree/main",  # Your GitHub repository
    packages=find_packages(),              # Automatically find packages in the project
    install_requires=[
        "pandas",                          # Dependencies
        "json",                          # Dependencies
        "requests"
    ],
    classifiers=[                          # Metadata about your package
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",               # Minimum Python version
)
