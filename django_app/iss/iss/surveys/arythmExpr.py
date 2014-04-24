from iss.surveys.value import Value


class ArythmExpr(Value):

    def generate_js(self):
        return ('function() { with (iss.vars) { return ('
                + self.generate_simple_js() + ') }}')
