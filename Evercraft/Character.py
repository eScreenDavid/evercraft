
class Character:
  def __init__(self):
        self.name = None
        self.alignment = None

  def getName(self):
        return self.name

  def setName(self, value):
      self.name = value

  def getAlignment(self):
      return self.alignment

  def setAlignment(self, value):
      if value not in ['Neutral', 'Good', 'Evil']:
            raise ValueError('Alignment not found.')
      self.alignment = value