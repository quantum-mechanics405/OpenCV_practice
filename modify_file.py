import os

file_path = r'C:\Users\DELL\Desktop\Computer vision\openCV\tutorial3.py'

# Check if the file exists
if os.path.exists(file_path):
    try:
        with open(file_path, 'a') as file:
            file.write("\nprint('Hello world')\n")
        print(f"Successfully added to {file_path}")
    except Exception as e:
        print(f"Error: {e}")
else:
    print(f"The file {file_path} does not exist.")
    

# @REM @echo off
# @REM REM Ensure we are in the correct Git repository directory
# @REM cd /d "C:\Users\DELL\Desktop\Computer vision\openCV"

# @REM REM Git commands to add, commit, and push changes
# @REM git add .
# @REM git commit -m "Automated commit: adding new line"
# @REM git push origin main

