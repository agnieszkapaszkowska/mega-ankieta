from widget import Widget


class TextArea(Widget):
    name = "text_area"
    requiredParametersNames = ["id"]
    optionalParameters = {"text": "",
                          "placeholder": ""}

    def __init__(self, listOfValues):
        self.listOfValues = listOfValues
