from iss.surveys.value import Value


class StructElem(Value):

    def generate_js(self):
        return 'function() { return ' + self.generate_simple_js() + ' }'

    def generate_simple_js(self):
        return 'iss.vars.' + Value.generate_simple_js(self)
