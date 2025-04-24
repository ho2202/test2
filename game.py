import random

cardlist = ("marine", "zergling", "scv")
cardlist_key = {1:["마린", 40, 20, 0], 2:["저글링", 20, 20, 0], 3:["scv", 60, 10, 10], 4:["spell1",60, 1, 10], 5:["stone", 60, 0, 10], 6:["duck", 40, 20, 0]}

class skill:
  def __init__(self, name, energy_cost, effect):
    """이름, 사용 마나, 체력 변화량"""
    self.name = name
    self.energy_cost = energy_cost
    self.effect = effect
  def activate(self, target):
    target.take_damage(self.effect)

class card:
    """Card number, Card type, location"""
    def __init__(self, no, location: int):
        self.no = no        # 카드 유형 0:유닛, 1:마법, 2:환경
        # 카드 속성 0:기본, 1:불, 2:물, 3:전기, 4:금속
        self.location = location  # 카드 위치 0:묘지, 1:덱, 2:패, 3-7:필드


class unit(card):
    """카드 번호, 속성, 지역, 체력, 공격력, 방어력
     속성 0:기본, 1:불, 2:물, 3:전기, 4:금속
     카드 위치 0:묘지, 1:덱, 2:패, 3-7:필드"""
    # def __init__(self, no: int, Ctype: int, location: int, hp: int, att, defense):
    #     super().__init__(no, Ctype, location)
    #     self.hp = hp
    #     self.att = att
    #     self.defense = defense

    def __init__(self, no, Ctype: int, location: int):
        super().__init__(no, location)
        self.hp = cardlist_key[no][1]
        self.att = cardlist_key[no][2]
        self.defense = cardlist_key[no][3]

    def use_skill(skill_name, target):
        pass

    def take_damage(self, damage):
        self.hp -= damage
        if(lang == 1):
          print(f"{cardlist_key[self.no][0]} 가 {damage} 데미지 입어서 체력이 {self.hp} 남음")
        elif (lang == 2):
          print(f"{cardlist_key[self.no][0]} took {damage} damage! hit point is {self.hp} left.")

    def is_alive(self):
        return self.hp > 0

class spell(card):
    def __init__(self, no, Ctype, location):
        super().__init__(no, Ctype, location)

    def use():
        return 0


class envir(card):
    """카드 위치 0:묘지, 1:덱, 2:패, 3-7:필드"""
    def __init__(self, no, Ctype, location):
        super().__init__(no, Ctype, location)

    def attack(self, no, unit, damage):
        damage = self.take_damage()
        unit.hp -= damage
        if(lang == 1):
          print(f"{cardlist_key[no][0]}가  {cardlist[unit.no]}에게 {damage} 데미지를 입혔다!")
        elif (lang == 2):
          print(f"{cardlist_key[no][0]} caused {damage} damage to {cardlist[unit.no]} !")


class Player:
    """플레이어 이름, 덱"""
    def __init__(self, name, deck: Deck):
        self.name = name
        self.hand = Deck(no, 2)
        self.field = Deck(no, 3)
        self.deck = deck
        self.g = []

    def draw_card_to_hand(self):
        card = self.deck.draw_card()
        if card is not None:
          self.hand.insert(random.randint(1, self.deck.deckSize), card)

    def field_card(self):
        card = self.deck.draw_card()
        if card is not None:
          self.hand.insert(random.randint(1, self.deck.deckSize), card)

    def play_card(self, card_index):
        # 카드를 필드에 내는 로직 구현
        pass


class CombatManager():
  def attack(attacker, defender : unit):
    a_name = cardlist_key[attacker.no][0]
    d_name = cardlist_key[defender.no][0]
    # 죽어있고 필드에 없다면
    if (not defender.is_alive and defender.location < 2):
      if(lang == 1):
        print(f"{d_name} 는 이미 처치함!")
      elif (lang == 2):
        print(f"{d_name} is already defeated!")

    else:
      # 살아있고 필드에 있다면
      base_damage = attacker.att - defender.defense
      if( lang == 1):
        print(f"{a_name}가 {d_name}에게 {base_damage} 데미지를 입혔다!")
      elif (lang == 2):
        print(f"{a_name} attacked {d_name}, causing damage!")

      defender.take_damage(attacker.att)
      print(f"{d_name}의 체력이 {defender.hp} 남았다")

      # if (defender.is_alive()):
      #   if(lang == 1):
      #     print(f"{d_name}의 체력이 {defender.hp} 남았다")
      #   elif (lang == 2):
      #     print(f"{d_name}'s Hp is {defender.hp} left")
      # else:
      #   if(lang == 1):
      #     print(f"{d_name} 가 처치됨!")
      #   elif (lang == 2):
      #     print(f"{d_name} is defeated!")

      defender.location = 0
    return attacker, defender


  def achieveManager():
    #업적 구현
    pass

class cardGame(CombatManager, Deck):
    """game object"""
    text = ["Setting the game", "Starting a New game.", "is already defeated!"]
    textKor = ["게임 세팅", "새로운 게임을 시작합니다.", "는 이미 처치함!"]
    def __init__(self):

        game_speed = 0.1

    def start_game(self):
        Run = True
        combat_manager = CombatManager()
        if(lang == 1):
          print(self.textKor[1])
        elif (lang == 0):
          print(self.text[1])
        grave = 0
        p1deck = Deck("p1", 1, "unit")
        p2deck = Deck("p2", 2, "abc")

    def stop_game():
        '''게임을 종료합니다.'''
        if(lang == 1):
          print("게임을 종료합니다.")
        elif (lang == 0):
          print("The game is close.")
        Run = False

    def play_turn(self):
        # 턴 진행 로직 구현
        pass

    def check_game_over(self):
        # 게임 종료 조건 판단 로직 구현
        pass

lang = 1
if (lang == 2):
  print("English")
else:
  print("한국어")

game1 = cardGame()

player1 = Player("Player1", Deck(1, 1, 'a'))
player2 = Player("Player2", Deck(2, 1, 'b'))

player1.hand.use_card()
card1 = player1.field.add_card(unit(1, 0, 1))
card2 = player2.field.add_card(unit(2, 0, 'b'))


# 순서 정하기
first = [player1, player2]
random.shuffle(first)

# while first[0].field[0] != 0 and first[1].location != 0:
#   if first[0].is_alive(): # 선공 공격
#     CombatManager.attack(first[0], first[1])
#   if first[1].is_alive(): # 후공 공격
#     CombatManager.attack(first[1], first[0])


#enviroment = envir(1, 1, 1)
# print("death unit:")
game1.stop_game
