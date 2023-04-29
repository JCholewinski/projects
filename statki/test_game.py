from classes import Ship, Field, Player, Game
from classes import can_it_fit, compile_text, create_table,\
                    how_many_boxes_vertically, position_from_other_boxes,\
                    widen_field, how_many_boxes_horizontally, distance,\
                    distance_in_line, will_ship_fit
from classes import CanNotBeHere, CanNotBeBias, CanNotBeHorizontally,\
                    CanNotBeVertically, InputError, MoreThanOneError,\
                    ShipDestroyed, InterfereWithOtherShips
from bot import ShootedBox, can_bot_hit, choose_random_box_row_end_table,\
                choose_random_box_col_end_table
from battleship import compile_box_to_text
import pytest
from io import StringIO


def test_distance_bias():
    assert distance([1, 1], [3, 3]) == 2


def test_distance_row():
    assert distance([1, 1], [1, 3]) == 2


def test_distance_col():
    assert distance([1, 1], [3, 1]) == 2


def test_distance_in_line():
    assert distance_in_line([[1, 1], [1, 2]], [1, 4]) == 2


def test_distance_in_line_bias():
    assert distance_in_line([[1, 1], [1, 2]], [2, 4]) == 2


def test_create_table():
    assert create_table("o", 2) == [["o", "o"], ["o", "o"]]


def test_widen_field():
    field = [['.', 'o'],
             ['o', '.']]
    widen_field(field) == [['.', '.', '.', '.'],
                           ['.', '.', 'o', '.'],
                           ['.', 'o', '.', '.'],
                           ['.', '.', '.', '.']]


def test_can_it_fit():
    field = create_table('.', 3)
    field[0][0] = 'o'
    assert can_it_fit(field, [3, 3])


def test_can_it_fit_not():
    field = create_table('.', 3)
    field[0][0] = 'o'
    assert not can_it_fit(field, [2, 2])


def test_can_it_fit_two_boxes():
    field = create_table('.', 3)
    field[0][0] = 'o'
    field[2][2] = 'o'
    assert can_it_fit(field, [1, 3])


def test_can_it_fit_two_boxes_not():
    field = create_table('.', 3)
    field[0][0] = 'o'
    field[2][2] = 'o'
    assert not can_it_fit(field, [2, 2])


def test_how_many_boxes_vertically():
    field = create_table('.', 4)
    field[0][0] = 'o'
    assert how_many_boxes_vertically(field, [1, 3]) == 4


def test_how_many_boxes_vertically_interfere_ship():
    field = create_table('.', 4)
    field[0][0] = 'o'
    assert how_many_boxes_vertically(field, [4, 1]) == 2


def test_how_many_boxes_vertically_interfere_ship_from_other_line():
    field = create_table('.', 4)
    field[0][0] = 'o'
    assert how_many_boxes_vertically(field, [3, 2]) == 2


def test_how_many_boxes_vertically_ships_from_both_sides():
    field = create_table('.', 5)
    field[0][0] = 'o'
    field[4][1] = 'o'
    assert how_many_boxes_vertically(field, [3, 1]) == 1


def test_how_many_boxes_vertically_interfere_double_ship_from_other_line():
    field = create_table('.', 4)
    field[0][0] = 'o'
    field[1][0] = 'o'
    assert how_many_boxes_vertically(field, [4, 2]) == 1


def test_how_many_boxes_horizontally():
    field = create_table('.', 4)
    field[0][0] = 'o'
    assert how_many_boxes_horizontally(field, [3, 3]) == 4


def test_how_many_boxes_horizontally_interfere_ship():
    field = create_table('.', 4)
    field[0][0] = 'o'
    assert how_many_boxes_horizontally(field, [1, 3]) == 2


def test_how_many_boxes_horizontally_interfere_ship_from_other_line():
    field = create_table('.', 4)
    field[0][0] = 'o'
    assert how_many_boxes_horizontally(field, [2, 3]) == 2


def test_how_many_boxes_horizontally_ships_from_both_sides():
    field = create_table('.', 5)
    field[0][0] = 'o'
    field[1][4] = 'o'
    assert how_many_boxes_horizontally(field, [1, 3]) == 1


def test_how_many_boxes_horizontally_interfere_double_ship_from_other_line():
    field = create_table('.', 4)
    field[0][0] = 'o'
    field[0][1] = 'o'
    assert how_many_boxes_horizontally(field, [1, 4]) == 1


