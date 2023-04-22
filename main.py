import urllib.request
from termcolor import colored
import os

print(colored("\nWellcome to Files-Downloader 2023!", "red"))

is_running = True
while is_running:
    option = int(input(f"""\n{colored("What you wanna do?", "cyan")}
    1. Download file
    2. Exit
    Choose: """))

    try:
        if option == 1:
            # https://archive.org/download/rem-apkthrone.com/rem-apkthrone.com_archive.torrent
            file_url = input("\nWhich is the file url?: ")
            extension = file_url[file_url.rindex(".")+1:]
            file_name = file_url[file_url.rindex("/")+1: file_url.rindex(".")]
            final_path = f"{os.path.dirname(__file__)}/downloads/{file_name}.{extension}"
            print("\nDownloading...")
            # download
            urllib.request.urlretrieve(file_url, final_path)

            print(colored("\n***Finished!", "green"))
        elif option == 2:
            is_running = False
        else:
            print("\nThat's not an option...")
    except:
        print("That's not valid...")

print("\nThanks for trying!")