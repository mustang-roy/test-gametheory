class Player:

    __decision: bool
    __person: str
    __person_number: int
    __coins: int
    __limit_winstreak: int
    __limit_losestreak: int

    def __init__(self, decision, person_num):
        self.__decision = decision
        self.__person_number = person_num
        self.__person = ['fool', 'bad', 'raging', 'pardoner', 'swindler']
        self.__coins = 1000

    @property
    def person_number(self):
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
        
        def fool_decision(winstreak, losestreak):
            self.__decision = True

        def bad_decision(winstreak, losestreak):
            self.__decision = False
        
        def rager_decision(winstreak, losestreak):
            if (losestreak >= 1):
                self.__decision = False

        def pardoner_decision(winstreak, losestreak):
            
            if (losestreak >= 1):
                self.__decision = False
            else:
                self.__decision = True

        def swindler_decision(winstreak, losestreak):
            if(winstreak >= 2 and losestreak == 0):
                self.__decision = False
            
            elif (losestreak >= 1 and winstreak == 0):
                self.__decision = True

        type_player = {
            0 : fool_decision,
            1 : bad_decision,
            2 : rager_decision,
            3 : pardoner_decision,
            4 : swindler_decision,
        }

        type_player[self.__person_number](winstreak, losestreak)


    def remove_coins(self, coins_2_remove):
        self.__coins -= coins_2_remove

    def give_coins(self, coins_2_give):
        self.__coins += coins_2_give