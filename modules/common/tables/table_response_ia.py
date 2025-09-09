class TableResponseIa:

  data = []

  def __new__(cls):
    if not hasattr(cls, 'instance'):
      cls.instance = super(TableResponseIa, cls).__new__(cls)
    return cls.instance
