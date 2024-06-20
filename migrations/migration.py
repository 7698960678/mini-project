from abc import ABCMeta, abstractmethod


class Migration:
    __metaclass__ = ABCMeta

    my_cursor = None
    conn = None

    def __init__(self, cursor, connection):
        self.my_cursor = cursor
        self.conn = connection

    @abstractmethod
    def update(self):
        pass
