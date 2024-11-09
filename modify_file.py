# modify_file.py
file_path = r'C:\Users\DELL\Desktop\Computer vision\openCV\tutorial3.py'

with open(file_path, 'a') as file:  # Open file in append mode
    file.write("\nprint('Hello world')\n")  # Add the print statement
