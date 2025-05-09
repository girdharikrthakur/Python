class InvalidOperationError(Exception):
    pass


class Stream:

    def __init__(self):
        self.opened = False

    def Open(self):

        if self.opened:
            raise InvalidOperationError("Stream is Already Opened")
        self.opened = True

    def Close(self):
        if not self.opened:
            raise InvalidOperationError("Stream is Already CLosed")
        self.opened = False


class FileStream(Stream):
    def read(self):
        print('Reading Data from A File')


class NetworkStream(Stream):

    def read(self):
        print("Reading Data from The Network")


stream = Stream()
stream = open()
