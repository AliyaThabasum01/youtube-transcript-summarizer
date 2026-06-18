# 🎥 YouTube Transcript Summarizer

A Python application that extracts YouTube transcripts and summarizes them using Google's Gemini AI.

## Features

- Extract transcript from YouTube videos
- AI-powered summary
- Key points
- Action items
- Saves output as Markdown

## Installation

```bash
pip install -r requirements.txt
```

## Add API Key

Create a `.env` file:

```env
GEMINI_API_KEY=YOUR_API_KEY
```

## Run

```bash
python app.py
```

## Example

```
Enter YouTube URL:
https://youtu.be/xxxxxxxx

Fetching transcript...
Generating summary...

Summary...

Key Points...

Action Items...
```
