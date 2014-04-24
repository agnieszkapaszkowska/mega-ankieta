from iss.surveys.value import Value


class String(Value):

    def get_python_value(self):
        return self.generate_simple_js()[1:-1]
