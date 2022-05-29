# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    my_sort.py                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: fulloa-s <fulloa-s@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/05/18 14:35:05 by fulloa-s          #+#    #+#              #
#    Updated: 2022/05/19 10:02:30 by fulloa-s         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

d={
'Hendrix' : '1942', 
'Allman' : '1946', 
'King' : '1925', 
'Clapton' : '1945', 
'Johnson' : '1911', 
'Berry' : '1926', 
'Vaughan' : '1954', 
'Cooder' : '1947', 
'Page' : '1944', 
'Richards' : '1943', 
'Hammett' : '1962', 
'Cobain' : '1967', 
'Garcia' : '1942', 
'Beck' : '1944', 
'Santana' : '1947', 
'Ramone' : '1948', 
'White' : '1975', 
'Frusciante': '1970', 
'Thompson' : '1949', 
'Burton' : '1939',
}

alphabetSortList = sorted(d.items(), key=lambda _tuple: _tuple[0])
yearSortList = sorted(alphabetSortList, key=lambda _tuple: _tuple[1])
for musicians in yearSortList:
    print(musicians[0])
 

    