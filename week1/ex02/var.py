# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    var.py                                             :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: fulloa-s <fulloa-s@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/05/18 11:32:59 by fulloa-s          #+#    #+#              #
#    Updated: 2022/05/18 11:48:27 by fulloa-s         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def my_var(x):
   print(x, "has a type", type(x))

x = 42
my_var(x)
x = str(42)
my_var(x)
x = "quarante-deux"
my_var(x)
x = float(42)
my_var(x)
x = True
my_var(x)
x = [42]
my_var(x)
x = {42: 42}
my_var(x)
x = (42,)
my_var(x)
x = set()
my_var(x)
