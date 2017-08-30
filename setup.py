from setuptools import setup, find_packages

with open('README.rst', 'r', encoding='utf-8') as f:
    long_description = f.read()


setup(
    name='jacquard-jaf',
    version='0.1.0',
    url='https://github.com/prophile/jacquard-jaf',
    description="Analysis framework for Jacquard",
    long_description=long_description,

    author="Alistair Lynn",
    author_email="alistair@alynn.co.uk",

    keywords = (
        'ab-testing',
        'e-commerce',
        'experiments',
        'jacquard',
        'metrics',
        'redis',
        'science',
        'split-testing',
        'testing',
        'zucchini',
    ),
    license='MIT',

    zip_safe=False,

    packages=find_packages(),

    classifiers=(
        'Development Status :: 2 - Pre-Alpha',
        'Environment :: Console',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: POSIX',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Office/Business',
    ),

    install_requires=(
        'jacquard >=0.4.0',
        'numpy',
        'scipy',
        'sqlalchemy',
    ),

    setup_requires=(
        'pytest-runner',
    ),

    tests_require=(
        'pytest',
        'hypothesis',
    ),
)
