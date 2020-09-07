from setuptools import setup, find_packages


setup(
    name='ditrans2cldf',
    version='alpha1',
    description='',
    long_description='',
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    author='Johannes Englisch',
    author_email='johannes.englisch@uni-leipzig.de',
    url='',
    keywords='data linguistics',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'cldfbench',
        'openpyxl',
        'pybtex',
        'pyglottolog',
        'unidecode'],
    entry_points={
        'cldfbench.scaffold': [
            'ditransitive_db=ditrans2cldf.scaffold:DitransDBTemplate'
        ],
    },
    extras_require={
        'dev': ['flake8'],
        'test': [
            'tox',
            'pytest',
            'pytest-cov',
            'coverage',
        ],
    },
    tests_require=[],
    test_suite="ditrans2cldf")
