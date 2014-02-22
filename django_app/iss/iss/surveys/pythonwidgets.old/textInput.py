from widget import Widget


class TextInput(Widget):
    name = "text_input"
    requiredParametersNames = ["id", ]
    optionalParameters = {"text": "",
                          "placeholder": "",
                          "type": "text"}

    def __init__(self, listOfValues):
        self.listOfValues = listOfValues
