#coding:utf8

def checkio(pawns):
    pawns_indexes = set()
    for p in pawns:
        row = int(p[1]) - 1
        col = ord(p[0]) - 97
        pawns_indexes.add((row, col))
    print pawns_indexes
    count = 0
    for row, col in pawns_indexes:
        is_safe = ((row - 1, col - 1) in pawns_indexes) or ((row - 1, col + 1) in pawns_indexes)
        if is_safe:
            count += 1
    return count

print checkio({"b4", "d4", "f4", "c3", "e3", "g5", "d2"})
print checkio({"b4", "c4", "d4", "e4", "f4", "g4", "e5"})