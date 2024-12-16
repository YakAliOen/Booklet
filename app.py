from cs50 import get_int, get_string
from termcolor import colored
from booklet import Booklet
from os import path


uploads = "files_upload"
save = "files_booklet"

booklet = Booklet(uploads, save)

def main():
    files = booklet.list_upload_files()

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
            print("To print your file, execute this command:")
            print(colored(f"lp -o number-up=2 -o sides=two-sided-short-edge -o media=A4 {files[f - 1]}-booklet.pdf", "light_yellow"))

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
