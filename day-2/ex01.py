from collections import Counter
from itertools import combinations
class Game(object):

    def __init__(self, matches=10):
        self.matches = matches
        self.bank_p1 = Counter({'candy': 0})
        self.bank_p2 = Counter({'candy': 0})
        self.steps_p1 = []  # Список для шагов первого игрока
        self.steps_p2 = []  # Список для шагов второго игрока

    def play(self, player1, player2):
        
        self.player1 = player1
        self.player2 = player2

        while self.matches != 0 :
            print(f' матч -{self.matches}')
            move_p1 = bool(player1)
            move_p2 = bool(player2)

            if move_p1 and move_p2:
                self.bank_p1['candy'] += 2
                self.bank_p2['candy'] += 2
                self.steps_p1.append('cooperate')  # Записываем шаг
                self.steps_p2.append('cooperate')  # Записываем шаг
                self.matches -= 1

            elif not move_p1 and not move_p2:
                self.steps_p1.append('cheat')  # Записываем шаг
                self.steps_p2.append('cheat')  # Записываем шаг
                self.matches -= 1

            elif not move_p1 and move_p2:
                self.bank_p1['candy'] += 3
                self.bank_p2['candy'] -= 1
                self.steps_p1.append('cheat')  # Записываем шаг
                self.steps_p2.append('cooperate')  # Записываем шаг
                self.matches -= 1
                # if self.bank_p2['candy'] < 0:
                #     self.bank_p2['candy'] += 1
                #     break

            elif move_p1 and not move_p2:
                self.bank_p1['candy'] -= 1
                self.bank_p2['candy'] += 3
                self.steps_p1.append('cooperate')  # Записываем шаг
                self.steps_p2.append('cheat')  # Записываем шаг
                self.matches -= 1
                # if self.bank_p1['candy'] < 0:
                #     self.bank_p1['candy'] += 1
                #     break

            if isinstance(player1, Copycat_Pl):
                player1.play(move_p2)
            if isinstance(player2, Copycat_Pl):
                player2.play(move_p1)
            
            if isinstance(player1, Grudeger_Pl):
                if  'cheat' in self.steps_p2:
                    # move_p1 = False
                    player1.play(move_p2)
                else:
                    player1.play(move_p2)
                    # move_p1 = True

            if isinstance(player2, Grudeger_Pl):
                if  'cheat' in self.steps_p1:
                    # move_p2 = False
                    player2.play(move_p1)    
                else:
                    player2.play(move_p1)


            if isinstance(player1, Two_True_False):
                if(self.matches % 2 == 0):
                    
                    move_p1 = False
                    # print(f"{move_p1}")
                    player1.play(move_p1)
                else:
                    move_p1 = True
                    # print(f"{move_p1}")
                    player1.play(move_p1)

            if isinstance(player2, Two_True_False):
                if(self.matches % 2 == 0):
                    
                    move_p2 = False
                    # print(f"{move_p1}")
                    player2.play(move_p2)
                else:
                    move_p2 = True
                    # print(f"{move_p1}")
                    player2.play(move_p2)
                    
            if isinstance(player1, Detective_PL):
                print("шаг 1")
                if self.matches == 9:
                    print("шаг 2")
                    # move_p1 = False
                    player1.play(move_p1)
                if self.matches == 8:
                    print("шаг 3")
                    player1.play(move_p1)

                if self.matches <= 7:
                    print("шаг 4")
                    if 'cheat' in self.steps_p2[0:4]:
                        print("шаг 4 -  должен быть copycat")
                        player1.play(move_p2)
                        
                    else:
                        print("шаг 4 -  должен быть citer")
                        # move_p1 = False
                        player1.play(move_p1)
                        # move_p2 = bool
    
    def viner(self):
        if(self.bank_p1['candy'] > self.bank_p2['candy']):
            return 'Выграл первый игрок'
        if(self.bank_p1['candy'] < self.bank_p2['candy']):
            return 'Выграл второй игрок'

        if(self.bank_p1['candy'] == self.bank_p2['candy']):
            return 'Ничья'

    def show_steps(self):
        print(f"Шаги первого игрока: {self.steps_p1}")
        print(f"Шаги второго игрока: {self.steps_p2}")

    def top3(self):
    
        for i  in self.bank_p1.items():
            print(i,  end=' ',)
        for  j in self.bank_p2.items():
            print(j,  end=' ')
    
