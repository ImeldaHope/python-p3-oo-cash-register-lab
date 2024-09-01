#!/usr/bin/env python3

class CashRegister:
  def __init__(self, discount = 0):
    self.discount = discount
    self.total = 0
    self.items = []

  @property
  def discount(self):
    return self._discount
  
  @discount.setter
  def discount(self, discount):
    if isinstance(discount, int):
      self._discount = discount
  
  @property
  def total(self):
    return self._total
  
  @total.setter
  def total(self, total):
    total = float(total)
    if isinstance(total, float):
      self._total = total

  @property
  def items(self):
    return self._items
  
  @items.setter
  def items(self, items):
    self._items = items

  def apply_discount(self):
    if self.discount > 0 :
      discount_amount = (self.discount / 100) * self.total
      self.total -= discount_amount      
      tots = int(self.total)
      print(f"After the discount, the total comes to ${tots}.")
    else:
      print("There is no discount to apply.")
     
  def add_item(self, title, price, quantity = 0):
    self.title = title
    self.price = price
    self.quantity = quantity

    if quantity > 0:
      self.total += (self.price * quantity)

      for _ in range(quantity):
        self.items.append(title)
    else:
      self.total += self.price
      self.items.append(title)

  def void_last_transaction(self):
    if self.items:
      if self.quantity> 0:
        self.total -= (self.price * self.quantity)
        for _ in range(self.quantity):
          self.items.pop()
      else:
        self.items.pop()    
        self.total -= self.price 
    

  

