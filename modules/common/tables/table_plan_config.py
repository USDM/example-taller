class TablePlanConfig:

  data = {
    "free": {
      "ia_names": ["gemini"],
      "send_email": False,
      "analyze_apis": False,
      "max_messages": 2
    },
    "subscribed": {
      "ia_names": ["gemini", "claude"],
      "send_email": False,
      "analyze_apis": True,
      "max_messages": 5
    },
    "premium": {
      "ia_names": ["gemini"],
      "send_email": True,
      "analyze_apis": True,
      "max_messages": 10
    },
    "student": {
      "ia_names": ["gemini"],
      "send_email": True,
      "analyze_apis": True,
      "max_messages": 10
    }
  }

  def __new__(cls):
    if not hasattr(cls, 'instance'):
      cls.instance = super(TablePlanConfig, cls).__new__(cls)
    return cls.instance




