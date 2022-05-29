# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    value_search.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: fulloa-s <fulloa-s@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/05/18 13:07:08 by fulloa-s          #+#    #+#              #
#    Updated: 2022/05/18 14:33:05 by fulloa-s         ###   ########.fr        #
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
    for key, value in capital_cities.items():
        if(value == sys.argv[1]):
            for s_key, s_value in states.items():
                if (key == s_value):
                    print(s_key)
                    sys.exit(0)           
    print("Unknown capital city")
except:
    sys.exit(1)