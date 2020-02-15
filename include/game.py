from include.players import Player

class Game:

    __round: int
    __player1: Player
    __player2: Player
    __winstreak_p1 = 0
    __losestreak_p1 = 0
    __winstreak_p2 = 0
    __losestreak_p2 = 0

    def __init__(self, player_1, player_2):
        self.__round = 100
        self.__player1 = player_1
        self.__player2 = player_2


    @property
    def player_1_name(self):
        return self.__player1.person

    @property
    def player_2_name(self):
        return self.__player2.person
    
    @property
    def player_1_coin(self):
        return self.__player1.coins
    
    @property
    def player_2_coin(self):
        return self.__player2.coins

    #def verify_decision(self):

    def remove_coin_p1(self, n_coins):
        self.__player1.remove_coins(n_coins)

    def remove_coin_p2(self, n_coins):
        self.__player2.remove_coins(n_coins)
    
    def add_coin_p1(self, n_coins):
        self.__player1.give_coins(n_coins)
    
    def add_coin_p2(self, n_coins):
        self.__player2.give_coins(n_coins)

    def bet_step (self):

        if (self.__player1.decision == True):
            self.remove_coin_p1(1)
            bet_player1 = True

        else:
            bet_player1 = False

        if (self.__player2.decision == True):
            self.remove_coin_p2(1)
            bet_player2 = True
                
        else:
            bet_player2 = False

    def result_step (self, bet_player1, bet_player2):
        if (bet_player1 == True and bet_player2 == True):
            self.add_coin_p1(2)
            self.add_coin_p2(2)

        if (bet_player1 == True and bet_player2 == False):
            self.add_coin_p2(3)

        if (bet_player2 == True and bet_player1 == False):
            self.add_coin_p1(3)

        if (bet_player2 == False and bet_player1 == False):
            self.remove_coin_p1(2)
            self.remove_coin_p2(2)

    def play_game(self):

        rounds = self.__round

        bet_player1 = True
        bet_player2 = True


        for r in range(rounds):

            self.bet_step()
            self.result_step(bet_player1, bet_player2)
            