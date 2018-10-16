from abc import ABCMeta, abstractstaticmethod

class Entry(metaclass=ABCMeta):
    pathListSeparator = ";"

    @abstractstaticmethod
    def readClass(self,className):
        pass

    def newEntry(path):
        from ch03.classpath.CompositeEntry import CompositeEntry
        from ch03.classpath.WildcardEntry import WildcardEntry
        from ch03.classpath.ZipEntry import ZipEntry
        from ch03.classpath.DirEntry import DirEntry
        if Entry.pathListSeparator in path:
            return CompositeEntry(path)
        elif path.endswith("*"):
            return WildcardEntry(path)
        elif path.endswith(".jar") or path.endswith(".JAR") or path.endswith(".zip") or path.endswith(".ZIP"):
            return ZipEntry(path)
        else:
            return DirEntry(path)
