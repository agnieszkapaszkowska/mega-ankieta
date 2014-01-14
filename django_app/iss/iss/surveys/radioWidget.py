from widget import Widget


class RadioWidget(Widget):
    name = "radio"
    requiredParametersNames = [
        ("name", Widget.encode_formats([Widget.SINGLE])),
        ("id", Widget.encode_formats([Widget.SINGLE, Widget.LIST])),
        ("text", Widget.encode_formats([Widget.SINGLE, Widget.LIST]))
    ]
    optionalParameters = {
        ("checkedIndex", Widget.encode_formats([Widget.SINGLE])): -1, 
        ("orientation", Widget.encode_formats([Widget.SINGLE])): "vertical"
    }

    def __init__(self, listOfValues):
        self.listOfValues = listOfValues
