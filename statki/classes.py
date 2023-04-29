import copy
import json


class CanNotBeHere(Exception):
    """
    Exception which represent that the ship can not be here
    """
    pass


class CanNotBeVertically(Exception):
    """
    Exception which represent that the ship can not vertically
    """
    pass


class CanNotBeHorizontally(Exception):
    """
    Exception which represent that the ship can not horizontally
    """
    pass


class CanNotBeBias(Exception):
    """
    Exception which represent that the ship has incorrect shap
    """
    pass


class MoreThanOneError(Exception):
    """
    Exception which represent that the box is too far from rest of ship
    """
    pass


class InterfereWithOtherShips(Exception):
    """
    Exception which represent that there is other ship in the area
    """
    pass


class InputError(Exception):
    """
    Exception which represent that user gave incorrect input
    """
    pass


class RestOfShip(Exception):
    """
    Exception which represent that the box is in the rest of ship
    """
    pass


class ShipDestroyed(Exception):
    """
    Exception which represent that the ship is destroyed
    """
    pass


class Winner(Exception):
    """
    Exception which represent that there is a winner
    """
    pass


def distance(box1, box2):
    """
    Reteurns the distance between two boxes, box -> [row, col].
    Diagonal distance is also counted as 1.
    """
    return max(abs(box1[0]-box2[0]), abs(box1[1]-box2[1]))


def distance_in_line(table, box):
    """
    Returns the smallest distance between the box and boxes from table.
    Box -> [row,col]
    """
    val = distance(table[0], box)
    for place in table:
        dis = distance(place, box)
        val = min(dis, val)
    return val


def create_table(sign, size):
    """
    Returns the table which size is sizeXsize and the table is filled with sigs
    """
    return [[sign for i in range(size)]for j in range(size)]


def widen_field(table):
    """
    Returns the table with frame filled with '.'
    """
    tab = copy.deepcopy(table)
    size = len(tab)
    table_with_zeros = [["." for i in range(size+2)]]
    for row in tab:
        new_row = row
        new_row.insert(0, ".")
        new_row.insert(size+1, ".")
        table_with_zeros.append(new_row)
    table_with_zeros.append(["." for i in range(size+2)])
    return table_with_zeros


def can_it_fit(field, place):
    """
    Returns True if there is not any other ship in the area of place,
    if there is a ship returns False. Place format -> [row, col].
    Field -> Field.get_filed()
    """
    new_field = widen_field(field)
    row = place[0]
    col = place[1]
    for i in range(-1, 2):
        for j in range(-1, 2):
            val = new_field[row+i][col+j]
            if val == "o":
                return False
    return True


def how_many_boxes_vertically(field, place):
    """
    Returns how large ship vertically you can fit from place.
    Function assume that there is not any ship in the area of place.
    """
    counter = 1
    size = len(field)
    col = place[1]
    for row in range(place[0]-1, 0, -1):
        if can_it_fit(field, [row, col]):
            counter += 1
        else:
            break
    for row in range(place[0]+1, size+1):
        if can_it_fit(field, [row, col]):
            counter += 1
        else:
            break
    return counter


def how_many_boxes_horizontally(field, place):
    """
    Returns how large ship horizontally you can fit from place.
    Function assume that there is not any ship in the area of place.
    """
    counter = 1
    size = len(field)
    row = place[0]
    for col in range(place[1]-1, 0, -1):
        if can_it_fit(field, [row, col]):
            counter += 1
        else:
            break
    for col in range(place[1]+1, size+1):
        if can_it_fit(field, [row, col]):
            counter += 1
        else:
            break
    return counter


def will_ship_fit(field, box, long):
    """
    Raise exception CanNotBeHere if ship,
    which has {long} lenght, can not be here.
    """
    if how_many_boxes_horizontally(field, box) < long and\
            how_many_boxes_vertically(field, box) < long:
        raise CanNotBeHere


def position_from_other_boxes(table, box, field, long):
    """
    Function returns True if given box is in correct position from
    the rest of the ship and the ship can be located in this orientation.
    Function assume that number of boxes in table is bigger than one,
    ship always can be located, there is no other ship in the area of box
    and long is bigger than two. If the box can not be located, function
    raise appropriate exception.
    """
    if len(table) == 1:
        row = table[0][0]
        col = table[0][1]
        if distance([row, col], box) > 1:
            raise MoreThanOneError
        elif box == [row+1, col+1] or box == [row+1, col-1] or\
                box == [row-1, col+1] or box == [row-1, col-1]:
            raise CanNotBeBias
        else:
            if row == box[0]:
                if how_many_boxes_horizontally(field, box) < long:
                    raise CanNotBeHorizontally
                else:
                    return True
            elif col == box[1]:
                if how_many_boxes_vertically(field, box) < long:
                    raise CanNotBeVertically
                else:
                    return True
    else:
        if table[0][0] == table[1][0]:
            if box[0] != table[0][0]:
                raise CanNotBeBias
            else:
                if distance_in_line(table, box) == 1:
                    return True
                else:
                    raise MoreThanOneError
        elif table[0][1] == table[1][1]:
            if box[1] != table[0][1]:
                raise CanNotBeBias
            else:
                if distance_in_line(table, box) == 1:
                    return True
                else:
                    raise MoreThanOneError


