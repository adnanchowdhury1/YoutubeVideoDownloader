from pytube import YouTube

link = input("Enter a youtube link: ")
yt = YouTube(link)

#Title of video
print("Title: ",yt.title)
#Number of views
print("Number of views: ",yt.views)
#Length of video
print("Length of video: ",yt.length,"seconds")
#Rating
print("Ratings: ",yt.rating)

ys = yt.streams.get_highest_resolution()

#Replace <<PATH>> with a valid location where video will be downloaded
location_to_download = "<<PATH>>"

print("Downloading...")
ys.download(location_to_download)
print("Download Complete")
