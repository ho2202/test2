class simpleDeck(unit, spell, envir):
  """플레이어, 번호, 덱_리스트
  1: 덱, 2: 패, 3: 필드"""
  def __init__(self, player: bool, deckNo: int):
      self.player = player
      self.no = no
      self.deckSize = 0
      self.cards = []
      self.deck_size()

  def shuffle_deck(self):
    random.shuffle(self.cards)

  def add_card(self, card):
    self.cards.append(card)
    self.deck_size()

  def deck_size(self):
    self.deckSize = len(self.cards)

  def showDeck(self):
    print("simpleDeck:", self.cards)

class Deck(simpleDeck)
    def __init__(self, player: bool, deckNo: int, deckL: str):
      super().__init__(player, deckNo)
      self.deckL = deckL
      if deckL == 'a':
        self.cards.append(unit(1, 0, 1))
      elif deckL == 'b':
        self.cards.append(unit(2, 0, 1))
      pass
    def draw_card(self):
      if self.cards:
          return self.cards.pop()
      else:
          print("덱에 카드가 없다")
          return None

  def showDeck(self):
    print("deck:", self.cards)


class Deck_hand(simpleDeck)
    def __init__(self, player: bool):
      super().__init__(player)
      self.hand = []

    def use_card(self, index :int):
      return self.hand.pop(index)

    def draw_card(self, card: card):
      if card is not None:
          self.hand.appand(card)

class Deck_field(simpleDeck)
    def __init__(self, player: bool):
      super().__init__(player)
      self.field = []

    def remove_card(self):
      return self.field.pop()

    def use_card(self, card: card, no: int):
      """카드, 카드를 놓을 위치"""
      if card is not None:
          self.field.insert(no, card)
