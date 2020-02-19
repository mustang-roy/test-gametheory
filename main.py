from include.players import Player
from include.game import Game



bad_player = Player(False,1, 100000, 0)
fool_player = Player(True,0, 100000, 100000)
raging_player = Player(True,2, 100000, 10000)
pardoner_player = Player(True,3, 100000, 100000)
swindler_player = Player(True,4 , 100000, 100000)


game1 = Game(fool_player, raging_player)

game1.play_game()


print(game1.player_1_coin)
print(game1.player_2_coin)

print(game1.player_1_winstreak)
print(game1.player_2_winstreak)





