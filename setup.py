from setuptools import setup

setup(
    name='Flask gitrcv',
    version='0.1',
    long_description=__doc__,
    packages=['flask-gitrcv'],
    include_package_data=True,
    zip_safe=False,
    install_requires=['Flask', 'GitPython']
)
