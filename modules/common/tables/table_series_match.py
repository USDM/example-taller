class TableSeriesMatch:

  data = {
    "UNRATE": {
      "name": "Unrat",
      "description": "Unrat",
      "url": "https://www.unrated.com",
      "frequency": "monthly"
    },
    "UNRATED": {
      "name": "Unrated",
      "description": "Unrated",
      "url": "https://www.unrated.com",
      "frequency": "monthly"
    },
    "APPL": {
      "name": "Apollo",
      "description": "Apollo",
      "url": "https://www.apollo.com",
      "frequency": "weekly"
    },
    "APOLLO": {
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


