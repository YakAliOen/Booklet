from os import chdir, listdir
from subprocess import run
from platform import system
from cs50 import get_string

confirm = ""

while confirm not in ["Y", "N"]:
    confirm = get_string("Do you want to print the converted files (Y/N)? ").strip().upper()

if confirm == "N":
    print("Exiting...")
    exit()

chdir("files_booklet")

files = listdir()

print_commands = []
os_name = system()
for f in files:
    if os_name == "Darwin":
        if f == ".DS_Store":
            continue
        print_commands.append(f"lp -o number-up=2 -o sides=two-sided-short-edge -o media=A4 {f}")
    elif os_name == "Windows":
        print_commands.append(f"lpr -o sides=two-sided-short-edge -o media=A4 {f}")
    else:
        print("Unsupported OS")
        exit()

for command in print_commands:
    run(command, shell=True)
print("Printing complete.")
