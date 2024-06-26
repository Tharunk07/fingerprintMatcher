# Fingerprint Matcher

https://pypi.org/project/fingerprintMatcher/

The Fingerprint Matcher package provides functionalities for matching fingerprint images and querying a database of fingerprint images.

## Installation

You can install the Fingerprint Matcher package using pip:

```bash
pip install fingerprintMatcher
```

# Usage

# Matching Two Fingerprint images

To match two fingerprint images and check if they are similar, you can use the match_fingerprints method:

```bash
from fingerprintmatcher import fingerprintMatcher

# Create an instance of the FingerprintMatcher class
fingerprint_matcher = fingerprintMatcher()

# Match two fingerprint images
fingerprint_matcher.match_fingerprints("path/to/image1", "path/to/image2")
```
Replace "path/to/image1" and "path/to/image2" with the file paths of the fingerprint images you want to compare.

# Matching with a database

To match a fingerprint image with a database of fingerprint images, you can use the match_with_database method:

```bash
from fingerprintmatcher import fingerprintMatcher

# Create an instance of the FingerprintMatcher class
fingerprint_matcher = fingerprintMatcher()

# Match with a database
fingerprint_matcher.match_with_database("path/to/test_image", "path/to/database_folder")
```

Replace "path/to/test_image" and database path "path/to/database_folder" of the fingerprint images and database you want to compare.

# Dependencies

- OpenCV
- NumPy


# Contributing

If you'd like to contribute to Fingerprint Matcher, please fork the repository and submit a pull request. You can also open an issue if you encounter any bugs or have suggestions for improvements.

# License

This project is licensed under the MIT License - see the LICENSE file for details.

