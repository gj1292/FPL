__author__ = 'gj'

from urls import *
from helpers import *


class Team(object):
    def __init__(self, name):
        self.name = name

    def get_win_percent(self, table_data):


