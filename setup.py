import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="rvmerge",
    version="1.0.0",
    author="Jean-Marie Couteyen",
    author_email="jm_couteyen@yahoo.fr",
    description="A simple program to merge recto / verso PDFs.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jm-cc/rvmerge/",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=["pikepdf"],
    entry_points={"console_scripts": ["rvmerge=rvmerge.rvmerge:main"]},
)
