classes = ["astronomy", "calculus", "french", "history", "literature", "organic chemistry", "physics"]
"""
The strategy: Have the initial order as the the first four alphabetical books. Then, sequentially replace the last
book in the order with the next textbook in the overall list. Then, shift the second to last book down one, and
iterate through the last one again
"""
count = 0
order_list = []
order = ["astronomy", "calculus", "french", "history"]
for book1 in classes:
    for book2 in classes:
        if book2 > book1:
            for book3 in classes:
                if book3 > book1 and book3 > book2:
                    for book4 in classes:
                        if book4 > book1 and book4 > book2 and book4 > book3:
                            order = [book1, book2, book3, book4]
                            order_list.append(order)

for order in order_list:
    print(order)
print(len(order_list))

repeat_check = order_list.copy()
#print(len(repeat_check))
for i in range(0, len(order_list)):
    for j in range(0, len(repeat_check)):
        #print(i, j)
        if order_list[i] == repeat_check[j] and i != j:
            print("These combinations are not unique.")

 