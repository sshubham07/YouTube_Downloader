# Import the yt_dlp module
import yt_dlp

# Set the YouTube video URL to download

video_url = input("Please enter youtube url  ")

# Set the output file name and location
output_path = input("Please enter the output name for your file  ")
output_path +=".mp4"

# Create a new instance of the YoutubeDL class


# Set the output format to mp4 and the output location
ydl_opts = {
    'format': 'mp4',
    'outtmpl': output_path
}
ydl = yt_dlp.YoutubeDL(ydl_opts)

# Call the download method with the video URL and the download options
with ydl:
    info_dict = ydl.extract_info(video_url, download=False)
    thumbnail_url = info_dict['thumbnail']
    title = info_dict['title']
    date=info_dict['upload_date']
    views=info_dict['view_count']
    likes=info_dict['like_count']
    ydl.download([video_url])
print("Downloaded Successfully")
print("Title is ",title)
print("Thumbnail URL is ", thumbnail_url)
print("Video was uploaded on ",date)
print("This video has total number of likes = ",likes)
