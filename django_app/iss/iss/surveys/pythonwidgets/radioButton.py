from widget import Widget


class RadioButton(Widget):
    name = "radio"
    requiredParametersNames = ["id", "name", "text"]
    optionalParameters = {"checkedIndex": -1,
                          "orientation": "vertical"}

    def __init__(self, listOfValues):
        self.listOfValues = listOfValues
