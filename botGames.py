import requests

# -----------------------------------------------------------------------
activeGames = {}  # Тут будем накапливать все активные игры. У пользователя может быть только одна активная игра


def newGame(chatID, newGame):
    activeGames.update({chatID: newGame})
    return newGame


def getGame(chatID):
    return activeGames.get(chatID)


def stopGame(chatID):
    activeGames.pop(chatID)


# -----------------------------------------------------------------------
# class Card:
#     emo_SPADES = "U0002660"  # Unicod эмоджи Пики
#     emo_CLUBS = "U0002663"  # Unicod эмоджи Крести
#     emo_HEARTS = "U0002665"  # Unicod эмоджи Черви
#     emo_DIAMONDS = "U0002666"  # Unicod эмоджи Буби
#
#     def __init__(self, card):
#         if isinstance(card, dict):  # если передали словарь
#             self.__card_JSON = card
#             self.code = card["code"]
#             self.suit = card["suit"]
#             self.value = card["value"]
#             self.cost = self.get_cost_card()
#             self.color = self.get_color_card()
#             self.__imagesPNG_URL = card["images"]["png"]
#             self.__imagesSVG_URL = card["images"]["svg"]
#             # print(self.value, self.suit, self.code)
#
#         elif isinstance(card, str):  # карту передали строкой, в формате "2S"
#             self.__card_JSON = None
#             self.code = card
#
#             value = card[0]
#             if value == "0":
#                 self.value = "10"
#             elif value == "J":
#                 self.value = "JACK"
#             elif value == "Q":
#                 self.value = "QUEEN"
#             elif value == "K":
#                 self.value = "KING"
#             elif value == "A":
#                 self.value = "ACE"
#             elif value == "X":
#                 self.value = "JOKER"
#             else:
#                 self.value = value
#
#             suit = card[1]
#             if suit == "1":
#                 self.suit = ""
#                 self.color = "BLACK"
#
#             elif suit == "2":
#                 self.suit = ""
#                 self.color = "RED"
#
#             else:
#                 if suit == "S":
#                     self.suit = "SPADES"  # Пики
#                 elif suit == "C":
#                     self.suit = "CLUBS"  # Крести
#                 elif suit == "H":
#                     self.suit = "HEARTS"  # Черви
#                 elif suit == "D":
#                     self.suit = "DIAMONDS"  # Буби
#
#                 self.cost = self.get_cost_card()
#                 self.color = self.get_color_card()
#
#     def get_cost_card(self):
#         if self.value == "JACK":
#             return 2
#         elif self.value == "QUEEN":
#             return 3
#         elif self.value == "KING":
#             return 4
#         elif self.value == "ACE":
#             return 11
#         elif self.value == "JOKER":
#             return 1
#         else:
#             return int(self.value)
#
#     def get_color_card(self):
#         if self.suit == "SPADES":  # Пики
#             return "BLACK"
#         elif self.suit == "CLUBS":  # Крести
#             return "BLACK"
#         elif self.suit == "HEARTS":  # Черви
#             return "RED"
#         elif self.suit == "DIAMONDS":  # Буби
#             return "RED"
#
# # -----------------------------------------------------------------------
# class Game21:
#     def __init__(self, deck_count=1, jokers_enabled=False):
#         new_pack = self.new_pack(deck_count, jokers_enabled)  # в конструкторе создаём новую пачку из deck_count-колод
#         if new_pack is not None:
#             self.pack_card = new_pack  # сформированная колода
#             self.remaining = new_pack["remaining"],  # количество оставшихся карт в колоде
#             self.card_in_game = []  # карты в игре
#             self.arr_cards_URL = []  # URL карт игрока
#             self.score = 0  # очки игрока
#             self.status = None  # статус игры, True - игрок выиграл, False - Игрок проиграл, None - Игра продолжается
#
#     # ---------------------------------------------------------------------
#     def new_pack(self, deck_count, jokers_enabled=False):
#         txtJoker = "&jokers_enabled=true" if jokers_enabled else ""
#         response = requests.get(f"https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count={deck_count}"+txtJoker)
#         # создание стопки карт из "deck_count" колод по 52 карты
#         if response.status_code != 200:
#             return None
#         pack_card = response.json()
#         return pack_card
#
#     # ---------------------------------------------------------------------
#     def get_cards(self, card_count=1):
#         if self.pack_card == None:
#             return None
#         if self.status != None:  # игра закончена
#             return None
#
#         deck_id = self.pack_card["deck_id"]
#         response = requests.get(f"https://deckofcardsapi.com/api/deck/{deck_id}/draw/?count={card_count}")
#         # достать из deck_id-колоды card_count-карт
#         if response.status_code != 200:
#             return False
#
#         new_cards = response.json()
#         if new_cards["success"] != True:
#             return False
#         self.remaining = new_cards["remaining"]  # обновим в классе количество оставшихся карт в колоде
#
#         arr_newCards = []
#         for card in new_cards["cards"]:
#             card_obj = Card(card)  # создаем объекты класса Card и добавляем их в список карт у игрока
#             arr_newCards.append(card_obj)
#             self.card_in_game.append(card_obj)
#             self.score = self.score + card_obj.cost
#             self.arr_cards_URL.append(card["image"])
#
#         if self.score > 21:
#             self.status = False
#             text_game = "Очков: " + str(self.score) + " ВЫ ПРОИГРАЛИ!"
#
#         elif self.score == 21:
#             self.status = True
#             text_game = "ВЫ ВЫИГРАЛИ!"
#         else:
#             self.status = None
#             text_game = "Очков: " + str(self.score) + " в колоде осталось карт: " + str(self.remaining)
#
#         return text_game


