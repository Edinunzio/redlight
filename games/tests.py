from django.core.urlresolvers import resolve
from django.test import TestCase
from django.http import HttpRequest

from views import home_page, player_move, player_stop
from models import Player, Game


class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_home_page_renders_correct_template(self):
        post_request = HttpRequest()
        get_request = HttpRequest()
        post_request.method = 'POST'
        get_request.method = 'GET'
        post_request.POST['winner'] = 'Player 2'
        response_1 = self.client.post('/', {'winner': 'Player 2'})
        response_2 = self.client.get('/')
        self.assertIn('Wins', response_1.content)
        self.assertNotIn('Wins', response_2.content)
        self.assertTemplateUsed(response_1, 'winner.html')
        self.assertTemplateUsed(response_2, 'base.html')


class GameScreenTest(TestCase):

    def test_url_resolves_to_game_page(self):
        response = self.client.get('/game/new/')
        self.assertTemplateUsed(response, 'game.html')

    def test_player_move(self):
        g = Game()
        g.register_player()
        p = g.player_1
        p2 = g.player_2
        self.assertEquals(0, p.location)
        p.move()
        self.assertEquals(1, p.location)
        self.assertEquals(True, p.in_motion)
        p.move()
        p.move()
        self.assertEquals(3, p.location)
        self.assertEquals(0, p2.location)


class PlayerModelTest(TestCase):

    def test_create_players(self):
        player_1 = Player('Player 1')
        player_2 = Player('Player 2')
        self.assertEqual('Player 1', player_1.name)
        self.assertEqual('Player 2', player_2.name)
        self.assertEqual(None, player_1.game_id)
        self.assertEqual(None, player_2.game_id)
        self.assertEqual(0, player_1.location)
        self.assertEqual(0, player_2.location)
        self.assertEqual(False, player_1.in_motion)
        self.assertEqual(False, player_2.in_motion)

    def test_joining_game(self):
        player_2 = Player('Player 2')
        self.assertEqual(player_2.join_game('123-456'), player_2.game_id)
        player_3 = Player('Player 3')
        self.assertEqual(player_3.join_game('asdfg'), player_3.game_id)

    def test_move_player(self):
        player_1 = Player('Player 1')
        player_1.move()
        self.assertEqual(1, player_1.location)
        self.assertEqual(True, player_1.in_motion)
        player_1.pause()
        self.assertEqual(False, player_1.in_motion)

    def test_going_thru_red_light(self):
        player_1 = Player('Player 1')
        player_1.location = 3
        player_1.in_motion = True
        self.assertTrue(player_1.in_motion)


class GameModelTest(TestCase):

    def test_create_new_game(self):
        game = Game()
        self.assertIsNotNone(game.id)
        self.assertIsNotNone(game.player_1)
        self.assertIsNone(game.light_color)
        self.assertEqual('open', game.status)
        self.assertEqual('Player 1', game.player_1.name)
        self.assertEqual(0, game.player_1.location)
        self.assertEqual(False, game.player_1.in_motion)

    def test_registering_second_player(self):
        game = Game()
        game.register_player()
        self.assertEqual('Player 1', game.player_1.name)
        self.assertEqual('Player 2', game.player_2.name)
        self.assertEqual(0, game.player_1.location)
        self.assertEqual(False, game.player_1.in_motion)
        self.assertEqual(0, game.player_2.location)
        self.assertEqual(False, game.player_2.in_motion)
        self.assertEqual('locked', game.status)

    def test_game_status_updates_on_game_end(self):
        game = Game()
        game.register_player()
        game.end_game()
        self.assertEqual('complete', game.status)

    def test_update_status(self):
        game = Game()
        game.register_player()
        json_string = '{"id": "asc123hjk", "distance": 20, "light_color": "green", "player_1": {"name": "Player 1", "location": 4, "in_motion": "true"}, "player_2": {"name": "Player 2", "location": 6, "in_motion": "true"}}'

        self.assertEqual(0, game.player_1.location)
        self.assertEqual(0, game.player_2.location)
        self.assertIsNone(game.light_color)
        self.assertEqual(20, game.distance)
        self.assertFalse(game.player_1.in_motion)
        self.assertFalse(game.player_2.in_motion)

        game.update_status(json_string)

        self.assertEqual(4, game.player_1.location)
        self.assertEqual(6, game.player_2.location)
        self.assertEqual('green', game.light_color)
        self.assertEqual(20, game.distance)
        self.assertTrue(game.player_1.in_motion)
        self.assertTrue(game.player_2.in_motion)

    def test_change_green_to_red(self):
        player_1 = Player('Player 1')
        game = Game(player_1)
        game.register_player()
        game.change_light('red')
        self.assertEqual('red', game.light_color)

    def test_change_red_to_green(self):
        player_1 = Player('Player 1')
        game = Game(player_1)
        game.register_player()
        game.change_light('green')
        self.assertEqual('green', game.light_color)
