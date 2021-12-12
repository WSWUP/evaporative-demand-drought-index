import io, re
from setuptools import setup

with io.open("README.rst", "rt", encoding="utf8") as f:
    readme = f.read()

with io.open("eddi/__init__.py", "rt", encoding="utf8") as f:
    version = re.search(r"__version__ = \'(.*?)\'", f.read()).group(1)

requires = [
    'bottleneck',
    'numpy',
    'pandas',
    'scipy',
    'statsmodels',
    'refet'
    
]

tests_require = ['pytest']

classifiers = [
    'License :: OSI Approved :: Apache Software License',
    'Programming Language :: Python :: 3.7',
    'Environment :: Console',
    'Development Status :: 4 - Beta',
    'Topic :: Scientific/Engineering',
    'Intended Audience :: Science/Research'
]

setup(
    name='eddi',
    description='Tools for calculating evaporative demand drought index and similar indices',
    long_description=readme,
    author='Daniel McEvoy and John Volk',
    author_email='john.volk@dri.edu',
    license='Apache',
    python_requires='>=3.7',
    version=version,
    url='https://github.com/WSWUP/evaporative-demand-drought-index',
    platforms=['Windows','Linux','Mac OS X'],
    classifiers=classifiers,
    packages=['eddi'],
    install_requires=requires,
    tests_require=tests_require,
    include_package_data=True,
)