# -----------------------------------------------------------------------
class GameRPS:
    values = ["Камень", "Ножницы", "Бумага"]

    def __init__(self):
        self.computerChoice = self.__class__.getRandomChoice()

    def newGame(self):
        self.computerChoice = self.__class__.getRandomChoice()

    @classmethod
    def getRandomChoice(cls):
        import random

        lenValues = len(cls.values)
        rndInd = random.randint(0, lenValues-1)
        return cls.values[rndInd]

    def playerChoice(self, player1Choice):
        winner = None

        code = player1Choice[0] + self.computerChoice[0]
        if player1Choice == self.computerChoice:
            winner = "Ничья!"
        elif code == "КН" or code == "БК" or code == "НБ":
            winner = "Игрок выиграл!"
        else:
            winner = "Компьютер выиграл!"

        return f"{player1Choice} vs {self.computerChoice} => " + winner


# -----------------------------------------------------------------------
class gameTicTacToe:
    fields = {}

    @classmethod
    def __init__(cls, chat_id, message_id):
        field = [0 for i in range(9)]

        cls.fields[str(chat_id) + '_' + str(message_id)] = field

    @classmethod
    def newGame(cls, chat_id, message_id):
        field = [0 for i in range(9)]

        cls.fields[str(chat_id) + '_' + str(message_id)] = field

    @classmethod
    def getField(cls, chat_id, message_id):
        return cls.fields[str(chat_id) + '_' + str(message_id)]

    @classmethod
    def computerChoice(cls, chat_id, message_id):
        import random

        field = cls.fields[str(chat_id) + '_' + str(message_id)]

        x = random.randint(0, 2)
        y = random.randint(0, 2)

        while field[x + 3 * y] != 0:
            x = random.randint(0, 2)
            y = random.randint(0, 2)

        # Ход компьютера
        field[x + y * 3] = 2

        cls.fields[str(chat_id) + '_' + str(message_id)] = field

    @classmethod
    def gameEndCheck(cls, chat_id, message_id):
        # Проверка на пообеду крестиков
        if cls.winnerCheck(chat_id, message_id, 1):
            return 1

        # Проверка на пообеду ноликов
        elif cls.winnerCheck(chat_id, message_id, 2):
            return 2

        # Проверка на ничью
        elif 0 not in cls.fields[str(chat_id) + '_' + str(message_id)]:
            return 3

        # Игра не завершена
        return 0

    @classmethod
    def winnerCheck(cls, chat_id, message_id, winner_check):
        field = cls.fields[str(chat_id) + '_' + str(message_id)]

        cond_list = []

        # Проверка заполнены ли строки одинаковыми символами
        for i in range(3):
            cond_list.append(field[0 + 3 * i:3 + 3 * i].count(winner_check) == 3)

        # Проверка заполнены ли столбцы одинаковыми символами
        for i in range(3):
            cond_list.append([field[0 + i], field[3 + i], field[6 + i]].count(winner_check) == 3)

        # Проверка заполнены ли диагонали одинаковыми символами
        cond_list.append([field[0], field[4], field[8]].count(winner_check) == 3)
        cond_list.append([field[2], field[4], field[6]].count(winner_check) == 3)

        return True in cond_list

    @classmethod
    def playerChoice(cls, chat_id, message_id, field_number):
        cls.fields[str(chat_id) + '_' + str(message_id)][field_number] = 1


# -----------------------------------------------------------------------
if __name__ == "__main__":
    print("Этот код должен использоваться ТОЛЬКО в качестве модуля!")