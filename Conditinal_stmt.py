file = "raw_data.csv"

if file.endswith(".csv"):
    print("The file is a CSV file.")
elif file.endswith(".txt"):
    print("The file is a text file.")
elif file.endswith(".json"):
    print("The file is a JSON file.")
else:
    print("Unknown file type.")


'''startswith() and endswith() are string methods in Python
 that allow you to check whether a string starts or ends with
   a specific substring, respectively.'''

if file.startswith("raw"):
    print("The file name starts with 'raw'.")
elif file.startswith("processed"):
    print("The file name starts with 'processed'.")
elif file.startswith("final"):
    print("The file name starts with 'final'.")
else:
    print("Unknown file name prefix.")