def compile_text(text, extent):
    """
    Returns coordinates of place by compiling given text.
    Function raises exception if format of text is incorrect.
    Correct text formats -> "LETTER_number", "letter_number"
    "number_LETTER", "number_letter"
    """
    try:
        dict = {"A": 1, "a": 1, "B": 2, "b": 2, "C": 3, "c": 3, "D": 4,
                "d": 4, "E": 5, "e": 5, "F": 6, "f": 6, "G": 7, "g": 7,
                "H": 8, "h": 8, "I": 9, "i": 9, "J": 10, "j": 10}
        word = text.replace(' ', '')
        place = ['', '']
        if len(word) > 3:
            raise InputError
        counter = 0
        for letter in word:
            if letter.isnumeric():
                place[0] += letter
            elif letter in dict:
                place[1] = dict[letter]
                counter += 1
                if counter > 1:
                    raise InputError
            elif letter not in dict:
                raise InputError
        place[0] = int(place[0])
        place[1] = int(place[1])
        if place[0] >= 1 and place[0] <= extent and place[1] >= 1 and\
                place[1] <= 10:
            return place
        else:
            raise InputError
    except ValueError:
        raise InputError


class Ship:
    """
    Class that represents ships in the game
    :param name: name is responsible for representation of ship
    :param lives: lives are responsible for lenght at first
    and than for lives of ship
    :param territory: territory store boxes where ships is located
    :param on_the_field: on_the_field represents if ship is on the field
    :type name: str
    :type lives: int
    :type territory: list
    :type on_the_field: bool
    """
    def __init__(self, name, lives):
        self.name = name
        self.lives = lives
        self.territory = None
        self.on_the_field = False

    def get_lives(self):
        return self.lives

    def get_name(self):
        return self.name

    def get_territory(self):
        return self.territory

    def get_on_the_field(self):
        return self.on_the_field

    def set_territory(self, table):
        self.territory = table

    def set_on_the_field(self, val=True):
        self.on_the_field = val

    def hit(self, box):
        """
        Represenst shot.
        """
        for square in self.territory:
            if square == box:
                self.lives -= 1
                return True
        return False

    def is_ship_destoyed(self):
        """
        Returns if ship is destroyed
        """
        if self.lives == 0:
            return True
        else:
            return False


class Field:
    """
    Class represents battlefield where ships are located
    :param field: represents battlefield
    :param list_of_ships: represents ships on battlefield
    :type field: list
    :type list_of_ships: list
    """
    def __init__(self, size):
        self.field = create_table(".", size)
        self.list_of_ship_on_field = []

    def get_field(self):
        return self.field

    def position_ship_on_field(self, ship):
        """
        Position ship on battlefield.
        """
        ship.set_on_the_field()
        self.list_of_ship_on_field.append(ship)
        for box in ship.get_territory():
            self.field[box[0]-1][box[1]-1] = "o"

    def get_list_of_ship_on_field(self):
        return self.list_of_ship_on_field

    def set_box_on_field(self, box, sign):
        """
        Change given boox on field on given sign
        """
        self.field[box[0]-1][box[1]-1] = sign


