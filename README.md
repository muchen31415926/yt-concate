# yt-concate-cli

A command-line tool that creates a single concatenated video
from clips mentioning a specific keyword within a YouTube channel.

## Features

- Download captions from a channel
- Search captions by keyword
- Download matched videos
- Combine multiple videos into one
- Built-in logging with configurable levels
- Flexible command-line options

## Requirements

### Python packages

- Python 3.12+
- yt-dlp
- moviepy
- python-dotenv (for loading the YouTube API key)

### System dependency

- FFmpeg (required for video processing)

### API Key

A YouTube Data API key is required.

Create a `.env` file in the project root directory and add:
```env
API_KEY=your_api_key_here
```


## Installation

```bash
pip install yt-concate-cli
```