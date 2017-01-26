
from setuptools import find_packages
from setuptools import setup

# Setup installation dependencies, removing some so they
# can build on the ppa
install_requires = [
    'setuptools',
    'PyYAML',
]

setup(
    name='groot_ansible',
    version='0.1.0',
    packages=find_packages(exclude=['tests*', 'docs*']),
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
            'groot-ansible = groot_ansible.vci:main',
        ],
    },
)
