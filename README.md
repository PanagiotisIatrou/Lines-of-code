# Lines-of-code
A quick python script to find total lines of code of specific files in a directory.
It is used to only include specific file extensions and is meant to use only in Terminal as it relies heavily on command line arguements.

It is useful because it allows you to find how many lines of code you've written in a big project.

# How to Use
The **first parameter** should always be the **root directory**. Make sure to include the path in **double quotes ""** so that it works with directories that contain spaces.

**Prameters:**
- **-p** prints the name of every file, as well as the lines of code it contains.
- **[ext]** is used to include files with ext extension. For example, [.py], [.cpp], [.cs.meta]. You can add as many of those as you want. 

# Examples
- ```lines_of_code "MyDirectory\my files" [.py]```
- ```lines_of_code "MyDirectory\my files" -p [.py]```
- ```lines_of_code "MyDirectory\my files" [.py] [.cs] [.cs.meta] [.txt]```
