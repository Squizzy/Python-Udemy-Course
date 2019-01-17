#
# ### basic method
# jabber = open("sample.txt", 'r')
# # jabber = open("D:\Github\Squizzy\Python-Udemy-Course\Python-Files\FileIO\sample.txt", 'r')
# ## in path use \\ to make sure it is interpreted as a path
# # jabber = open("D:\\Github\\Squizzy\\Python-Udemy-Course\\Python-Files\\FileIO\\sample.txt", 'r')
#
# for line in jabber:
#     if "jabberwock" in line.lower():  # find only the lines which have this word.
#                                       # .lower testing if upper or lowercase
#         print(line, end='')  # end='' prevents printing the new line by print,
#                              # as the one from the text is imported as \n
#
# jabber.close()

# ### method that doesn't require to close the file.
# # Also, if there is an error in the program when the file is still open,
# # this could close issues when opening the file again
# # but the below method avoids that - this will close the file before the error finishes
# with open("sample.txt", 'r') as jabber:
#     for line in jabber:
#         if "JAB" in line.upper():
#             print(line, end='')


# ### trapping if the file was empty
# with open("sample.txt", 'r') as jabber:
#     line = jabber.readline()
#     while line:
#         print(line, end='')
#         line = jabber.readline()

### inport all the lines at once
with open("sample.txt", 'r') as jabber:
    lines = jabber.readlines()  # read the whole file, converts to a list
print(lines)

### display all the lines
for line in lines:
    print(line, end='')

### display all the lines in reverse
for line in lines[::-1]:
    print(line, end='')

### read the whole file as one string
with open("sample.txt", 'r') as jabber:
    lines = jabber.read()  # read the whole file, converts to a string

### display all the text in reverse, as lines contains the whole text as a string
for line in lines[::-1]:
    print(line, end='')
