from widget import Widget


class TextareaWidget(Widget):
    name = "textarea"
    requiredParametersNames = [("id", Widget.encode_formats([Widget.SINGLE]))]
    optionalParameters = {
        ("text", Widget.encode_formats([Widget.SINGLE])): "",
        ("placeholder", Widget.encode_formats([Widget.SINGLE])): ""
    }

    def __init__(self, listOfValues):
        self.listOfValues = listOfValues
