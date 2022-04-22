def get_row(k):
    row = []
    for x in range(0, k):
        row = [1 if y == 0 or y == x else row[y - 1] + row[y]
               for y in range(0, x + 1)]
    return row


print(get_row(10))
