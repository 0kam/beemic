from harkpython import harkbasenode

class GenConsts(harkbasenode.HarkBaseNode):
    def __init__(self):
        self.outputNames = list(map(lambda s: "c" + s,
                               ("int", "float", "complex", "source", 
                                "vecint", "vecfloat", "veccomplex", "vecsource",
                                "matint", "matfloat", "matcomplex", 
                                "mapvecint", "mapvecfloat", "mapveccomplex", 
                                "mapprimfloat", "string")))
        print(self.outputNames);
        self.outputTypes = ("prim_int", "prim_float", "prim_complex", "prim_source", 
                            "vector_int", "vector_float", "vector_complex", "vector_source",
                            "matrix_int", "matrix_float", "matrix_complex", 
                            "map_vector_int", "map_vector_float", "map_vector_complex", 
                            "map_prim_float", "prim_string")

    def calculate(self):
        self.outputValues["cint"] = 5
        self.outputValues["cfloat"] = 6.0
        self.outputValues["ccomplex"] = 7 + 8j
        self.outputValues["csource"] = {"id":1, "x":[0.5, 0.5, 0.5], "power":5.0}
        self.outputValues["cvecint"] = [1, 2, 3]
        self.outputValues["cvecfloat"] = [4.0, 5.0, 6.0]
        self.outputValues["cveccomplex"] = [7+8j, 9+10j, 11+12j]
        self.outputValues["cvecsource"] = [{"id":1, "x":[0.5, 0.5, 0.5], "power":5.0},
                                           {"id":2, "x":[0.2, 0.5, 0.5], "power":5.0}]
        self.outputValues["cmatint"] = [[1,2,3], [4,5,6]]
        self.outputValues["cmatfloat"] = [[7.0,8.0,9.0], [4,5,6]]
        self.outputValues["cmatcomplex"] = [[10+11j,12+13j,13+14j], [4,5,6]]

        self.outputValues["cmapvecint"] = {1: [1, 2, 3], 2:[4,5,6]}
        self.outputValues["cmapvecfloat"] = {1: [1.5, 2.5, 3.5], 2:[4,5,6]}
        self.outputValues["cmapveccomplex"] = {1: [1+7j, 2+8j, 3+9j], 2:[4,5,6]}

        self.outputValues["cmapprimfloat"] = {1: 0.5, 2: 2.4}

        self.outputValues["cstring"] = "/path/to/file"


class TestAllTypes(harkbasenode.HarkBaseNode):
    def __init__(self):        
        self.outputNames = list(map(lambda s: "x" + s,
                               ("int", "float", "complex", "source", 
                                "vecint", "vecfloat", "veccomplex", "vecsource",
                                "matint", "matfloat", "matcomplex", 
                                "mapvecint", "mapvecfloat", "mapveccomplex", 
                                "mapprimfloat", "string")))
        #"mapvecint", "mapvecfloat", "mapveccomplex")
        self.outputTypes = ("prim_int", "prim_float", "prim_complex", "prim_source", 
                            "vector_int", "vector_float", "vector_complex", "vector_source",
                            "matrix_int", "matrix_float", "matrix_complex", 
                            "map_vector_int", "map_vector_float", "map_vector_complex", 
                            "map_prim_float", "prim_string")


    def calculate(self):
        for ion, on in enumerate(self.outputNames):
            try:
                self.outputValues[on] = getattr(self, on[1:])
                print(type(self.outputValues[on]))
                print(self.outputValues[on])
            except:
                pass
