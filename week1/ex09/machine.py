# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    machine.py                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: francesco <francesco@student.42.fr>        +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/05/19 20:03:46 by francesco         #+#    #+#              #
#    Updated: 2022/05/19 21:17:48 by francesco        ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from beverages import *
from typing import Union
import random

class CoffeeMachine:
    life = 10
    def __init__(self) -> None:
        pass
    class EmptyCup(HotBeverage):
        def __init__(self) -> None:
            self._price = 0.90
            self._name = "empty cup"
        def description(self) -> str:
            return "An empty cup?! Gimme my money back!"
    class BrokenMachineException(Exception):
        def __init__(self) -> None:
            super().__init__("This coffee machine has to be repaired.")
    def serve(self, beverage) -> Union[object, BrokenMachineException ]:
        if (self.life > 0):
            tuple = (self.EmptyCup, beverage)
            self.life -= 1
            return random.choice(tuple)()
        else:
            raise self.BrokenMachineException()
    def repair(self) -> None:
        self.life = 10
            

try:
    coffee_Mac = CoffeeMachine()
    print(coffee_Mac.serve(Coffee))
    print(coffee_Mac.serve(Tea))
    print(coffee_Mac.serve(Coffee))
    print(coffee_Mac.serve(Coffee))
    print(coffee_Mac.serve(Coffee))
    print(coffee_Mac.serve(Cappuccino))
    print(coffee_Mac.serve(Coffee))
    print(coffee_Mac.serve(Coffee))
    print(coffee_Mac.serve(Chocolate))
    print(coffee_Mac.serve(Coffee))
    print(coffee_Mac.serve(Coffee))
    print(coffee_Mac.serve(Cappuccino))
    print(coffee_Mac.serve(Coffee))
    print(coffee_Mac.serve(Coffee))
    print(coffee_Mac.serve(Tea))
    print(coffee_Mac.serve(Coffee))
    print(coffee_Mac.serve(Coffee))

except Exception as e:
    # print(e)
    coffee_Mac.repair()
    try:
        print("---------->REPAIRED")
        print(coffee_Mac.serve(Chocolate))
        print(coffee_Mac.serve(Coffee))
        print(coffee_Mac.serve(Coffee))
        print(coffee_Mac.serve(Cappuccino))
        print(coffee_Mac.serve(Coffee))
        print(coffee_Mac.serve(Coffee))
        print(coffee_Mac.serve(Tea))
        print(coffee_Mac.serve(Coffee))
        print(coffee_Mac.serve(Coffee))
        print(coffee_Mac.serve(Cappuccino))
        print(coffee_Mac.serve(Coffee))
        print(coffee_Mac.serve(Coffee))
        print(coffee_Mac.serve(Tea))
        print(coffee_Mac.serve(Coffee))
        print(coffee_Mac.serve(Coffee))

    except Exception as e:
    # print(e)
        coffee_Mac.repair()
        print("---------->REPAIRED")
        print(coffee_Mac.serve(Chocolate))
        print(coffee_Mac.serve(Coffee))
        print(coffee_Mac.serve(Coffee))
        print(coffee_Mac.serve(Cappuccino))
        print(coffee_Mac.serve(Coffee))
        print(coffee_Mac.serve(Coffee))
        print(coffee_Mac.serve(Tea))
        print(coffee_Mac.serve(Coffee))
        print(coffee_Mac.serve(Coffee))