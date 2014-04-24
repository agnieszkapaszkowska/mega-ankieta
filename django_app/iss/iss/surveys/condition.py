from iss.surveys.value import Value


class Condition(Value):

    def generate_js(self):
        return 'function() { with (iss.vars) { return (' + self.generate_simple_js() + ') }}'

