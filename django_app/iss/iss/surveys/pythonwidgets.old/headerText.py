from widget import Widget


class HeaderText(Widget):
    name = "text"
    requiredParametersNames = ["text"]
    optionalParameters = {}

    def __init__(self, listOfValues):
        self.listOfValues = listOfValues
