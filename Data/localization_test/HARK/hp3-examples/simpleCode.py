import random
import numpy
from harkpython import harkbasenode

class HarkNode(harkbasenode.HarkBaseNode):
    def __init__(self):
        self.outputNames = ("mult", "add", "matrix")
        self.outputTypes = ("prim_complex", "vector_float", "matrix_complex")

    def calculate(self):
        print(dir())
        print(self.nodeID, self.nodeName)
        self.outputValues["mult"] = 3 * self.source2 + 1j
        self.outputValues["add"] = numpy.append(self.source1, random.random())
        self.outputValues["matrix"] = numpy.array([[1, 2],[3,4],[5,6+2j]], numpy.complex)
        print(self.outputValues["matrix"])
