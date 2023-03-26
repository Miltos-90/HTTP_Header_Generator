from setuptools import setup, find_namespace_packages


with open('./README.md', 'r') as f: README = f.read()

setup(
    name="random-header-generator", 
    version="1.2",
    author="miltos_90",
    description='Generator of random, realistic http headers.',
    long_description=README,
    long_description_content_type="text/markdown",
    license="GNU General Public License v3.0",
    python_requires='>=3.10',
    include_package_data = True,
    packages=find_namespace_packages(),
    install_requires=["bs4", "requests"],
    keywords=['python', 'headers', 'http'],
    classifiers=[
    "Environment :: Web Environment",
    "Intended Audience :: Developers",
    "Operating System :: OS Independent",
    "License :: OSI Approved :: Apache Software License",
    "Programming Language :: Python",
    "Topic :: Internet :: WWW/HTTP",
    "Topic :: Software Development :: Libraries :: Python Modules",
    "Programming Language :: Python :: 3.10",
    ],
)