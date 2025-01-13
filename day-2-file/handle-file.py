# # create myfile.txt file with 3 lines of "Hello World"
# with open("myfile.txt", "w") as f:
#     f.write("Hello\nWorld\n")

# Instead of try/finally to cleanup resources you can use a with statement
# with open("myfile.txt") as f:
#     for line in f:
#         print(line.strip())  # remove extra line breaks


# Writing to a file
# contents = {"aa": 12, "bb": 21}
# with open("myfile1.txt", "w") as file:
#     file.write(str(contents))        # writes a string to a file
#
# import json
# with open("myfile2.txt", "w") as file:
#     file.write(json.dumps(contents))  # writes an object to a file

import pandas as pd


def main():
    # using try catch to handle exceptions
    try:
        with open("demo.csv", "r") as f:
            df = pd.read_csv(f)
            # typeof df
            print(type(df))
            print(df)
    except FileNotFoundError:
        print("File not found")


if __name__ == "__main__":
    main()
