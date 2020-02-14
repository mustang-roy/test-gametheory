class Player:

    __decision: bool
    __person: str
    __coins: int

    def __init__(self, decision, person):
        self.__decision = decision
        self.__person = person
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

    def remove_coins(self, coins_2_remove):
        self.__coins -= coins_2_remove

    def give_coins(self, coins_2_give):
        self.__coins += coins_2_give