def test_will_ship_fit():
    with pytest.raises(CanNotBeHere):
        field = create_table('.', 3)
        field[0][0] = 'o'
        field[2][2] = 'o'
        will_ship_fit(field, [1, 3], 2)


def test_position_from_other_boxes():
    field = create_table('.', 5)
    field[0][0] = 'o'
    field[0][1] = 'o'
    field[0][2] = 'o'
    assert position_from_other_boxes([[1, 5]], [2, 5], field, 3)


def test_position_from_other_boxes_too_far():
    with pytest.raises(MoreThanOneError):
        field = create_table('.', 5)
        field[0][0] = 'o'
        field[0][1] = 'o'
        field[0][2] = 'o'
        assert position_from_other_boxes([[1, 5]], [3, 5], field, 3)


def test_position_from_other_boxes_bad_shape():
    with pytest.raises(CanNotBeBias):
        field = create_table('.', 5)
        field[0][0] = 'o'
        field[0][1] = 'o'
        assert position_from_other_boxes([[1, 5]], [2, 4], field, 3)


def test_position_from_other_boxes_not_horizontally():
    with pytest.raises(CanNotBeHorizontally):
        field = create_table('.', 5)
        field[0][0] = 'o'
        field[0][1] = 'o'
        assert position_from_other_boxes([[1, 5]], [1, 4], field, 3)


def test_position_from_other_boxes_not_vertically():
    with pytest.raises(CanNotBeVertically):
        field = create_table('.', 5)
        field[0][0] = 'o'
        field[1][0] = 'o'
        assert position_from_other_boxes([[5, 1]], [4, 1], field, 3)


def test_position_from_other_boxes_more_than_one_len_table():
    field = create_table('.', 5)
    field[0][0] = 'o'
    field[0][1] = 'o'
    field[0][2] = 'o'
    assert position_from_other_boxes([[1, 5], [2, 5]], [3, 5], field, 3)


def test_position_from_other_boxes_more_than_one_len_table_bad_shape():
    with pytest.raises(CanNotBeBias):
        field = create_table('.', 5)
        field[0][0] = 'o'
        field[0][1] = 'o'
        assert position_from_other_boxes([[1, 5], [1, 4]], [2, 4], field, 3)


def test_position_from_other_boxes_more_than_one_len_table_too_far_bias():
    with pytest.raises(CanNotBeBias):
        field = create_table('.', 5)
        assert position_from_other_boxes([[1, 5], [1, 4]], [3, 3], field, 3)


def test_position_from_other_boxes_more_than_one_len_table_too_far_in_row():
    with pytest.raises(MoreThanOneError):
        field = create_table('.', 5)
        assert position_from_other_boxes([[1, 5], [1, 4]], [1, 2], field, 3)


def test_position_from_other_boxes_more_than_one_len_table_too_far_in_col():
    with pytest.raises(MoreThanOneError):
        field = create_table('.', 5)
        assert position_from_other_boxes([[5, 1], [4, 1]], [2, 1], field, 3)


def test_compile_text():
    assert compile_text("A7", 10) == [7, 1]


def test_compile_textinverted():
    assert compile_text("7A", 10) == [7, 1]


def test_compile_text_with_spaces():
    assert compile_text(" A   7 ", 10) == [7, 1]


def test_compile_text_other_signs():
    with pytest.raises(InputError):
        compile_text("A7#", 10)


def test_compile_text_more_than_one_letter():
    with pytest.raises(InputError):
        compile_text("AA7", 10)


def test_compile_text_out_of_range():
    with pytest.raises(InputError):
        compile_text("A11", 10)


def test_compile_text_letter_out_of_range():
    with pytest.raises(InputError):
        compile_text("O1", 10)


def test_compile_text_two_numbers():
    with pytest.raises(InputError):
        compile_text("10", 10)


def test_compile_text_kot():
    with pytest.raises(InputError):
        compile_text("ibafgSw4wc", 10)


def test_ship():
    ship = Ship("jednomasztowiec", 1)
    assert ship.name == "jednomasztowiec"
    assert ship.lives == 1
    assert ship.territory is None


def test_get_lives():
    ship = Ship("jednomasztowiec", 1)
    assert ship.get_lives() == 1


def test_get_name():
    ship = Ship("jednomasztowiec", 1)
    assert ship.get_name() == "jednomasztowiec"


def test_ship_set_get_territory():
    ship = Ship("jednomasztowiec", 1)
    ship.set_territory([1, 1])
    assert ship.get_territory() == [1, 1]


