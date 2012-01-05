from setuptools import setup, find_packages

setup(
    name = "djangoqa",
    version = "1.0",
    url = 'https://github.com/gauravtech4u/djangoqa',
    license = 'BSD',
    description = "Questionnaire App",
    author = 'Gaurav Kapoor',
    packages = find_packages('src'),
    package_dir = {'': 'src'},
    install_requires = ['setuptools'],
)
