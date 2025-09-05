class TableContent:

    data = {
        1: {
            "text": "Content 1",
            "metadata": {
                "title": "Content 1",
                "authors": ["Author 1", "Author 2", "Author 3"]
            },
            "comments": [
                {
                    "text": "Comment 1",
                    "rating": "positive",
                    "reasoning": "Reasoning 1"
                },
                {
                    "text": "Comment 2",
                    "rating": "positive",
                    "reasoning": "Reasoning 2"
                },
                {
                    "text": "Comment 3",
                    "rating": "positive",
                    "reasoning": "Reasoning 3"
                }
            ],
            "summary": "Summary 1",
            "questions": [
                "Question 1",
                "Question 2",
                "Question 3"
            ],
            "answers": [
                "Answer 1",
                "Answer 2",
                "Answer 3"
            ],
            "topics": [
                "Topic 1",
                "Topic 2",
                "Topic 3"
            ],
            "ia_name": "IA 1",
            "critical_perspective": "Critical Perspective 1",
            "sources": ["Source 1", "Source 2", "Source 3"]
        }
    }

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(TableContent, cls).__new__(cls)
        return cls.instance