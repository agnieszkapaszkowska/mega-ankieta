from widget import Widget


class CheckboxWidget(Widget):
    name = "checkbox"
    requiredParametersNames = [
        ("name", Widget.encode_formats([Widget.SINGLE])),
        ("id", Widget.encode_formats([Widget.SINGLE, Widget.LIST])),
        ("text", Widget.encode_formats([Widget.SINGLE, Widget.LIST]))
    ]
    optionalParameters = {
        ("checked", Widget.encode_formats([Widget.SINGLE, Widget.LIST])): "false", 
        ("orientation", Widget.encode_formats([Widget.SINGLE])): "vertical"
    }

    def __init__(self, listOfValues):
        self.listOfValues = listOfValues
