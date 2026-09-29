from copy import deepcopy
from game_data import INIT_GAME_STATE
from game_functions import start_game

game_state = deepcopy(INIT_GAME_STATE)
start_game(game_state)