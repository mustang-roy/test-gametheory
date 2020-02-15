from include.players import Player
from include.game import Game

bad_player = Player(False, 'bad', 100000, 0)
fool_player = Player(True, 'fool', 100000, 100000)
raging_player = Player(True, 'raging', 100000, 10000)
pardoner_player = Player(True, 'pardon', 100000, 100000)
swindler_player = Player(True, 'swindler', 100000, 100000)

game1 = Game(fool_player, fool_player)

game1.play_game()

print(game1.player_1_coin)
print(game1.player_2_coin)





