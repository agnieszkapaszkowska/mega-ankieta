from iss.surveys.iterator import Iterator


class AbstractIteratorSubclass(Iterator):

    def generate_js(self):
        simple_js = self.generate_simple_js()

        return "function() {return " + simple_js + "}"

    def generate_simple_js(self):
        return ('iss.lib.iterators.' + self.get_class_name()
                + '(' + Iterator.generate_simple_js(self) + ')')
