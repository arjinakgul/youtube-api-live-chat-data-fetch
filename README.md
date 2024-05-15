# YouTube Live Chat Scraper

This Python script scrapes live chat messages from a YouTube video using the `pytchat` library and saves the chat data to a CSV file.

## Prerequisites

Before running the script, ensure you have the following:

- Python 3.x
- The `pytchat` library installed

You can install the `pytchat` library using pip:

```bash
pip install pytchat
```

## Usage

### 1. Set the YouTube Video ID

Replace "youtube video id" with the actual YouTube video ID from which you want to scrape live chat messages.

```bash
videoid = "your_youtube_video_id"
```

### 2. Set the Output File Name

The chat messages will be saved in a CSV file. You can specify the desired file name:

```bash
file_name = "chat.csv"
```

### 3. Run the Script

Execute the script to start scraping live chat messages and saving them to the specified CSV file.

```bash
python youtube-api-live-chat.py
```

## Notes

- Ensure that the YouTube video ID is correct and that the live chat is active for the script to function properly.
- The script will continue running as long as the live chat is active. To stop the script, you can manually terminate it.
