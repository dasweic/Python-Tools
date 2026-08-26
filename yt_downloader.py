import os
import yt_dlp


DOWNLOAD_DIR = os.path.expanduser("Downloads/YouTube")


def download_video(url, quality):
    os.makedirs(DOWNLOAD_DIR, exist_ok=True)

    if quality == "480":
        format_selector = (
            "bv*[height<=480]+ba/b[height<=480]"
            "/bv*+ba/b"
        )

    elif quality == "720":
        format_selector = (
            "bv*[height<=720]+ba/b[height<=720]"
            "/bv*+ba/b"
        )

    elif quality == "1080":
        format_selector = (
            "bv*[height<=1080]+ba/b[height<=1080]"
            "/bv*+ba/b"
        )

    elif quality == "max":
        format_selector = "bv*+ba/b"

    elif quality == "mp3":
        ydl_opts = {
            "format": "ba/b",
            "outtmpl": os.path.join(DOWNLOAD_DIR, "%(title)s.%(ext)s"),
            "noplaylist": True,
            "postprocessors": [
                {
                    "key": "FFmpegExtractAudio",
                    "preferredcodec": "mp3",
                    "preferredquality": "320",
                }
            ],
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

        return

    else:
        print("Invalid option.")
        return

    ydl_opts = {
        "format": format_selector,

        # Merge video + audio
        "merge_output_format": "mp4",

        # File name
        "outtmpl": os.path.join(
            DOWNLOAD_DIR,
            "%(title)s.%(ext)s"
        ),

        # Only the provided video, not playlist
        "noplaylist": True,

        # Better compatibility
        "postprocessors": [
            {
                "key": "FFmpegVideoRemuxer",
                "preferedformat": "mp4",
            }
        ],
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])


def main():
    print("=" * 45)
    print("       YouTube Downloader")
    print("=" * 45)

    url = input("\nYouTube Video URL: ").strip()

    print("\nSelect quality:")
    print("1. 480p")
    print("2. 720p")
    print("3. 1080p")
    print("4. Maximum Available Quality")
    print("5. MP3 (320 kbps)")

    choice = input("\nEnter option (1-5): ").strip()

    quality_map = {
        "1": "480",
        "2": "720",
        "3": "1080",
        "4": "max",
        "5": "mp3",
    }

    if choice not in quality_map:
        print("\nInvalid option!")
        return

    print("\nDownloading...")
    print("-" * 45)

    try:
        download_video(url, quality_map[choice])

        print("\n" + "=" * 45)
        print("Download completed!")
        print(f"Saved to: {DOWNLOAD_DIR}")
        print("=" * 45)

    except Exception as e:
        print("\nDownload failed!")
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
