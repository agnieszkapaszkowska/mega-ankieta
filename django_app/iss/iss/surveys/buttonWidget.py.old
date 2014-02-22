from widget import Widget


class ButtonWidget(Widget):
    name = "button"
    requiredParametersNames = [
        ("id", Widget.encode_formats([Widget.SINGLE, Widget.LIST])),
        ("text", Widget.encode_formats([Widget.SINGLE, Widget.LIST])),
        ("onclick", Widget.encode_formats([Widget.SINGLE]))
    ]
    optionalParameters = {}

    def __init__(self, listOfValues):
        self.listOfValues = listOfValues
