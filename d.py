from pytube import YouTube
from tqdm import tqdm

def download_video(video_url):
# Replace 'https://www.youtube.com/watch?v=VIDEO_ID' with the actual URL of the video


    yt = YouTube(video_url)

    # Get the stream with both video and audio (highest resolution available)
    video_stream = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
    # captions = yt.captions
    # print(captions)
    # # Print available captions languages
    # print("Available Captions:")
    # for caption in captions:
    #     print(caption.code, caption.name)

    # # Choose a language (e.g., 'en' for English)
    # language_code = 'en'

    # # Get the chosen caption track
    # chosen_caption = captions.get_by_language_code(language_code)

    # # Download the caption file
    # caption_file = chosen_caption.download(title=video_stream.title)
    file_size = video_stream.filesize
    
    # Download the video
    # Download the video with progress bar
    video_stream.download()

    print("Downloaded successfully.")
