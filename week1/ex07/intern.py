# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    intern.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: fulloa-s <fulloa-s@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/05/19 10:09:48 by fulloa-s          #+#    #+#              #
#    Updated: 2022/05/19 10:51:56 by fulloa-s         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

class Intern:
    class Coffee:
        def __init__(self) -> None:
            pass
        def __str__(self) -> str:
            return ("This is the worst coffee you ever tasted.")    
    def __init__(self, name="My name? I’m nobody, an intern, I have no name."):
        self.__name = name
    def __str__(self):
        return self.__name
    def work(self) -> Exception:
        raise Exception("I’m just an intern, I can’t do that...")
    def make_coffee(self) -> Coffee:
        return self.Coffee()


try:
    mr_nobody = Intern()
    print(mr_nobody)
    mark = Intern("Mark")
    print(mark)
    print(mark.make_coffee())
    mr_nobody.work()
except Exception as e:
    print(e)
