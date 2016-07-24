from __future__ import unicode_literals
from time import sleep
from django.db import models
from uuid import uuid4
from random import uniform
import json


class Player(object):

    def __init__(self, name='Player 1'):
        self.name = name
        self.game_id = None
        self.location = 0
        self.in_motion = False

    def join_game(self, game_id):
        self.game_id = game_id
        return self.game_id

    def move(self):
        self.in_motion = True
        self.location += 1
        sleep(.5)
        self.in_motion = False

    def winner(self, player):
        pass


class Game(object):

    def __init__(self, first_player, distance=20):
        self.id = str(uuid4())
        self.player_1 = first_player
        self.distance = distance
        self.light_color = None
        self.status = 'open'

    def register_player(self, player):
        self.player_2 = player
        player.join_game(self.id)
        self.status = 'locked'

    def end_game(self):
        self.status = 'complete'

    def update_status(self, json_data):
        """
        json_data = '{
            "id": "asc123hjk",
            "distance": 20,
            "light_color": "green",
            "player_1": {"name": "Player 1", "location": 4, "in_motion": "true"},
            "player_2": {"name": "Player 2", "location": 6, "in_motion": "true"}
        }'
        """
        data_dict = json.loads(json_data)
        self.player_1.location = data_dict['player_1']['location']
        self.player_2.location = data_dict['player_2']['location']
        self.player_1.in_motion = data_dict['player_1']['in_motion']
        self.player_2.in_motion = data_dict['player_2']['in_motion']

        self.distance = data_dict['distance']
        self.light_color = data_dict['light_color']
