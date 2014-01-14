from widget import Widget


class TextinputWidget(Widget):
    name = "textinput"
    requiredParametersNames = [("id", Widget.encode_formats([Widget.SINGLE]))]
    optionalParameters = {
        ("text", Widget.encode_formats([Widget.SINGLE])): "",
        ("placeholder", Widget.encode_formats([Widget.SINGLE])): "",
        ("type", Widget.encode_formats([Widget.SINGLE])): "text"
    }

    def __init__(self, listOfValues):
        self.listOfValues = listOfValues
