from setuptools import find_packages, setup

setup(
    name="lab4",
    packages=find_packages(exclude=["lab4_tests"]),
    install_requires=[
        "dagster",
        "dagster-cloud"
    ],
    extras_require={"dev": ["dagit", "pytest"]},
)