def test_ship_get_on_the_field():
    ship = Ship("jednomasztowiec", 1)
    assert ship.get_on_the_field() is False


def test_set_on_the_field():
    ship = Ship("jednomasztowiec", 1)
    ship.set_on_the_field()
    assert ship.get_on_the_field() is True


def test_ship_hit_yes():
    ship = Ship("jednomasztowiec", 1)
    ship.set_territory([[1, 1]])
    assert ship.hit([1, 1]) is True
    assert ship.get_lives() == 0


def test_ship_hit_not():
    ship = Ship("jednomasztowiec", 1)
    ship.set_territory([1, 1])
    assert ship.hit([1, 2]) is False
    assert ship.get_lives() == 1


def test_ship_is_ship_destroyed_yes():
    ship = Ship("jednomasztowiec", 1)
    ship.set_territory([[1, 1]])
    ship.hit([1, 1])
    assert ship.is_ship_destoyed() is True


def test_ship_is_ship_destroyed_not():
    ship = Ship("jednomasztowiec", 1)
    ship.set_territory([1, 1])
    ship.hit([1, 2])
    assert ship.is_ship_destoyed() is False


def test_Field():
    field = Field(2)
    assert field.field == [[".", "."], [".", "."]]


def test_Field_get_field():
    field = Field(2)
    assert field.get_field() == [[".", "."], [".", "."]]


def test_Field_position_ship_on_field():
    field = Field(2)
    ship = Ship("jednomasztowiec", 1)
    ship.set_territory([[1, 1]])
    field.position_ship_on_field(ship)
    assert field.get_field() == [['o', '.'], ['.', '.']]
    assert ship.get_on_the_field()
    assert field.get_list_of_ship_on_field() == [ship]


def test_Field_set_box_on_field():
    field = Field(2)
    field.set_box_on_field([1, 1], 'P')
    assert field.get_field() == [['P', '.'], ['.', '.']]


def test_Player():
    player = Player("gracz", 2)
    assert player.name == "gracz"
    assert len(player.Field.get_field()) == 2
    assert len(player.made_shots) == 2
    assert player.list_of_ships == []


def test_Player_get_name():
    player = Player("gracz", 2)
    assert player.get_name() == "gracz"


def test_Player_get_Field():
    player = Player("gracz", 2)
    assert player.get_Field() == player.Field


def test_Player_get_made_shots():
    player = Player("gracz", 2)
    assert player.get_made_shots() == [['.', '.'], ['.', '.']]


def test_Player_get_list_of_ships():
    player = Player("gracz", 2)
    assert player.get_list_of_ships() == []


def test_Player_add_ship():
    player = Player("gracz", 2)
    ship = Ship("jednomasztowiec", 1)
    ship.set_territory([[1, 1]])
    player.add_ship(ship)
    assert player.get_list_of_ships()[0] is ship
    assert player.get_Field().get_field() == [['o', '.'], ['.', '.']]


def test_Player_get_sum_of_ships_lives():
    player = Player("gracz", 2)
    ship = Ship("jednomasztowiec", 1)
    ship.set_territory([[1, 1]])
    player.add_ship(ship)
    assert player.get_sum_of_ships_lives() == 1


def test_Player_get_shot_yes():
    player = Player("gracz", 2)
    ship = Ship("jednomasztowiec", 1)
    ship.set_territory([[1, 1]])
    player.add_ship(ship)
    player.get_shot([1, 1], True)
    assert player.get_Field().get_field() == [['x', '.'], ['.', '.']]


def test_Player_get_shot_not():
    player = Player("gracz", 2)
    ship = Ship("jednomasztowiec", 1)
    ship.set_territory([[1, 1]])
    player.add_ship(ship)
    player.get_shot([1, 2], False)
    assert player.get_Field().get_field() == [['o', 'P'], ['.', '.']]


def test_Player_made_shot_yes():
    player = Player("gracz", 2)
    player.made_shot([1, 1], True)
    assert player.get_made_shots() == [['x', '.'], ['.', '.']]


def test_Player_made_shot_not():
    player = Player("gracz", 2)
    player.made_shot([1, 1], False)
    assert player.get_made_shots() == [['P', '.'], ['.', '.']]


def test_Player_get_destroyed_made_shots():
    player = Player("gracz", 2)
    player.set_destroyed_ship_made_shots([[1, 1]])
    assert player.get_made_shots() == [['X', '.'], ['.', '.']]


