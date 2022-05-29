# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    print_secs.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: fulloa-s <fulloa-s@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/05/18 10:59:58 by fulloa-s          #+#    #+#              #
#    Updated: 2022/05/18 11:31:00 by fulloa-s         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

if (len(sys.argv) != 4):
    raise Exception("Error with the number of arguments")
try:
    print(int(sys.argv[3]) + int(sys.argv[2]) * 60 + (int(sys.argv[1]) * 60) * 60)
except:
    print("PARSING ERROR, time format (24)HH MM SS")
