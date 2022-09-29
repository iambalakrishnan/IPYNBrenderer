from ensurepip import version
import setuptools
with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

__version__ = "0.0.0"

REPO_NAME = "IPYNBrenderer"
AUTHOR_NAME = "iambalakrishnan"
AUTHON_EMAIL = "imbkrishnaa@gmail.com"
SRC_REPO = "IPYNBrenderer"

setuptools(
    name=SRC_REPO,
    version=__version__,
    author_email=AUTHOR_EMAIL,
    description="A small python package",
    Long_description=long_description,
    long_description_contect="text/markdown",
    url=f"https://github.com/{AUTHOR_NAME}/{REPO_NAME}"
    project_urls={
        "bug Tracker": f"https://github.com/{AUTHOR_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")

)