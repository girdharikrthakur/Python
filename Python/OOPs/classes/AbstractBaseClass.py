from abc import ABC, abstractmethod


class InvalidOperationError(Exception):
    pass


class Stream(ABC):

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

    @abstractmethod
    def Read(self):
        pass


class FileStream(Stream):

    def read(self):
        print('Reading Data from A File')


class FileStream(Stream):
    def read(self):  # incorrect method name (case mismatch)
        print("Reading data from file")


stream = FileStream()

stream.open()
