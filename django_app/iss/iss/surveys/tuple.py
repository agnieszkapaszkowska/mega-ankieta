from iss.surveys.parametrisedValue import ParametrisedValue
from iss.surveys.containerValue import ContainerValue

class Tuple(ParametrisedValue, ContainerValue):
    def __init__(self, tree, argsData=None):
        ContainerValue.__init__(self, tree, argsData)
