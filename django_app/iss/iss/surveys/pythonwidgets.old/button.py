from widget import Widget


class Button(Widget):
    name = "button"
    requiredParametersNames = ["id", "text", "onclick"]
    optionalParameters = {}

    def __init__(self, listOfValues):
        self.listOfValues = listOfValues
