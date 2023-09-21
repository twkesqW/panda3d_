import json

from direct.showbase.ShowBase import ShowBase
from panda3d.core import CollisionBox, CollisionNode


class Mapmanager():
    def __init__(self):
        self.model = 'mymodel/untitled.gltf'  # модель куба у файлі block.egg
        self.texture = 'block.png'  # текстура куба
        self.color = (150/255, 32/255, 10/255, 1)  # rgba
        self.startNew()
        self.addBlock((0, 10, 0))
        self.addBlock((0, 9, 0))
        self.addBlock((1, 10, 0))

    def addBlock(self, position):
        self.block = loader.loadModel(self.model)
        self.block.setPos(position)
        self.block.reparentTo(self.land)

        blockSolid = CollisionBox((-1, -1, -1), (1, 1, 1))

        blockNode = CollisionNode('block-collision-node')
        blockNode.addSolid(blockSolid)
        collider = self.block.attachNewNode(blockNode)

        collider.setPythonTag('owner', self.block)

    def startNew(self):
        self.land = render.attachNewNode("Land")


    def makeMap(self):
        with open("map.json","r") as file:
            data = json.load(file)
            for elem in data:
                if elem["name"] == "block":
                    self.addBlock(tuple(elem["pos"]))
