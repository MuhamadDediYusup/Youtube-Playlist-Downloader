# YouTube Playlist Downloader

This script allows you to download all videos from a YouTube playlist in your chosen format: **MP4 (video)**, **MP3 (audio)**, or the original format of the video.

## Features
- Download entire playlists from YouTube.
- Choose the output format:
  - **MP4**: Video format with the highest available resolution.
  - **MP3**: Audio-only format, converted to MP3 at 192kbps.
  - **Original Format**: Downloads the video/audio in its original format.
- Automatically creates an output folder if it does not exist.

## Requirements
- Python 3.6 or later.
- `yt-dlp` library (a modern alternative to `youtube-dl`).
- FFmpeg (required for MP3 conversion).

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/your-repo-name.git
   cd your-repo-name
   ```

2. Install the required Python library:
   ```bash
   pip install yt-dlp
   ```

3. Install FFmpeg:
   - **Windows**: Download FFmpeg from [FFmpeg.org](https://ffmpeg.org/download.html) and add it to your system PATH.
   - **Linux**: Install via your package manager (e.g., `sudo apt install ffmpeg`).
   - **Mac**: Install using Homebrew (`brew install ffmpeg`).

## Usage

1. Run the script:
   ```bash
   python main.py
   ```

2. Enter the URL of the YouTube playlist when prompted.

3. Enter the output folder (default is `./downloads`).

4. Choose the format:
   - `1` for MP4 (video)
   - `2` for MP3 (audio only)
   - `3` for Original format

5. The script will download all videos in the playlist to the specified folder.

## Example

```
Enter the YouTube playlist URL: https://www.youtube.com/playlist?list=PL12345...
Enter the output folder (default: ./downloads): my_videos
Choose format:
1. MP4 (video)
2. MP3 (audio only)
3. Original format
Enter your choice (1/2/3): 1
Downloading playlist: https://www.youtube.com/playlist?list=PL12345...
All videos downloaded successfully.
```

## Notes
- Ensure the playlist URL is correct and publicly accessible.
- Some videos may not be downloadable due to copyright or regional restrictions.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

---
Feel free to contribute or suggest improvements by submitting issues or pull requests!

