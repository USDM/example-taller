class TableSeriesMatch:

  data = {
    "UNRATE": {
      "id": 1,
      "name": "Unrat",
      "description": "Unrat",
      "url": "https://www.unrated.com",
      "frequency": "monthly"
    },
    "UNRATED": {
      "id": 2,
      "name": "Unrated",
      "description": "Unrated",
      "url": "https://www.unrated.com",
      "frequency": "monthly"
    },
    "APPL": {
      "id": 3,
      "name": "Apollo",
      "description": "Apollo",
      "url": "https://www.apollo.com",
      "frequency": "weekly"
    },
    "APOLLO": {
      "id": 4,
      "name": "Apollo",
      "description": "Apollo",
      "url": "https://www.apollo.com",
      "frequency": "weekly"
    },
  }
  def __new__(cls):
    if not hasattr(cls, 'instance'):
      cls.instance = super(TableSeriesMatch, cls).__new__(cls)
    return cls.instance


