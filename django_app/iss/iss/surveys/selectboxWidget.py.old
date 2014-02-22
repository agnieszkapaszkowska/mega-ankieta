from widget import Widget


class SelectboxWidget(Widget):
    name = "selectbox"
    requiredParametersNames = [
        ("id", Widget.encode_formats([Widget.SINGLE])),
        ("options", Widget.encode_formats([Widget.LIST]))
    ]
    optionalParameters = {
        ("selectedIndex", Widget.encode_formats([Widget.SINGLE])): 0
    }

    def __init__(self, listOfValues):
        self.listOfValues = listOfValues
