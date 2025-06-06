from cs50 import get_int, get_string
from termcolor import colored
from booklet import Booklet
from os import path, chdir
from subprocess import run


uploads = "files_upload"
save = "files_booklet"

booklet = Booklet(uploads, save)


def main():
    files = booklet.list_upload_files()

    option = get_string("Convert/Print (C/P): ").strip().upper()
    while option not in ["C", "P"]:
        option = get_string("Convert/Print (C/P): ").strip().upper()
    print()
    if option == "C":
        while True:
            # Shows all pdf files in uploads and whether they've already been converted or not
            converted_files = booklet.list_saved_files()
            for count, f in enumerate(files):
                if (f"{path.splitext(f)[0]}-booklet.pdf") in converted_files:
                    print(colored(f"{count+1}) {f} (Converted)", "green"))
                    continue
                print(f"{count+1}) {f}")

            # Ask user for which files they want to convert
            f = get_int("Which file do you wanna convert (file number): ")
            while f > len(files) or f < 1:
                f = get_int("Which file do you wanna convert (file number): ")
            convert_booklet = booklet.convert(files[f - 1])

            # Converting file to booklet
            if convert_booklet is None:
                continue
            else:
                print(convert_booklet)

            cont = get_string("Continue (Y/N)? ").strip().upper()

            while cont not in ["Y", "N"]:
                cont = get_string("Continue (Y/N)? ").strip().upper()

            if cont == "Y":
                print()
                continue
            else:
                break
    elif option == "P":
        converted_files = booklet.list_saved_files()
        chdir("files_booklet")
        while True:
            for count, f in enumerate(converted_files):
                print(f"{count+1}) {f}")

            # Ask user for which files they want to print
            f = get_int("Which file do you wanna print (file number): ")
            while f > len(converted_files) or f < 1:
                f = get_int("Which file do you wanna print (file number): ")

            # Printing file
            print(f"Printing {converted_files[f-1]}...")
            run(f"lp -o number-up=2 -o sides=two-sided-short-edge -o media=A4 {converted_files[f-1]}", shell=True)

            cont = get_string("Continue (Y/N)? ").strip().upper()

            while cont not in ["Y", "N"]:
                cont = get_string("Continue (Y/N)? ").strip().upper()

            if cont == "Y":
                print()
                continue
            else:
                break


if __name__ == "__main__":
    main()

