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

    def pause(self):
        self.in_motion = False


class Game(object):

    def __init__(self, distance=20):
        self.id = str(uuid4())
        self.player_1 = Player()
        self.distance = distance
        self.light_color = None
        self.status = 'open'
        self.winner = None

    def change_light(self, color):
        self.light_color = 'green'
        if color != 'green':
            duration = '{0:.2f}'.format(uniform(0.25, 15))
            sleep(float(duration))
            self.light_color = color

    def register_player(self):
        self.player_2 = Player('Player 2')
        self.player_2.join_game(self.id)
        self.status = 'locked'

    def end_game(self):
        self.status = 'complete'

    def begin_game(self):
        """

        :return:
        """
        if self.player_1 and self.player_2:
            self.game_loop()

    def game_loop(self):
        while self.status is not 'complete':
            self.change_light('red')
            data = self.get_status()
            self.update_status(data)
            self.update_screen(data) #  TODO: write jsonresponse to update front end

    def update_status(self, json_data):
        data_dict = json.loads(json_data)
        self.player_1.location = data_dict['player_1']['location']
        self.player_2.location = data_dict['player_2']['location']
        self.player_1.in_motion = data_dict['player_1']['in_motion']
        self.player_2.in_motion = data_dict['player_2']['in_motion']

        self.distance = data_dict['distance']
        self.light_color = data_dict['light_color']
