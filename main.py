import pytube
import os
import shutil
from time import sleep as delay
from getpass import getpass

def isFileExistent(fileToValidate) :
    if os.path.isfile(fileToValidate) :
        result = True
    else :
        result = False

    return result

def download_video(link) :
    os.system("cls")
    download_folder = os.path.expanduser("~") + r'\Downloads'
    yt = pytube.YouTube(link)
    ys = yt.streams.get_highest_resolution()
    destination = download_folder + r"\DownloadedVideo.mp4"
    current_file = yt.streams[0].title + ".mp4"

    print()
    print("Downloading...")

    if isFileExistent("DownloadedVideo.mp4") :
        os.remove("DownloadedVideo.mp4")
    ys.download()
    os.rename(current_file , "DownloadedVideo.mp4")
    shutil.move("DownloadedVideo.mp4" , download_folder)
    os.system("cls")

def main() :
    os.system("cls")
    link = input("Enter the link of YouTube video you want to download:\n  ")
    download_folder = os.path.expanduser("~") + r'\Downloads'
    destination = download_folder + r"\DownloadedVideo.mp4"

    if isFileExistent(destination) :
        os.system("cls")
        print("There is already a\nfile called 'DownloadedVideo.mp4'\nin your downloads folder.")
        print("Try removing that file and try again.")
        print()
        getpass("Press enter to dismiss: ")
        raise Exception

    try :
        download_video(link)
    except Exception :
        print("The link you have entered is\nnot a valid YouTube link.")
        getpass("Press enter to try again: ")
        main()

    if isFileExistent(destination):
        print()
        print("Download complete.")
        delay(.75)
        os.system("start " + destination)
        getpass("Press enter to dismiss: ")
        delay(.2)
        raise Exception


if __name__ == "__main__" :
    main()