from widget import Widget


class Checkbox(Widget):
    name = "checkbox"
    requiredParametersNames = ["name", "id",
                               "text"]
    optionalParameters = {"checked": "false",
                          "orientation": "vertical"}

    def __init__(self, listOfValues):
        self.listOfValues = listOfValues
