from setuptools import setup, find_packages

with open("README.md") as f:
    long_description = f.read()

setup(
    name="dwanimes",
    version="0.0.1",
    scripts=[
        "dw-animes=downloader/main.py"
    ],
    packages=find_packages(),
    author="Joaquín Buendía",
    description="Download your anime",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords=["download", "anime"]
)
