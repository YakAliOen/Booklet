from cs50 import get_int, get_string
from termcolor import colored
from booklet import Booklet

uploads = "files_upload"
save = "files_booklet"

booklet = Booklet(uploads, save)

def main():
    booklet.show_uploads()

    files = booklet.list_files()

    while True:
        f = get_int("Which file do you wanna convert (file number): ")
        while f > len(files) or f < 1:
            f = get_int("Which file do you wanna convert (file number): ")

        convert_booklet = booklet.convert(files[f - 1])
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
            continue
        else:
            break


if __name__ == "__main__":
    main()