def test_Game():
    game = Game("gracz", 2)
    assert game.get_player().get_name() == "gracz"
    assert game.get_bot().get_name() == "Bot"
    assert game.list_of_ships is None


def test_Game_set_get_list_of_ships():
    game = Game("gracz", 2)
    ship = Ship("jednomasztowiec", 1)
    ships = [ship]
    game.set_list_of_ships(ships)
    assert game.get_list_of_ships() is ships


def test_Game_load_ships_json():
    file_handle = StringIO('[{"name": "jednomasztowiec", "lives": 1},\
        {"name": "dwumasztowiec", "lives": 2}]')
    game = Game(['player'], 10)
    game.load_ships_json(file_handle)
    ships = game.get_list_of_ships()
    assert len(ships) == 2
    assert ships[0].get_name() == 'jednomasztowiec'
    assert ships[0].get_lives() == 1
    assert ships[1].get_name() == 'dwumasztowiec'
    assert ships[1].get_lives() == 2


def test_Game_shot_yes():
    game = Game("gracz", 2)
    ship = Ship("dwumasztowiec", 2)
    ship.set_territory([[1, 1], [1, 2]])
    game.get_bot().add_ship(ship)
    assert game.shot([1, 1], "gracz") is True


def test_Game_shot_not():
    game = Game("gracz", 2)
    ship = Ship("dwumasztowiec", 2)
    ship.set_territory([[1, 1], [1, 2]])
    game.get_bot().add_ship(ship)
    assert game.shot([2, 1], "gracz") is False


def test_Game_shot_ship_destroyed():
    with pytest.raises(ShipDestroyed):
        game = Game("gracz", 2)
        ship = Ship("dwumasztowiec", 1)
        ship.set_territory([[1, 1]])
        game.get_bot().add_ship(ship)
        game.shot([1, 1], "gracz")


def test_Game_does_player_win_not():
    game = Game("gracz", 2)
    ship = Ship("dwumasztowiec", 2)
    ship.set_territory([[1, 1], [1, 2]])
    game.get_bot().add_ship(ship)
    game.shot([1, 1], "gracz")
    assert game.does_player_win("gracz") is False


def test_Game_does_player_win():
    game = Game("gracz", 2)
    assert game.does_player_win("gracz") is True


def test_compile_box_to_text():
    box = [1, 1]
    assert compile_box_to_text(box) == "A1"


def test_can_bot_hit():
    made_shots = [['.', '.'], ['.', '.']]
    assert can_bot_hit(made_shots, [1, 1]) is True


def test_can_bot_hit2():
    made_shots = [['.', 'x'], ['.', '.']]
    assert can_bot_hit(made_shots, [1, 1]) is True


def test_can_bot_hit_ShootedBox1():
    with pytest.raises(ShootedBox):
        made_shots = [['x', '.'], ['.', '.']]
        can_bot_hit(made_shots, [1, 1])


def test_can_bot_hit_ShootedBox2():
    with pytest.raises(ShootedBox):
        made_shots = [['P', '.'], ['.', '.']]
        can_bot_hit(made_shots, [1, 1])


def test_can_bot_hit_ShootedBox3():
    with pytest.raises(ShootedBox):
        made_shots = [['X', '.'], ['.', '.']]
        can_bot_hit(made_shots, [1, 1])


def test_can_bot_hit_InterfereWithOtherSpis():
    with pytest.raises(InterfereWithOtherShips):
        made_shots = [['.', 'X'], ['.', '.']]
        can_bot_hit(made_shots, [1, 1])


def test_choose_random_box_row_end_table_first(monkeypatch):
    def return_first(table):
        return table[0]
    monkeypatch.setattr("random.choice", return_first)
    assert choose_random_box_row_end_table([[2, 2], [2, 3]]) == [2, 1]


def test_choose_random_box_row_end_table_second(monkeypatch):
    def return_second(table):
        return table[1]
    monkeypatch.setattr("random.choice", return_second)
    assert choose_random_box_row_end_table([[2, 2], [2, 3]]) == [2, 4]


def test_choose_random_box_col_end_table_first(monkeypatch):
    def return_first(table):
        return table[0]
    monkeypatch.setattr("random.choice", return_first)
    assert choose_random_box_col_end_table([[2, 2], [3, 2]]) == [1, 2]


def test_choose_random_box_col_end_table_second(monkeypatch):
    def return_second(table):
        return table[1]
    monkeypatch.setattr("random.choice", return_second)
    assert choose_random_box_col_end_table([[2, 2], [3, 2]]) == [4, 2]