class Player:
    def chit(self):
        return False

    def cooperate(self):
        return True

class Cheater_Pl(Player):
    def __init__(self):
        self.name = 'Cheater'
        super().__init__()
        self.player = self.chit()

    def __bool__(self):

        return  self.player

class Cooperator_Pl(Player):
    def __init__(self):
        self.name = 'Cooperator_Pl'
        super().__init__()
        self.player = self.cooperate()

    def __bool__(self):

        return self.player
        
        
class Copycat_Pl(Player):
    def __init__(self):
        self.name = 'Copycat_Pl'
        super().__init__()
        self.player = self.cooperate()  # Начинаем с сотрудничества

    def play(self, opponent_move):
        print( f'ход соперника {opponent_move}')
        self.player = opponent_move  # Запоминаем последний ход оппонента

    def __bool__(self):
        return self.player
    
class Grudeger_Pl(Player):

    def __init__(self):
        self.name = 'Grudeger_Pl'
        super().__init__()
        self.player = True
        self.bank = []

    def play(self, opponent_move):

        self.opponent_move = opponent_move
        self.bank.append(self.opponent_move)
        # print(f' ход соперника {opponent_move}')
        if False in self.bank:
            print(f' ход соперника {opponent_move}')
            self.player = False
        if False not in self.bank:
            self.player = True
            print(f' ход соперника {opponent_move}')

    def __bool__(self):
        return self.player
    
class Two_True_False(Player):
    def __init__(self):
        self.name = 'Two_True_False'
        super().__init__()
        self.player = True
        self.two_count = 0
    
    def play(self, opponent_move):
        
        if(self.two_count % 2 == 0):
            self.player = False
        else:
            self.player = True
        self.two_count+=1

    def __bool__(self):
        return self.player

class Detective_PL(Player):
    def __init__(self):
        self.name = 'Detective_PL'
        super().__init__()
        self.player = True
        self.count = 0
        self.bank = []

    def play(self, opponent_move):
        self.opponent_move = opponent_move
        self.bank.append(self.opponent_move)
        
        if self.count == 0:
            self.player = self.chit()
            self.count += 1
            print(f' count = {self.count} ход соперника {self.opponent_move}')
        
        elif self.count == 1:
            self.player = self.cooperate()
            self.count += 1
            print(f'count = {self.count} ход соперника {self.opponent_move}')
        
        elif self.count == 2:
            self.player = self.cooperate()
            self.count += 1
            print(f'count = {self.count} ход соперника {self.opponent_move}')
        
        elif self.count >= 3:
            print(f'count == {self.count} ход соперника {self.opponent_move}')
            if False in  self.bank[0:4]:
                self.player = self.opponent_move
                print(f'Detectiv - copycat {self.opponent_move}')
              
            else:
                self.player = self.chit()
                print("Detectiv - cheater")

    def hod(self):
        return self.bank
 
    def __bool__(self):
        return self.player
chit = Cheater_Pl()
company = Cooperator_Pl()
copycat = Copycat_Pl()
# grudeger = Grudeger_Pl()
# detective = Detective_PL()
# # two_true_false = Two_True_False()
play = Game()
play.play(chit, company)

# # print(f"Ходы детектива -- {grudeger.bank}")
# # print(f"Ходы злопамятного--{detective.bank}")

# play.play(chit, company)
# play.viner()

play.show_steps()
play.top3()
play.play(chit, copycat) 
play.top3()

# Создаем игроков
# players = [
#     Cheater_Pl(),
#     Cooperator_Pl(),
#     Copycat_Pl(),
#     Grudeger_Pl(),
#     Detective_PL(),
#     Two_True_False()
# ]

# # Словарь для хранения результатов
# results = {player.name: Counter({'candy': 0}) for player in players}

# # Организуем турнир
# for player1, player2 in combinations(players, 2):
#     game = Game()
#     game.play(player1, player2)
#     results[player1.name]['candy'] += game.bank_p1['candy']
#     results[player2.name]['candy'] += game.bank_p2['candy']

# # Сортируем результаты и выводим топ-3 игроков
# sorted_results = sorted(results.items(), key=lambda x: x[1]['candy'], reverse=True)
# top3_results = sorted_results[:]

# print("Топ-3 игроков:")
# for name, score in top3_results:
#     print(f"{name}: {score['candy']} конфет")