from yt_dlp import YoutubeDL
#pip install yt-dlp
def youtube_search(query):
    """
    Returns the first YouTube video URL for the given search query.
    """
    ydl_opts = {
        "quiet": True,
        "extract_flat": True,
    }

    with YoutubeDL(ydl_opts) as ydl:
        result = ydl.extract_info(f"ytsearch1:{query}", download=False)

    if result["entries"]:
        video = result["entries"][0]
        return f"https://www.youtube.com/watch?v={video['id']}"

    return None


# Example
link = youtube_search("Python tutorial")
print(link)
