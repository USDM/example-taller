class TableSeriesData:

  data = {
    1: [
      {
        "date": "2021-01-01",
        "value": 100
      },
      {
        "date": "2021-01-02",
        "value": 110
      },
      {
        "date": "2021-01-03",
        "value": 120
      },
      {
        "date": "2021-01-04",
        "value": 130
      },
      
      {
        "date": "2021-01-05",
        "value": 140
      },
      
      {
        "date": "2021-01-06",
        "value": 150
      },

      {
        "date": "2021-01-07",
        "value": 160
      },

      {
        "date": "2021-01-08",
        "value": 170
      },
      
      {
        "date": "2021-01-09",
        "value": 180
      },

      {
        "date": "2021-01-10",
        "value": 190
      },
      
      {
        "date": "2021-01-11",
        "value": 200
      },

      {
        "date": "2021-01-12",
        "value": 210
      },
      
      {
        "date": "2021-01-13",
        "value": 220
      },
      
      
      
    ],
  }

  def __new__(cls):
    if not hasattr(cls, 'instance'):
      cls.instance = super(TableSeriesData, cls).__new__(cls)
    return cls.instance


