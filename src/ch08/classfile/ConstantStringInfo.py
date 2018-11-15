from ch08.classfile.ConstantInfo import ConstantInfo
from ch08.classfile.ConstantPool import ConstantPool

class ConstantStringInfo(ConstantInfo):
    def __init__(self, constantPool):
        self.cp = ConstantPool(constantPool)
        self.stringIndex = ""

    def readInfo(self, classReader):
        self.stringIndex = int.from_bytes(classReader.readUnit16(), byteorder="big")

    def String(self):
        return self.cp.getUtf8(self.stringIndex)