from concurrent.futures import process
import socket
import threading
import sys
import pickle

class Game():
    def __init__(self, id,players):
        self.initialize(id,players)
    def initialize(self,id,players):
        self.id = id
        self.players = players
    def __eq__(self, other):
        id = isinstance(other, self.__class__)
        if not id:
            return False
        if self.id == other.id:
            return True
        else:
            return False