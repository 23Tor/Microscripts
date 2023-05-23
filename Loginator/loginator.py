import os

# Specify the folder path containing the .tsv files
folder_path = 'a/folder/path'

# Specify the output file path
output_file = 'the/output/file/path.txt'

# Get a list of all .tsv files in the folder
file_list = [f for f in os.listdir(folder_path) if f.endswith('.tsv')]

# Sort the file list based on the date and time in the file name
file_list.sort()

with open(output_file, 'a') as output:
    for file_name in file_list:
        with open(os.path.join(folder_path, file_name), 'r') as file:
            contents = file.read()
            output.write(contents)