# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    print_sum.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: fulloa-s <fulloa-s@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/05/18 10:06:19 by fulloa-s          #+#    #+#              #
#    Updated: 2022/05/18 11:24:56 by fulloa-s         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys


if (len(sys.argv) != 3):
    raise Exception("Error with the number of arguments")
try: 
    x = (float(sys.argv[1]))
    y = (float(sys.argv[2]))
    if((x + y).is_integer()):
        print(int(x + y))
    else:
        print(x + y)
except:
    print("Please insert numbers")
    sys.exit(1)