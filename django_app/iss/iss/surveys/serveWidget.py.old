from widget import Widget


class ServeWidget(Widget):
    name = "serve"
    requiredParametersNames = []
    optionalParameters = {
        ("back", Widget.encode_formats([Widget.SINGLE])): "false",
        ("title", Widget.encode_formats([Widget.SINGLE])): ""
    }

    def __init__(self, listOfValues):
        self.listOfValues = listOfValues
