from selenium import webdriver
import unittest


class FirstPlayerTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_creates_a_new_game(self):
        # Player one goes to site
        self.browser.get('http://localhost:8000')

        # Player sees name of game in page title
        self.assertIn('Red', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('Green', header_text)

        # Player sees button to start a new game
        new_game_btn = self.browser.find_element_by_id('id_new_game')
        self.assertEqual(new_game_btn.text, 'Create New Game')

        # Player clicks new game button to start a new game
        new_game_btn.click()

        # Page updates with game elements
        light_div = self.browser.find_element_by_id('light_container')
        player_1 = self.browser.find_element_by_id('id_player_1')
        goal_div = self.browser.find_element_by_id('id_goal_div')
        self.assertIn(light_div.text, 'Waiting for a challenger')
        self.assertIn(goal_div.text, 'Destination')

        self.fail('Finish the test!')

if __name__ == '__main__':
    unittest.main()