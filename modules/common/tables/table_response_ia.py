class TableResponseIa:

  data = [
    {
      "message": "Hola, que tal?",
      "response": "Estoy bien, gracias por preguntar"
    },
    {
      "message": "Que es lo que te envie?",
      "response": "Me enviaste un contenido de test"
    },
    {
      "message": "Que piensas del contenido?",
      "response": "El contenido es de test, no cuenta con mucha informacion"
    },
    {
      "message": "Y por que no tiene datos?",
      "response": "Porque es un contenido de test"
    }
  ]

  def __new__(cls):
    if not hasattr(cls, 'instance'):
      cls.instance = super(TableResponseIa, cls).__new__(cls)
    return cls.instance
