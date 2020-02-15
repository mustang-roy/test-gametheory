class Player:

    __decision: bool
    __person: str
    __coins: int
    __limit_winstreak: int
    __limit_losestreak: int

    def __init__(self, decision, person, limit_winstreak, limit_losestreak):
        self.__decision = decision
        self.__person = person
        self.__limit_losestreak = limit_losestreak
        self.__limit_winstreak = limit_winstreak
        self.__coins = 1000

    @property
    def decision(self):
        return self.__decision
    
    @property
    def person(self):
        return self.__person
    
    @property
    def coins(self):
        return self.__coins

    def set_decision(self, winstreak, losestreak):
        
        if (self.__limit_winstreak < winstreak and self.__limit_losestreak > losestreak):
            self.__decision = False

        else:
            self.__decision = True


    def remove_coins(self, coins_2_remove):
        self.__coins -= coins_2_remove

    def give_coins(self, coins_2_give):
        self.__coins += coins_2_give