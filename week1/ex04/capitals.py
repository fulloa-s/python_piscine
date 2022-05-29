# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    capitals.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: fulloa-s <fulloa-s@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/05/18 13:07:08 by fulloa-s          #+#    #+#              #
#    Updated: 2022/05/18 13:18:56 by fulloa-s         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

states = {
"Oregon" : "OR",
"Alabama" : "AL",
"New Jersey": "NJ",
"Colorado" : "CO"
}
capital_cities = {
"OR": "Salem",
"AL": "Montgomery",
"NJ": "Trenton",
"CO": "Denver"
}

try:
    if (len(sys.argv) != 2):
        raise Exception
    if (states.get(sys.argv[1])):
        print(capital_cities.get(states.get(sys.argv[1])))
    else:
        print("Unknown state")
except:
    sys.exit(1)