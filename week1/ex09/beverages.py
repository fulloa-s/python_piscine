# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    beverages.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: francesco <francesco@student.42.fr>        +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/05/19 10:54:41 by fulloa-s          #+#    #+#              #
#    Updated: 2022/05/19 20:44:02 by francesco        ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class HotBeverage:
    _price = 0.30
    _name = "hot beverage"
    def __init__(self) -> None:
        pass
    def description(self) -> str:
        return "Just some hot water in a cup."
    def __str__(self) -> str:
        return "name : " + self._name + "\n" + "price : " + str("{:.2f}".format(self._price)) + "\n" + "description : " + self.description()


class Coffee(HotBeverage):
    def __init__(self) -> None:
        self._price = 0.40
        self._name = "coffee"
    def description(self) -> str:
        return "A coffee, to stay awake."

class Tea(HotBeverage):
    def __init__(self) -> None:
        self._price = 0.30
        self._name = "tea"

class Chocolate(HotBeverage):
    def __init__(self) -> None:
        self._price = 0.40
        self._name = "chocolate"
    def description(self) -> str:
        return "Chocolate, sweet chocolate..."

class Cappuccino(HotBeverage):
    def __init__(self) -> None:
        self._price = 0.45
        self._name = "cappuccino"
    def description(self) -> str:
        return "Un po' di Italia nella sua tazza!"


def main():
    print(HotBeverage())
    print(Coffee())
    print(Tea())
    print(Chocolate())
    print(Cappuccino())

if __name__ == "__main__":
    main()