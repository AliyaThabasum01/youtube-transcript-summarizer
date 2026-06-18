from transcript import extract_video_id, get_transcript
from summarizer import summarize


def main():

    print("=" * 50)
    print("🎥 YouTube Transcript Summarizer")
    print("=" * 50)

    url = input("\nEnter YouTube URL: ")

    try:

        video_id = extract_video_id(url)

        print("\nFetching transcript...")

        transcript = get_transcript(video_id)

        print("Generating summary...\n")

        summary = summarize(transcript)

        print(summary)

        with open("summary.md", "w", encoding="utf-8") as file:
            file.write(summary)

        print("\n✅ Summary saved as summary.md")

    except Exception as e:

        print("\nError:", e)


if __name__ == "__main__":
    main()
