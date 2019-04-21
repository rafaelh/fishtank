import settings
from loguru import logger

@logger.catch
class Grid():
    """ A collection of all the Locations on the game map. """
    def __init__(self):
        self.locations = []
        for xlocation in range(1, settings.X+1):
            for ylocation in range(1, settings.Y+1):
                self.locations.append(Location(xlocation, ylocation))

    def printcontents(self):
        """ Show the contents of a location """
        print("\nThe contents of the game map are as follows:\n")
        for location in self.locations:
            location.showdescription()

    def place(self, xlocation, ylocation, content):
        """ Put an object into a location """
        for location in self.locations:
            if location.xlocation == xlocation and location.ylocation == ylocation:
                location.contents.append(content)
                logger.debug("Placed: ", content, xlocation, ylocation)

@logger.catch
class Location:
    """ A space on the game map """
    def __init__(self, xlocation, ylocation):
        self.xlocation = xlocation
        self.ylocation = ylocation
        self.description = "This space has not yet been described."
        self.contents = []

    def showdescription(self):
        """ Show the contents of a location """
        print("Location %s, %s, contains: " % (self.xlocation, self.ylocation), end='')
        for content in self.contents:
            content.showdescription()
        print("")
