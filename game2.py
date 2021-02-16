import numpy as np
import time

class Game:

    def __init__(self, vision, controller):
        self.vision = vision
        self.controller = controller
        self.state = 'not_started'

    def run(self):
        while True:
            self.vision.refresh_frame()
            if self.state == 'not_started' and self.found_play():
                self.log('Round needs to be started, pressing play')
                #self.launch_game()
                #self.state = 'started1'
            elif self.state == 'started1' and self.found_start():
                self.log('Found start button, attempting to start round')
                self.launch_game2()
                self.state = 'started2'
            elif self.state == 'started2' and self.round_found():
                self.log('Round found, clicking to enter')
                self.launch_game3()
                self.state = 'in_game'
            elif self.state == 'in_game':
                if self.found_3star():
                    self.log('Round in progress, found 3 star unit, attempting to buy them')
                    self.buy_3star()
                if self.found_4star():
                    self.log('Round in progress, found 4 star unit, attempting to buy them')
                    self.buy_4star()
                if self.found_chosen():
                    self.log('Round in progress, found chosen unit, attempting to buy them')
                    self.buy_chosen()
                if self.found_ball():
                    self.log('Found item ball, trying to pick it up')
                    self.click_ball()
                if self.found_exp():
                    self.log('Found exp button, trying to increase lvl')
                    self.buy_exp()
                if  self.found_exit_now():
                    self.log('Found exit button, attempting to start new round')
                    self.exit_game()
                if  self.found_end():
                    self.log('Found restart button, attempting to start new round')
                    self.restart_game()
                    self.state = 'started1'
                if  self.emergency_exit():
                    quit()
                else:
                    self.log('Not doing anything')
                time.sleep(1)
            else:
                 self.log('Not doing anything')
            time.sleep(1)



    def found_play(self):
        matches = self.vision.find_template('play')
        return np.shape(matches)[1] >= 1



    def log(self, text):
        print('[%s] %s' % (time.strftime('%H:%M:%S'), text))
