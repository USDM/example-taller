class TableContent:

  data = {
    1: {
      "text": "Este es un contenido de prueba",
      "metadata": {
        "title": "Titulo del contenido",
        "authors": ["Autor del contenido"]
      },
      "comments": [
        {
          "comment": "Este aumento del deficit comercial podria indicar una debilidad en la economia estadounidense, especialmente si se mantiene en el futuro.",
          "reasoning": "Este es un comentario de prueba",
          "rating": "negative"
        },
        {
          "comment": "El incremento del deficit comercial probablemente impacte negativamente el crecimiento economico a largo plazo, al reducir la demanda agregada.",
          "reasoning": "Este es un comentario de prueba",
          "rating": "negative"
        },
        {        
          "comment": "La politica monetaria restrictiva de la Reserva Federal podria estar contribuyendo al aumento del deficit al fortalecer el dolar y encarecer las exportaciones.",
          "reasoning": "Este es un comentario de prueba",
          "rating": "negative"
        },
        {
          "comment": "Seria util examinar la composicion del deficit para determinar si se concentra en ciertos sectores, lo que puede indicar areas que necesitan mejoras en la produccion y competitividad.",
          "reasoning": "Este es un comentario de prueba",
          "rating": "neutral"
        }
      ],
      "summary": "Este es un resumen del contenido",
      "questions": [],
      "answers": [],
      "topics": [],
      "ia_name": "gemini",
      "critical_perspective": "Este es un contenido critico",
      "sources": []
    }
  }


  def __new__(cls):
    if not hasattr(cls, 'instance'):
      cls.instance = super(TableContent, cls).__new__(cls)
    return cls.instance