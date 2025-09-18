class TableResponseIa:

  data = {
    2: {
      "user_id": 2,
      "comments": [
        {
          "id": 1,
          "text": "Mensaje 1 creado para pruebas",
          "timestamp": "2024-01-01T10:00:00Z"
        },
        {
          "id": 2,
          "text": "Mensaje 2 creado para pruebas", 
          "timestamp": "2024-01-01T10:01:00Z"
        },
                {
          "id": 3,
          "text": "Mensaje 2 creado para pruebas", 
          "timestamp": "2024-01-01T10:01:00Z"
        },
                {
          "id": 4,
          "text": "Mensaje 2 creado para pruebas", 
          "timestamp": "2024-01-01T10:01:00Z"
        },
                {
          "id": 5,
          "text": "Mensaje 2 creado para pruebas", 
          "timestamp": "2024-01-01T10:01:00Z"
        },
                {
          "id": 6,
          "text": "Mensaje 2 creado para pruebas", 
          "timestamp": "2024-01-01T10:01:00Z"
        },
                {
          "id": 7,
          "text": "Mensaje 2 creado para pruebas", 
          "timestamp": "2024-01-01T10:01:00Z"
        },
                {
          "id": 8,
          "text": "Mensaje 2 creado para pruebas", 
          "timestamp": "2024-01-01T10:01:00Z"
        },
                {
          "id": 9,
          "text": "Mensaje 2 creado para pruebas", 
          "timestamp": "2024-01-01T10:01:00Z"
        }
      ]
    }
  }

  def __new__(cls):
    if not hasattr(cls, 'instance'):
      cls.instance = super(TableResponseIa, cls).__new__(cls)
    return cls.instance
