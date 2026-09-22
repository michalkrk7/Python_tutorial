#list slicing
amazon_cart = [
    'notebook',
    'sunglasses',
    'toys',
    'grapes',
]

amazon_cart[0] = 'laptop' 

new_cart = amazon_cart [:] # creating a copy of the list
new_cart[0] = 'gum' #changing the value of the new_cart list

print(amazon_cart[0:3]) #printing the sliced list
print(amazon_cart)
