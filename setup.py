
import os

from setuptools import find_packages
from setuptools import setup
from groot_ansible import __version__

# Setup installation dependencies, removing some so they
# can build on the ppa
install_requires = [
    'setuptools',
    'PyYAML',
    'ansible',
]


def roles():
    """
    Relative pathnames of all files in the groot_ansible/playbooks/roles folder
    """
    return [os.path.relpath(os.path.join(root, filename), 'groot_ansible')
            for root, _, filenames in os.walk('groot_ansible/playbooks/roles') for filename in filenames if '.git' not in root.split(os.sep)
            ]


def modules():
    """
    Relative pathnames of all modules in the groot_ansible/playbooks/library folder
    """
    return [os.path.relpath(os.path.join(root, filename), 'groot_ansible')
            for root, _, filenames in os.walk('groot_ansible/playbooks/library') for filename in filenames if '.git' not in root.split(os.sep)
            ]

setup(
    name='groot_ansible',
    version=__version__,
    packages=find_packages(exclude=['tests*', 'docs*']),
    package_data={
        'groot_ansible': [
            'playbooks/*.yaml',
        ] + roles() + modules(),
    },
    data_files=[],  # system files?
    install_requires=install_requires,
    author='Daniel Stonier',
    author_email='d.stonier@gmail.com',
    maintainer='Daniel Stonier',
    maintainer_email='d.stonier@gmail.com',
    url='http://github.com/stonier/groot_ansible',
    keywords=['catkin'],
    classifiers=[
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Topic :: System :: Systems Administration',
        'Topic :: Utilities'
    ],
    description="system installation and update scripts",
    long_description="Python wrapped ansible for setting up and updating systems for various use cases.",
    license='BSD',
    # test_suite='tests',
    entry_points={
        'console_scripts': [
            'groot-ansible = groot_ansible:main',
        ],
    },
)
