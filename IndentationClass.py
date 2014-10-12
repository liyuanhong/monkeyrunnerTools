import string

class IndentationClass:
    def __init__(self):
        self.indent = []

    def appentBlank(self):
        self.indent.append('  ')

    def delBlank(self):
        self.indent = self.indent[:len(self.indent) - 1]

    def getBlank(self):
        __str = string.join(self.indent)        
        return __str
