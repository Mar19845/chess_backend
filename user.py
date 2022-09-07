from concurrent.futures import process
import socket
import threading
import sys
import pickle

class User():
    def __init__(self, id,_name,conn,addr):
        self.initialize(id,_name,conn,addr)
    def initialize(self,id,_name,conn,addr):
        self.id = id
        self.name = _name
        self.conn = conn
        self.addr = addr
    def __eq__(self, other):
        id = isinstance(other, self.__class__)
        if not id:
            return False
        if self.id == other.id:
            return True
        else:
            return False
    
