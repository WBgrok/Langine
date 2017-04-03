import random


class controller(object):

  def __init__(self):
    self.words = dict()

  def add(self, word):
    self.words.update({word.key: word})

  def get(self, key):
    if key[0] == '$':
      key2 = key[1:]
      if key2 in self.words:
        return self.words[key2].generate()
    return key


class phrase(object):

  def __init__(self, key, controller, items=list()):
    self.key = key
    self.controller = controller
    self.items = items
    self.total_weight = sum(weight for (item, weight) in self.items)
    controller.add(self)

  def add(self, item, weight):
    self.items.append((item, weight))
    self.total_weight = sum(weight for (item, weight) in self.items)

  def generate(self):
    return' '.join(map(self.controller.get, self.draw().split()))

  def draw(self):
    r = random.uniform(0, self.total_weight)
    tally = 0
    for item, weight in self.items:
      if tally + weight >= r:
        return item
      tally += weight
