print('list methods:')

#adding

basket1 = [1,2,3,4,5]
basket1.append(100)
new_list1 = basket1
print(f'\nappend: {new_list1}')

basket2 = [1,2,3,4,5]
basket2.insert(2, 100)
new_list2 = basket2
print(f'\ninsert: {new_list2}')

basket3 = [1,2,3,4,5]
basket3.extend([100])
new_list3 = basket3
print(f'\nextend: {new_list3}')

#removing

basket4 = [1,2,3,4,5]
basket4.pop() #pops off whatever is at the end of the list
new_list4 = basket4
print(f'\npop(): {new_list4}')

basket5 = [1,2,3,4,5]
basket5.pop(0) #removes the index
new_list5 = basket5
print(f'\npop(index): {new_list5}')

basket6 = [1,2,3,4,5]
basket6.remove(4) #value to remove
new_list6 = basket6
print(f'\nremove: {new_list6}')

basket7 = [1,2,3,4,5]
new_list7 = basket7.clear() #clears the "basket"
print(f'\nclear: {basket7}')

basket8 = ['a','b','c','d','e']
print(f'\n index: {basket8.index('d')}') #mowi na którym miejscu (indexie) (pamietaj indexy liczymy od 0: 0,1,2,3,4,5)

basket9 = ['a','b','c','d','e'] #sprawdzanie czy w liście jest dany element i ile razy występuje (może też być z liczbami)
print(f'\n in: {'i' in basket9}') 

basket10 = ['a','b','c','d','e']
print(f'\n count: {basket10.count('d')}') #ile razy występuje dany element w liście

basket11 = ['b','d','a','c','e']
# basket11.sort()
# print(f'\n sorted: {basket11}') #sortuje listę 
print(f'\n sorted: {sorted(basket11)}') #sortuje listę i tworzy nową posortowaną listę

basket12 = ['a','b','c','d','e']
basket12.reverse()
print(f'\n reverse: {basket12}') #odwraca kolejność elementów w liście
