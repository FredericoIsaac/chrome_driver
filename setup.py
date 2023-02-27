from setuptools import setup, find_packages

setup(
    name="driver_local",
    version="0.2.0",
    license='MIT',
    author="Frederico Gago",
    author_email='fredyisaac@gmail.com',
    packages=find_packages(),
    url='https://github.com/gmyrianthous/example-publish-pypi',
    keywords='chrome driver selenium',
    install_requires=["selenium==4.1.3",
                      "beautifulsoup4==4.10.0",
                      "pywin32==303",
                      "requests==2.27.1",
                      "setuptools==67.4.0"
                      ]
)
