# Cracker
[![Code Climate](https://codeclimate.com/github/aaronjwood/cracker/badges/gpa.svg)](https://codeclimate.com/github/aaronjwood/cracker)
[![Codacy Badge](https://api.codacy.com/project/badge/grade/3586d4c5ce8840ee9f1ecec1bdb482aa)](https://www.codacy.com/app/aaronjwood/cracker)

This tool applies a brute force method against various types of hashes to try and crack them.
Currently, the supported hashes are:
* MD5
* MD4
* LM
* NTLM
* SHA1
* SHA224
* SHA256
* SHA384
* SHA512

It tries to be more efficient by parallelizing the work performed on different character sets.
For example, if the character set abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ is selected then one worker will work with abcdefghijklmnopqrstuvwxyz, another worker will work with ABCDEFGHIJKLMNOPQRSTUVWXYZ, and the last worker will work with abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ.

