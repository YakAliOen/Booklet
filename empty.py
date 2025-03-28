from subprocess import run
import os
from platform import system
from sys import exit
from cs50 import get_string

confirm = ""
while confirm not in ["Y", "N"]:
    confirm = get_string("Are you sure you want to delete files (Y/N): ").strip().upper()

if confirm == "N":
    print("Exiting...")
    exit()

upload_files = os.listdir("files_upload")
booklet_files = os.listdir("files_booklet")

os_name = system()

if os_name == "Darwin":
    upload_files.remove(".DS_Store")
    booklet_files.remove(".DS_Store")

for file in upload_files:
    file_path = os.path.join("files_upload", file)
    try:
        os.remove(file_path)
    except Exception as e:
        print(f"Error deleting {file_path}: {e}")

for file in booklet_files:
    file_path = os.path.join("files_booklet", file)
    try:
        os.remove(file_path)
    except Exception as e:
        print(f"Error deleting {file_path}: {e}")

print("Files removed successfully")
