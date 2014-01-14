from widget import Widget


class TextWidget(Widget):
    name = "text"
    requiredParametersNames = [("text", Widget.encode_formats([Widget.SINGLE]))]
    optionalParameters = {}

    def __init__(self, listOfValues):
        self.listOfValues = listOfValues
