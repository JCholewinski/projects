import random
import copy
from classes import CanNotBeHere, CanNotBeVertically, InterfereWithOtherShips,\
    CanNotBeHorizontally, can_it_fit, position_from_other_boxes,\
    will_ship_fit, widen_field
import operator


class OutOfRange(Exception):
    """
    Exception which represents going out of range.
    """
    pass


class ShootedBox(Exception):
    """
    Exception which represents shooted box.
    """
    pass


def choose_random_box_row_end_table(table):
    """
    Returns chocie between two boxes at the edn of territory
    in horizontally orientation.
    Function assume that there is at least 2 boxes in table.
    """
    table = copy.copy(table)
    table = sorted(table, key=operator.itemgetter(1))
    min = table[0][1]
    max = table[-1][1]
    choice = random.choice([min-1, max+1])
    box = [table[0][0], choice]
    return box


def choose_random_box_col_end_table(table):
    """
    Returns chocie between two boxes at the edn of territory
    in vertically orientation.
    Function assume that there is at least 2 boxes in table.
    """
    table = copy.copy(table)
    table = sorted(table)
    min = table[0][0]
    max = table[-1][0]
    choice = random.choice([min-1, max+1])
    box = [choice, table[0][1]]
    return box


def can_bot_hit(made_shots, box):
    """
    Function check if bot can hit in this box.
    If not, function raises exception.
    """
    new_made_shots = widen_field(made_shots)
    row = box[0]
    col = box[1]
    if new_made_shots[row][col] == 'P' or new_made_shots[row][col] == 'x'\
            or new_made_shots[row][col] == 'X':
        raise ShootedBox
    else:
        for i in range(-1, 2):
            for j in range(-1, 2):
                val = new_made_shots[row+i][col+j]
                if val == "X":
                    raise InterfereWithOtherShips
        return True


def create_random_Field_for_bot(bot, list_of_ships):
    """
    Function generate random battlefiled for bot.
    """
    Field_of_bot = bot.get_Field().get_field()
    list_of_ships = copy.deepcopy(list_of_ships)
    size = len(Field_of_bot)
    memory = []
    for ship in list_of_ships:
        table = []
        while len(table) < ship.get_lives():
            try:
                box = [random.randint(1, size), random.randint(1, size)]
                if not can_it_fit(Field_of_bot, box):
                    raise InterfereWithOtherShips
                if box in memory:
                    raise InterfereWithOtherShips
                else:
                    will_ship_fit(Field_of_bot, box, ship.get_lives())
                    table.append(box)
                    memory.append(box)
                    while len(table) < ship.get_lives():
                        try:
                            choice = random.choice([[1, 0], [-1, 0], [0, 1], [0, -1]])
                            selected_box = [box[0]+choice[0], box[1]+choice[1]]
                            if selected_box[0] < 1 or selected_box[0] > size\
                                    or selected_box[1] < 1\
                                    or selected_box[1] > size:
                                raise OutOfRange
                            if not can_it_fit(Field_of_bot, selected_box):
                                raise InterfereWithOtherShips
                            if selected_box in memory:
                                raise InterfereWithOtherShips
                            else:
                                position_from_other_boxes(table, selected_box,
                                                          Field_of_bot, ship.get_lives())
                                table.append(selected_box)
                                memory.append(selected_box)
                                while len(table) < ship.get_lives():
                                    try:
                                        if table[0][0] == table[1][0]:
                                            selected_box2 = choose_random_box_row_end_table(table)
                                            if selected_box2[1] < 1 or selected_box2[1] > size:
                                                raise OutOfRange
                                            if not can_it_fit(Field_of_bot, selected_box2):
                                                raise InterfereWithOtherShips
                                            if selected_box2 in memory:
                                                raise InterfereWithOtherShips
                                            table.append(selected_box2)
                                            memory.append(selected_box2)
                                        elif table[0][1] == table[1][1]:
                                            selected_box3 = choose_random_box_col_end_table(table)
                                            if selected_box3[0] < 1 or selected_box3[0] > size:
                                                raise OutOfRange
                                            if not can_it_fit(Field_of_bot, selected_box3):
                                                raise InterfereWithOtherShips
                                            if selected_box3 in memory:
                                                raise InterfereWithOtherShips
                                            table.append(selected_box3)
                                            memory.append(selected_box3)
                                    except (OutOfRange, InterfereWithOtherShips):
                                        pass
                        except (OutOfRange, CanNotBeHorizontally,
                                CanNotBeVertically, InterfereWithOtherShips):
                            pass
                ship.set_territory(table)
                bot.add_ship(ship)
            except (InterfereWithOtherShips, CanNotBeHere):
                pass


def bot_shot(bot, table):
    """
    Function choose random box for shot, where can be ship.
    """
    made_shots_of_bot = bot.get_made_shots()
    size = len(made_shots_of_bot)
    if len(table) == 0:
        while True:
            try:
                box = [random.randint(1, size), random.randint(1, size)]
                if can_bot_hit(made_shots_of_bot, box):
                    return box
            except (ShootedBox, InterfereWithOtherShips):
                pass
    else:
        if len(table) == 1:
            while True:
                try:
                    down_box = table[0]
                    choice = random.choice([[1, 0], [-1, 0], [0, 1], [0, -1]])
                    box = [down_box[0]+choice[0], down_box[1]+choice[1]]
                    if box[0] < 1 or box[0] > size or box[1] < 1 or box[1] > size:
                        raise OutOfRange
                    if can_bot_hit(made_shots_of_bot, box):
                        return box
                except (ShootedBox, InterfereWithOtherShips, OutOfRange):
                    pass
        else:
            while True:
                try:
                    if table[0][0] == table[1][0]:
                        box = choose_random_box_row_end_table(table)
                        if box[0] < 1 or box[0] > size or box[1] < 1 or box[1] > size:
                            raise OutOfRange
                        if can_bot_hit(made_shots_of_bot, box):
                            return box
                    elif table[0][1] == table[1][1]:
                        box = choose_random_box_col_end_table(table)
                        if box[0] < 1 or box[0] > size or box[1] < 1 or box[1] > size:
                            raise OutOfRange
                        if can_bot_hit(made_shots_of_bot, box):
                            return box
                except (ShootedBox, InterfereWithOtherShips, OutOfRange):
                    pass
