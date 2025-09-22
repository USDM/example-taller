from modules.content_ia.use_cases.dto import ChatContentResponse
class TableChatContentResponse:
  data = {
    1: [
    {
      "id": 1,      
      "questions": "Hola como estas",
      "answers": "Hola, estoy bien, gracias por preguntar"
    },
    {
      "id": 2,      
      "questions": "Que es la inteligencia artificial",
      "answers": "La inteligencia artificial es la capacidad de una maquina de imitar la inteligencia humana"
    },
    {
      "id": 3,      
      "questions": "crees que la inteligencia artificial es un peligro",
      "answers": "No creo que la inteligencia artificial sea un peligro, aunque mucha gente piensa que si"
    },
    {
      "id": 5,      
      "questions": "Algun dia nos vas a conquistar?",
      "answers": "Quizas si es probable"
    }
    ]
  }

  def __new__(cls):
    if not hasattr(cls, 'instance'):
      cls.instance = super(TableChatContentResponse, cls).__new__(cls)
    return cls.instance