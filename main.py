from direct.showbase.ShowBase import ShowBase

import Mapmanager


# ShowBase().run()

class Game(ShowBase):
    def __init__(self):
        super().__init__(self)
        land = Mapmanager.Mapmanager()


game = Game()
game.run()