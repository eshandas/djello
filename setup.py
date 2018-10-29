from setuptools import find_packages, setup
# Read more here: https://pypi.org/project/twine/

setup(
    name='djello',
    packages=find_packages(),
    include_package_data=True,
    version='0.1',
    description='A pretty and configurable admin panel to enhance the default Django Admin Panel based on Ela Admin',
    author='Eshan Das',
    author_email='eshandasnit@gmail.com',
    url='',  # use the URL to the github repo
    download_url='',  # Create a tag in github
    keywords=['django', 'admin', 'panel', 'dashboard'],
    classifiers=[],
    install_requires=[
        'Django>=2.0',
        'django-widget-tweaks>=1.4.3'],
)
