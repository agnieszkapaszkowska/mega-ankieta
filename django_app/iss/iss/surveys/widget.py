import operator


class Widget:
    SINGLE = 'SINGLE'
    TUPLE = 'TUPLE'
    LIST = 'LIST'
    FORMATS = {
        SINGLE: 1,
        TUPLE: 2,
        LIST: 4
    }
    
    @classmethod
    def get_instance(self, parsingTree):
        return None

    def getJS():
        return ""

    def format_available(self, checked_format, available_formats):
        return (self.FORMATS[checked_format] & available_formats
                == self.FORMATS[checked_format])

    def check_formats(self):
        print self.create_available_formats([self.SINGLE, self.LIST])
    
    @classmethod
    def encode_formats(self, available_formats_list):
        return reduce(operator.or_, map(
                          lambda f:self.FORMATS[f], 
                          available_formats_list), 0)
