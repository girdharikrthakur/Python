class Text(str):
    def duplicate(self):
        return self+self


class TrackableList(list):
    def append(self, object):
        print("Appned Call")
        super().append(object)


list = TrackableList()

list.append("1")
