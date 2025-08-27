class TableUser:

  data = {
    1: {
      "user_type": "free",
      "user_email": "free@test.com"
    },
    2: {
      "user_type": "subscribed",
      "user_email": "test1@test.com"
    },
    3: {
      "user_type": "premium",
      "user_email": "test2@test.com"
    },
    4: {
      "user_type": "student",
      "user_email": "test3@test.com"
    }
  }

  def __new__(cls):
    if not hasattr(cls, 'instance'):
      cls.instance = super(TableUser, cls).__new__(cls)
    return cls.instance


