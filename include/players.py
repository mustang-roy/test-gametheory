class Player:

    __decision: bool
    __person: str
    __person_number: int
    __coins: int
    __limit_winstreak: int
    __limit_losestreak: int

    def __init__(self, decision, person_num, limit_winstreak, limit_losestreak):
        self.__decision = decision
        self.__person_number = person_num
        self.__person = ['fool', 'bad', 'raging', 'pardoner', 'swindler']
        self.__limit_losestreak = limit_losestreak
        self.__limit_winstreak = limit_winstreak
        self.__coins = 1000

    @property
    def person_number():
        return self.__person_number

    @property
    def decision(self):
        return self.__decision
    
    @property
    def person(self):
        return self.__person[self.__person_number]
    
    @property
    def coins(self):
        return self.__coins

    def set_decision(self, winstreak, losestreak):
        
        if (self.__limit_winstreak < winstreak or self.__limit_losestreak < losestreak):
            self.__decision = False
            print('setando false')

        else:
            self.__decision = True
            print('setando true')


    def remove_coins(self, coins_2_remove):
        self.__coins -= coins_2_remove

    def give_coins(self, coins_2_give):
        self.__coins += coins_2_give