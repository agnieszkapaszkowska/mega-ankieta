from widget import Widget


class PageWidget(Widget):
    name = "page"
    requiredParametersNames = ["id"]
    optionalParameters = {"back": "false",
                          "title": "",
                          "navigation_buttons": "true"}

    def __init__(self, listOfValues):
        self.listOfValues = listOfValues
