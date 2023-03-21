from setuptools import setup


with open('./README.md', 'r') as f: README = f.read()

# Setting up
setup(
       # the name must match the folder name 'verysimplemodule'
        name="http-headers", 
        version="1.1.0",
        author="miltos_90",
        description='Generator of random, realistic http headers.',
        long_description=README,
        long_description_content_type="text/markdown",
        packages=["http_headers"],
        license="GNU General Public License v3.0",
        install_requires=["bs4", "requests"],
        keywords=['python', 'first package'],
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