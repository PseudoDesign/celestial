from setuptools import setup
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

# Arguments marked as "Required" below must be included for upload to PyPI.
# Fields marked as "Optional" may be commented out.

setup(
    name='celestial_tools',
    version='0.0.1',
    description='A collection of tools for managing and debugging embedded software',  # Optional
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/pseudodesign/celestial',
    author='PseudoDesign',
    author_email='info@pseudo.design',
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    packages=["celestial_tools"],
    python_requires='>=3.5',
    install_requires=[],
    extras_require={
        'test': ['coverage', 'behave'],
        'docs': ['sphinx'],
    },
    # If there are data files included in your packages that need to be
    # installed, specify them here.
    package_data={

    },
    entry_points={
        'console_scripts': [
            'celestial_dual_rootfs_update=celestial_tools.client.dual_rootfs_update:dual_rootfs_update_cmdline',
        ],
    },

)
