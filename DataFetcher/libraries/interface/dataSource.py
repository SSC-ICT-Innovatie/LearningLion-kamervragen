from abc import ABC, abstractmethod

class dataSource(ABC):

    """
    Haalt data op van een bepaalde bron
    """
    @abstractmethod
    def fetchAllData(self):
        """
        Haalt alle data op van de bron
        """
        pass

    @abstractmethod
    def fetchFile(self, fileId):
        """
        Haalt een bestand op van de bron
        
        :param fileId: id van het bestand
        """
        pass
      
