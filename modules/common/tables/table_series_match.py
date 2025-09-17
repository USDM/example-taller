class TableSeriesMatch:

  data = {
    "UNRATE": {
      "id": 1,
      "name": "Unrat",
      "description": "Unrat",
      "url": "https://www.unrated.com",
      "frequency": "monthly",
      "importance": 1
    },
    "UNRATED": {
      "id": 2,
      "name": "Unrated",
      "description": "Unrated",
      "url": "https://www.unrated.com",
      "frequency": "monthly",
      "importance": 3
    },
    "APPL": {
      "id": 3,
      "name": "Apollo",
      "description": "Apollo",
      "url": "https://www.apollo.com",
      "frequency": "weekly",
      "importance": 2
    },
    "APOLLO": {
      "id": 4,
      "name": "Apollo",
      "description": "Apollo",
      "url": "https://www.apollo.com",
      "frequency": "weekly",
      "importance": 1
    },
  }
  def __new__(cls):
    if not hasattr(cls, 'instance'):
      cls.instance = super(TableSeriesMatch, cls).__new__(cls)
    return cls.instance


