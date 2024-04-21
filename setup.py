from setup_tools import find_packages,setup

setup(
    name = 'mlproject',
    version = '0.0.1',
    author = 'TTRV',
    author_email = 'basavadinesh7@gmail.com',
    packages = find_packages(),
    install_requires = ['numpy','pandas','seaborn']




)