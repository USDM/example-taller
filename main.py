from content_service import ContentService


def main():
    video_url = "https://www.youtube.com/watch?v=aa_GIiivHTw"
    content_service = ContentService()
    content_service.process_content_video(video_url)

    
if __name__ == "__main__":
    main()