from iss.surveys.value import Value


class InnerString(Value):

    def generate_plain_js(self):
        return '"' + Value.generate_simple_js() + '"'
