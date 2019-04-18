from setuptools import setup, find_packages
setup(
 
    name = "Corsair Link",
    version = "0.1",
    packages = find_packages(),
 
    entry_points = {
        'console_scripts': [
            'cl = cl:main'
        ]
    },
 
    # metadata for upload to PyPI
    author = "Roman Stingler",
    author_email = "roman.stingler@symvaro.com",
    description = "A tool to communicate with Corsair link",
 
    license = "GPL2",
    keywords = "Corsair link linux",
    url = "https://github.com/romanstingler/corsairlink-linux",
 
    install_requires=[
        'ioctl-opt>=1.2'
    ],
 
)
