from content_service import ContentService
from dto import SubcontentType

def main():
    video_url = "https://www.youtube.com/watch?v=aa_GIiivHTw"
    content_service = ContentService()
    content_service.process_content_video(video_url)

    #content_service.generate_summary(1)
    #content_service.generate_questions(1)

    #content_service.generate_video_subcontent(1, SubcontentType.SUMMARY)
    

    
if __name__ == "__main__":
    main()