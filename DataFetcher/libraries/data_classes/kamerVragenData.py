class KamerVragenData:
  """
  klasse die de data van de kamer vragen bijhoudt
  """
  id: str
  gewijzigdOp: str
  verwijderd: bool
  datum:str
  soort:str
  
  def __init__(self, id: str, gewijzigdOp: str, verwijderd: bool, datum:str, soort:str):
    """
    Initialisatie van de klasse
    
    :param id: id van de kamer vraag
    :param gewijzigdOp: wanneer de vraag is gewijzigd
    :param verwijderd: of de vraag is verwijderd
    :param datum: de datum van de vraag
    :param soort: het soort vraag
    """
    self.id = id
    self.gewijzigdOp = gewijzigdOp
    self.verwijderd = verwijderd
    self.datum = datum
    self.soort = soort
    
  def convertToDict(self):
    """
    Converteert de data naar een dictionary
    """
    return {
      'id': self.id,
      'GewijzigdOp': self.gewijzigdOp,
      'Verwijderd': self.verwijderd,
      'Datum': self.datum
    }
  
  def convertFromDict(self, data):
    """
    Converteert de data van een dictionary naar de klasse
    """
    self.id = data['id']
    self.gewijzigdOp = data['GewijzigdOp']
    self.verwijderd = data['Verwijderd']
    self.datum = data['Datum']