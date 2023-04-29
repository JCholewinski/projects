from classes import Game, InterfereWithOtherShips, ShipDestroyed, InputError
from classes import compile_text
from bot import create_random_Field_for_bot, bot_shot
import argparse


def compile_box_to_text(box):
    """
    Returns box's text format.
    """
    tab = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
    text = f"{tab[box[1]-1]}{box[0]}"
    return text


def main():
    """
    Function is resposible for whole gameplay, locate ships on field,
    generate battlefield for bot, input from user and execute volley of shots,
    point winner at the end.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('--file_ships_json')
    args = parser.parse_args()
    if args.file_ships_json:
        path = args.file_ships_json
    else:
        path = "ships.json"
    print("*GRA STATKI\n*")
    player_name = input("Podaj swoją nazwę:\n")
    if player_name == "Bot":
        player_name = "bot"
    bot_name = "Bot"
    size = 10
    game = Game(player_name, size)
    with open(path, 'r') as file_handle:
        game.load_ships_json(file_handle)
    print("Ustaw swoje statki:\n")
    print(game.get_player().get_field_str_format())
    game.position_ships_player()
    create_random_Field_for_bot(game.get_bot(), game.get_list_of_ships())
    winner = None
    player_memory = []
    bot_memory_last_hited = []
    counter = 1
    while winner is None:
        print(f"Tura {counter}:\n")
        shot = True
        while shot is True:
            try:
                print(f"Planer ataku {player_name}:\n")
                print(game.get_player().get_made_shots_str_format())
                box = compile_text(input("Podaj koordynaty strzału:\n"), size)
                if box in player_memory:
                    raise InterfereWithOtherShips
                player_memory.append(box)
                shot = game.shot(box, player_name)
                if shot is True:
                    print(f"{player_name} trafia!\n")
                elif shot is False:
                    print(f"{player_name} pudłuje!\n")
                    input("Przejdź do następnego kroku wciskając Enter.\n")
            except ShipDestroyed:
                print("Trafiony zatopiony!!!\n")
                if game.does_player_win(player_name) is True:
                    winner = player_name
                    shot = False
            except InterfereWithOtherShips:
                print("Nie strzelej dwa razy w to samo pole!!!\n")
            except InputError:
                print("Zły format pola!!!\n")
        shot_bot = True
        while shot_bot is True and winner is None:
            try:
                box = bot_shot(game.get_bot(), bot_memory_last_hited)
                shot_bot = game.shot(box, bot_name)
                print(f"Bot strzelił w {compile_box_to_text(box)}")
                print(f"{player_name} statki:\n")
                print(game.get_player().get_field_str_format())
                if shot_bot is True:
                    bot_memory_last_hited.append(box)
                input("Przejdź do następnego kroku wciskając Enter.\n")
            except ShipDestroyed:
                print("Trafiony zatopiony!!!\n")
                print(f"Pole bitwy {player_name}:\n")
                print(game.get_player().get_field_str_format())
                if game.does_player_win(bot_name) is True:
                    winner = bot_name
                bot_memory_last_hited = []
                input("Przejdź do następnego kroku wciskając Enter.\n")
        counter += 1
    print(f"Wygrał {winner}!")


if __name__ == '__main__':
    main()
