import settings
from grid import Grid
from actor import Actor
from loguru import logger

@logger.catch
if __name__=="__main__":
    settings.initialize()
    GAMEMAP = Grid()
    
    # Set up 4 actors on the game map at random locations
    for creature in range(4):
        x = Actor()
        GAMEMAP.place(x.startxlocation, x.startylocation, x)

    GAMEMAP.printcontents()
    #GAMEMAP.nicegrid()

