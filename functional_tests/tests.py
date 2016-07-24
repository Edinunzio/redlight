from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class FirstPlayerTest(StaticLiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_creates_a_new_game(self):
        # Player one goes to site
        self.browser.get(self.live_server_url)

        # Player sees name of game in page title
        self.assertIn('Red', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('Green', header_text)

        # Player sees button to start a new game
        new_game_link = self.browser.find_element_by_id('id_new_game')
        self.assertEqual(new_game_link.text, 'Create New Game')

        # Player clicks new game link to start a new game
        new_game_link.click()
        self.assertEqual(self.browser.current_url, 'http://localhost:8081/game/new/')

        # Page updates with game elements
        """light_div = self.browser.find_element_by_id('light_container')
        player_1 = self.browser.find_element_by_id('id_player_1')
        goal_div = self.browser.find_element_by_id('id_goal_div')
        self.assertIn(light_div.text, 'Waiting for a challenger')
        self.assertIn(goal_div.text, 'Destination')
        """
        self.fail('Finish the test!')
