class TablePlanConfig:

  data = {
    "free": {
      "ia_names": ["gemini"],
      "send_email": False,
      "analyze_apis": False
    },
    "subscribed": {
      "ia_names": ["gemini", "claude"],
      "send_email": False,
      "analyze_apis": True
    },
    "premium": {
      "ia_names": ["gemini"],
      "send_email": True,
      "analyze_apis": True
    },
    "student": {
      "ia_names": ["gemini"],
      "send_email": True,
      "analyze_apis": True
    }
  }

  def __new__(cls):
    if not hasattr(cls, 'instance'):
      cls.instance = super(TablePlanConfig, cls).__new__(cls)
    return cls.instance




