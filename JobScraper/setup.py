from setuptools import setup, find_packages

VERSION = '0.0.1' 
DESCRIPTION = 'JobScraper'
LONG_DESCRIPTION = '''
    Get Active Job Listings from the top 6 search engines
        - LinkedIn
        - Monster
        - Indeed
        - Dice
        - ZipRecruiter
        - Google
    
    Construct a new class of Scraper, by defing the 
        @param days_ago: Int = How recent was the job posted
        @param job_title: String = What Job do you want
'''

# Setting up
setup(
    # the name must match the folder name 'verysimplemodule'
    name="verysimplemodule", 
    version=VERSION,
    author="Brandon Montalvo",
    author_email="brandon.montalvo@colorado.edu",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=[], # add any additional packages that 
    # needs to be installed along with your package. Eg: 'caer'
    
    keywords=['python', 'first package'],
    classifiers= [
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Education",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
