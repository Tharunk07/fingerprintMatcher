from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='fingerprintMatcher',
    version='1.0.6',
    author='Tharun K',
    author_email='tharunkkumarasamy@gmail.com',
    description='The FingerprintMatcher Python package provides a comprehensive toolkit for fingerprint matching and recognition tasks. With its intuitive interface and powerful functionality, this package enables users to compare fingerprint images, match them against a database of known fingerprints, and determine their similarity with high accuracy.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/Tharunk07/fingerprintMatcher',
    project_urls={
        'Bug Tracker': 'https://github.com/Tharunk07/fingerprintMatcher/issues'
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent'
    ],
    install_requires=['opencv-python>=4.9.0',
                      'opencv-contrib-python']
)
