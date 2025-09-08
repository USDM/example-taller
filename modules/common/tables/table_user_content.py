class TableUserContent:

  data = {
    1:[
        {
        "text": "Test",
        "metadata": {
            "title": "Test",
            "description": "Test",
        },
        "comments": ["Este comentario es de test", "Este comentario es de test 2", "Este comentario es de test 3"],
        "summary": "Test",
        "questions": [],
        "answers": [],
        "topics": [],
        "ia_name": "Test",
        "critical_perspective": "Test",
        "sources": []
        },
        {
        "text": "Test 2",
        "metadata": {
            "title": "Test 2",
            "description": "Test2 ",
        },
        "comments": ["Este comentario es de test 2222", "Este comentario es de test 22222", "Este comentario es de test 32222"],
        "summary": "Test 2",
        "questions": [],
        "answers": [],
        "topics": [],
        "ia_name": "Test 2",
        "critical_perspective": "Test 2",
        "sources": []
        }
      ]
    }

  def __new__(cls):
    if not hasattr(cls, 'instance'):
      cls.instance = super(TableUserContent, cls).__new__(cls)
    return cls.instance