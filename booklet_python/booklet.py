from PyPDF2 import PdfReader, PdfWriter
from sys import exit
from termcolor import colored
from os import listdir, path


class Booklet:
    def __init__(self, upload_dir, save_dir):
        self.upload_dir = upload_dir
        self.save_dir = save_dir
        self.upload_files = sorted(
            [
                file
                for file in listdir(self.upload_dir)
                if path.splitext(file)[1].lower() == ".pdf"
            ]
        )

    @property
    def upload_dir(self):
        return self._upload_dir

    @upload_dir.setter
    def upload_dir(self, upload_dir):
        if not upload_dir:
            print(colored("Missing Upload Directory", "red"))
            exit()

        if path.isdir(upload_dir):
            self._upload_dir = upload_dir
        else:
            print(colored(f"The directory '{upload_dir}' does not exist.", "red"))
            exit()

    @property
    def save_dir(self):
        return self._save_dir

    @save_dir.setter
    def save_dir(self, save_dir):
        if not save_dir:
            print(colored("Missing Upload Directory", "red"))
            exit()

        if path.isdir(save_dir):
            self._save_dir = save_dir
        else:
            print(colored(f"The directory '{save_dir}' does not exist.", "red"))
            exit()

    def list_saved_files(self):
        return sorted(
            [
                file
                for file in listdir(self.save_dir)
                if path.splitext(file)[1].lower() == ".pdf"
            ]
        )

    def list_upload_files(self):
        return self.upload_files

    def convert(self, f):
        if f not in self.upload_files:
            print(colored(f"{f} cannot be found in {self.upload_dir}", "red"))
            return None

        file = f"{self.upload_dir}/{f}"

        reader = PdfReader(file)

        num_of_pages = len(reader.pages)

        if (num_of_pages < 4) or (num_of_pages % 4 != 0):
            print(
                colored(
                    f"File doesn't have appropriate number of pages\n-->{f} has {num_of_pages} pages. Number of pages must be more than 4 and divisible by 4.",
                    "red",
                )
            )
            return None

        page_order = []

        for i in range(1, (int(num_of_pages / 2) + 1)):
            if i % 2 == 1:
                page_order.append(num_of_pages - (i - 1))
                page_order.append(i)
            else:
                page_order.append(i)
                page_order.append(num_of_pages - (i - 1))

        writer = PdfWriter()
        for i in page_order:
            writer.add_page(reader.pages[i - 1])

        with open(
            f"{self.save_dir}/{path.splitext(f)[0]}-booklet.pdf", "wb"
        ) as new_file:
            writer.write(new_file)

        return colored(f"File {f} converted", "green")
