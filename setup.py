import setuptools

with open("README.md","r",encoding="utf-8") as f:
    long_description = f.read()

__version__ = "0.0.0"


REPO_NAME = "Kidney-Disease-Classification-DL-Project-01"
AUTHOR_USER_NAME = "shangeethAlex"
SRC_REPO = "Kidney-Disease-Classifier"
AUTHOR_EMAIL = "shangeethmathan2020@gmail.com"


setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for kidney disease app",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)