# # create myfile.txt file with 3 lines of "Hello World"
# with open("myfile.txt", "w") as f:
#     f.write("Hello\nWorld\n")

# Instead of try/finally to cleanup resources you can use a with statement
# with open("file/myfile.txt") as f:
#     for line in f:
#         print(line.strip()) # remove extra line breaks

# Writing to a file
contents = {"aa": 12, "bb": 21}
with open("file/myfile1.txt", "w") as file:
    file.write(str(contents))        # writes a string to a file

import json
with open("file/myfile2.txt", "w") as file:
    file.write(json.dumps(contents))  # writes an object to a file