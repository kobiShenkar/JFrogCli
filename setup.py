from setuptools import setup, find_packages


setup(
    # include_package_data=True,
    name='FrogCli',
    version='5.0.0',
    packages=find_packages(),
    package_data={
        '': ['*.txt', '*.json']
    },
    entry_points={
        'console_scripts': [
            'FrogCli = FrogCli.main:cli'
        ]}
)

