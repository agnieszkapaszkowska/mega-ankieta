from widget import Widget


class PageWidget(Widget):
    name = "page"
    requiredParametersNames = [("id", Widget.encode_formats([Widget.SINGLE]))]
    optionalParameters = {
        ("back", Widget.encode_formats([Widget.SINGLE])): "false",
        ("title", Widget.encode_formats([Widget.SINGLE])): "",
        ("navigation_buttons", Widget.encode_formats([Widget.SINGLE])): "true"
    }

    def __init__(self, listOfValues):
        self.listOfValues = listOfValues