class Player:
    """
    Class represents player in game.
    :param name: represents name of player
    :param Field: represents battlefield of player
    :param made_shots: represents plan of attack on the enemy
    :param list_of_ships: represents ships used on the filed
    :type name: str
    :type Field: Field
    :type made_shots: list
    :type list_of_ships: list
    """
    def __init__(self, name, size):
        self.name = name
        self.Field = Field(size)
        self.made_shots = create_table(".", size)
        self.list_of_ships = []

    def get_name(self):
        return self.name

    def get_Field(self):
        return self.Field

    def get_made_shots(self):
        return self.made_shots

    def get_made_shots_str_format(self):
        """
        Returns text representation of plan of atack.
        """
        table = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
        text = f'{" ":^5}'
        size = len(self.made_shots)
        for num_of_word in range(size):
            text += f"{table[num_of_word]:^5}"
        text += "\n"
        for row in range(1, 11):
            text += f"{row:^5}"
            text += f"{self.made_shots[row-1]}\n"
        return text

    def get_field_str_format(self):
        """
        Return text representation of battlefield.
        """
        table = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
        text = f'{" ":^5}'
        size = len(self.Field.get_field())
        for num_of_word in range(size):
            text += f"{table[num_of_word]:^5}"
        text += "\n"
        for row in range(1, 11):
            text += f"{row:^5}"
            text += f"{self.Field.get_field()[row-1]}\n"
        return text

    def get_list_of_ships(self):
        return self.list_of_ships

    def add_ship(self, ship):
        """
        Adds ship to a list_of_ship and position ship on the field.
        """
        self.list_of_ships.append(ship)
        self.get_Field().position_ship_on_field(ship)

    def get_sum_of_ships_lives(self):
        """
        Returns sum of player's ships lives.
        """
        sum = 0
        for ship in self.list_of_ships:
            sum += ship.get_lives()
        return sum

    def get_shot(self, box, val):
        """
        Changes box on field when player got shot.
        """
        if val is True:
            self.Field.set_box_on_field(box, 'x')
        else:
            self.Field.set_box_on_field(box, 'P')

    def made_shot(self, box, val):
        """
        Changes box in plan of attack when player shoots.
        """
        if val is True:
            self.made_shots[box[0]-1][box[1]-1] = 'x'
        else:
            self.made_shots[box[0]-1][box[1]-1] = 'P'

    def set_destroyed_ship_made_shots(self, territory):
        """
        Changes box of destroyed ship in plan of attack.
        """
        for box in territory:
            self.made_shots[box[0]-1][box[1]-1] = "X"


class Game:
    """
    Class that represents gameplay.
    :param players: stores players in game
    :param list_of_ships: represents ships used in game
    :type players: list
    :type list_of_ships: list
    """
    def __init__(self, player_name, size):
        self.players = [Player(player_name, size), Player("Bot", size)]
        self.list_of_ships = None

    def set_list_of_ships(self, ships):
        self.list_of_ships = ships

    def get_list_of_ships(self):
        return self.list_of_ships

    def load_ships_json(self, file_handle):
        """
        Adds ships loaded from json file.
        """
        reader = json.load(file_handle)
        ships = []
        for item in reader:
            name = item['name']
            lives = int(item['lives'])
            ship = Ship(name, lives)
            ships.append(ship)
        self.list_of_ships = ships

    def get_bot(self):
        return self.players[1]

    def get_player(self):
        return self.players[0]

    def position_ships_player(self):
        """
        Initialised method asks user where he/she want to locate his/her
        ship and than ship is locetd on the battlefield.
        Method pick up illegal compositions and do never allow to
        make illegal composition from user.
        """
        ships = copy.deepcopy(self.list_of_ships)
        chosen = self.players[0]
        for ship in ships:
            field = chosen.get_Field().get_field()
            lives = ship.get_lives()
            print(f"Ustaw {ship.get_name()}({lives}):\n")
            table = []
            while len(table) < ship.get_lives():
                try:
                    box = compile_text(input("Podaj pole:"), len(field))
                    if box in table:
                        raise RestOfShip
                    elif not can_it_fit(field, box):
                        raise InterfereWithOtherShips
                    elif len(table) == 0:
                        will_ship_fit(field, box, lives)
                        table.append(box)
                    else:
                        position_from_other_boxes(table, box, field, lives)
                        table.append(box)
                except CanNotBeHere:
                    print("Tu się statek nie zmieści!!!")
                except (CanNotBeVertically, CanNotBeHorizontally):
                    print("Ustawiaj statek w innej orientacji!!")
                except InterfereWithOtherShips:
                    print("Tu nie może stać statek!!!")
                except CanNotBeBias:
                    print("Nie wstawiaj na ukos!!!")
                except MoreThanOneError:
                    print("Wybierz bliższe pole!!!")
                except InputError:
                    print("Niepoprawny format pola!!!")
                except RestOfShip:
                    print("Tu już stoi część statku!!!")
            ship.set_territory(table)
            chosen.add_ship(ship)
            print(chosen.get_field_str_format())

    def shot(self, box, player_name):
        """
        Represents shot of player. Returns true if there is ship
        under the box and false if there is not ship under the box.
        If ship is destroyed, function rises exception ShipDestroyed.
        Method ste boxes on battlefield and plan attack that there was shot.
        """
        for player in self.players:
            if player.get_name() == player_name:
                shooter = player
            else:
                enemy = player
        for ship in enemy.get_list_of_ships():
            if ship.hit(box):
                enemy.get_shot(box, True)
                shooter.made_shot(box, True)
                if ship.get_lives() == 0:
                    ter = ship.get_territory()
                    shooter.set_destroyed_ship_made_shots(ter)
                    raise ShipDestroyed
                return True
        enemy.get_shot(box, False)
        shooter.made_shot(box, False)
        return False

    def does_player_win(self, player_name):
        """
        Returns if player won.
        """
        for player in self.players:
            if player.get_name() != player_name:
                if player.get_sum_of_ships_lives() == 0:
                    return True
                else:
                    return False
