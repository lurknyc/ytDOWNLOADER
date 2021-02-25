from pytube import YouTube

#ask for the link from user
link = input("Enter the link of YouTube video you want to download:  ")
yt = YouTube(link)

#Showing details
print("Title: ",yt.title)
print("Number of views: ",yt.views)
print("Length of video: ",yt.length)
print("Rating of video: ",yt.rating)
ys = yt.streams.get_highest_resolution()

download_prompt = input("Would you like to download the video? (1 is YES, 2 is NO)")

if download_prompt == 1 :

    ys.download()
    #Starting download
    print("Downloading...")
    print("Download completed!!")


elif download_prompt == 2 :

    print("Restart the Program to Try Again!")
    exit()

#Getting the highest resolution possible


