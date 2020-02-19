from include.players import Player
from include.game import Game



bad_player = Player(False, 1)
fool_player = Player(True, 0)
fool_player2 = Player (True, 0)
raging_player = Player(True, 2)
pardoner_player = Player(True,3)
swindler_player = Player(True,4)


game1 = Game(fool_player,swindler_player )

game1.play_game()


print(game1.player_1_coin)
print(game1.player_2_coin)

print(game1.player_1_winstreak)
print(game1.player_2_winstreak)





