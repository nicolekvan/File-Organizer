# File-Organizer
ICS 32 Assignment 1
This code is a simple file inspector that takes input from the user in a command line. In this program, I imported the Path module from pathlib to use various functions, implemented when checking if the path contains (sub) files and (sub) directories. 

The while loop breaks when the user inputs 'q' or if there is not a valid input. The input must contain a command: "q" quit or "l" meaning list, a path, and optional options. The function output_directory takes 3 options, "-f" to output files, "-s" to search files, and "-e" to output certain extentions. All options take another option, "-r" which prints further files/directories recursively.
