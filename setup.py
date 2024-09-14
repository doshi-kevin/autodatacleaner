from setuptools import setup, find_packages

setup(
    name='autodatacleaner',                  # Name of the package
    version='0.1.0',                         # Package version
    author='Kevin Doshi',                      # Your name or organization
    author_email='kevin.doshi2@spit.ac.in',   # Your email
    description='A simple package for cleaning data by removing duplicates',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',  # Format for long description
    url='https://github.com/doshi-kevin/autodatacleaner.git',  # URL of your package repository
    packages=find_packages(),                # Automatically find packages in your project
    classifiers=[                            # Additional metadata
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',                 # Minimum Python version
    install_requires=[                       # External dependencies, if any
        'pandas',
    ],
)
