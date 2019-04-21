import settings
import random
from loguru import logger

@logger.catch
class Actor():
    """ A creature that acts """
    def __init__(self):
        self.type = "actortype"
        self.description = "actordescription"
        self.startxlocation = random.randint(1, settings.X)
        self.startylocation = random.randint(1, settings.Y)
        print("Created: ", end='')
        print(self, self.startxlocation, self.startylocation)

    def showdescription(self):
        print(self.description, end=' ')
