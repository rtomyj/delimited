#Delimited

Python script that summarizes lines of a file that are delimited by any delimiter. 

User can specify the file to process (arg 0), number of rows to process (arg 1), and delimiter being used (arg 2). 

#Defualts
arg 1 is -1 (processes the whole file)
arg 2 is \t (tab)

#Needed
arg 0 (file name to process)

#Features
Program will process the first row it sees that is delimited by delimiter user chose. The number of columns in that first row will be saved. 
Any time it sees that a line has the same number of columns after it is split using the delimiter it assumes the line is a row of importance. 
This means that a file can have a mix of delimited lines and lines that aren't delimited but the script will only summarize the tab delimited ones.
