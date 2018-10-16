from ch03.classfile.AttributeInfo import AttributeInfo

class UnparsedAttribute(AttributeInfo):
    def __init__(self, attrName, attrLen):
        self.name = attrName
        self.length = attrLen
        self.info = ""

    def readInfo(self, classReader):
        self.info = classReader.readBytes(self.length)
