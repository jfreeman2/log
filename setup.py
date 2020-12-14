from setuptools import setup, find_packages

setup(
    name="log",
    version="0.0.1",
    include_package_data=True,
    description='Logging Package',
    long_description="""Logging Package""",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    url="https://github.com/jfreeman2/log.git",
    author="John Freeman",
    author_email="johnfreeman210@gmail.com",
    license="MIT",
    platforms=["any"],
    python_requires=">=3.6",
)