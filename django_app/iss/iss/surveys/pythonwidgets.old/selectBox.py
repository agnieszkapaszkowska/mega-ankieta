from widget import Widget


class SelectBox(Widget):
    name = "select"
    requiredParametersNames = ["id", "options"]
    optionalParameters = {"selectedIndex": 0}

    def __init__(self, listOfValues):
        self.listOfValues = listOfValues
