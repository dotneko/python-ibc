from setuptools import setup

######################################################################################################
################ You May Remove All the Comments Once You Finish Modifying the Script ################
######################################################################################################

setup(
    name = 'cosmpy-api',
    version = '0.2.0',
    description = 'A library to make developing python based programs on cosmos chains easier',  
    py_modules = ["cosmpy_api"],
    package_dir = {'':'src'},
    packages = [
        'cosmpy_api',
        'cosmpy_price',
        'cosmpy_chain',
    ],
    author = 'Reece Williams',
    author_email = 'reecepbcups@gmail.com',
    # long_description = open('README.md').read() + '\n\n' + open('CHANGELOG.md').read(),
    long_description = open('README.md').read() + '\n\n',
    long_description_content_type = "text/markdown",
    url='https://github.com/Reecepbcups/cosmpy-api',
    include_package_data=True,
    classifiers  = [
        'Development Status :: 4 - Beta',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        "License :: OSI Approved :: BSD License",
        'Intended Audience :: Developers',
        'Intended Audience :: Other Audience',
        'Intended Audience :: Science/Research',
        'Intended Audience :: Education',
        'Topic :: Text Processing',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: OS Independent',
    ],
    install_requires = [
        # 'requests ~= 2.28.1',
        'requests>=2.20.0',
    ],
    keywords = ['Cosmos Blockchain', 'Cosmoshub', "atom token"],
)