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

### Requirements

Python 3

### Performance

While this tool does what it's supposed to, it has some major downfalls.
For starters, it's using Python. I'm not saying Python is a bad language or anything like that.
The issue is Python's [GIL](https://wiki.python.org/moin/GlobalInterpreterLock) which prevents multiple threads from executing Python's bytecode at the same time.
This means that I am unable to achieve parallelism with threads since only one character set would be worked on at a time.
What needs to be done instead is splitting the work up across multiple processes and share data across those processes.
This is less efficient than working with threads in general but is a necessary evil with Python.
Additionally, interpreted languages are not well suited to workloads that are 100% focused on compute.
See the recommendations below for what you should do if you're serious about using this kind of tool.


### Recommendations

You could consider this project an example of how to accomplish such a task using Python and an example of what kinds of issues you'd run into.
The tool is certainly usable and may work for your scenario but keep in mind that it will run far slower than anything written in C, C++, Rust, or Go.
If you require the highest performance possible get yourself a GPU and don't bother using any tools (including this one) that target the CPU.
Look for something that makes use of CUDA, OpenCL, or ACL which will bring you into the domain of billions of hashes per second.