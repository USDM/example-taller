class TableContent:

  data = {
    1: {
      "text": "Test",
      "metadata": {
        "title": "Test",
        "description": "Test",
      },
      "comments": ["Este comentario es de test", "Este comentario es de test 2", "Este comentario es de test 3",
       "Este comentario es de test 4",  "Este comentario es de test 5",  "Este comentario es de test 6",  "Este comentario es de test 7",
        "Este comentario es de test 8", "Este comentario es de test 9", "Este comentario es de test 10"
      ],
      "summary": "Test",
      "questions": [],
      "answers": [],
      "topics": [],
      "ia_name": "Test",
      "critical_perspective": "Test",
      "sources": []
    }
  }

  def __new__(cls):
    if not hasattr(cls, 'instance'):
      cls.instance = super(TableContent, cls).__new__(cls)
    return cls.instance