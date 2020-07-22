from setuptools import setup, find_packages
name = "otils"
setup(
    name=name,
    version="1.0",
    keywords=[name, ],
    description=f"{name} tools",
    long_description=open('README.md').read(),
    license="",
    url="",
    author="mrongm",
    author_email="",
    packages=find_packages(exclude=('test',)),
    include_package_data=True,
    platforms="any",
    install_requires=[

    ],
    scripts=[],
    entry_points={
        'console_scripts': [
        ]
    }
)
