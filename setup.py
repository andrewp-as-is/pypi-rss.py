import setuptools

setuptools.setup(
    name='pypi-rss',
    version='2020.12.3',
    install_requires=open('requirements.txt').read().splitlines(),
    packages=setuptools.find_packages()
)
