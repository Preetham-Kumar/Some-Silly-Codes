def draw_bush(start, end):
    for row in range(start, end + 1):
        print ' ' * (end - row),
        print '* ' * row


rows = int(raw_input("Enter number of rows: "))

draw_bush(3, rows)