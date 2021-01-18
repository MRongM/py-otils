from setuptools import setup, find_packages

name = "otils"
setup(
    name=name,
    version="1.0.3",
    keywords=[name, ],
    description=f"{name} tools",
    long_description=open('README.md', 'r', encoding='utf8').read(),
    license="MIT",
    url="https://github.com/MRongM/py-otils.git",
    author="MRongM",
    author_email="idskof@sina.cn",
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
