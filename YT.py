import pytube
def ActivisteDownload(url, output_path):
    try:
        video = pytube.YouTube(url)
        stream = video.streams.get_highest_resolution()
        stream.download(output_path)
        print("DOWNLOAD OK")
    except Exception as e:
        print("ERROR :", str(e))
if __name__ == "__main__":
    URL = input("URL >> ")
    FOLDEROUTPUT = input("PATH >> ")
    ActivisteDownload(URL, FOLDEROUTPUT)
