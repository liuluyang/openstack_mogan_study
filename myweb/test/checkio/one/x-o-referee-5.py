#coding:utf8

def checkio(result):
    rows = result
    cols = map(''.join, zip(*rows))
    print list(cols)
    diags = map(''.join, zip(*[(r[i], r[2 - i]) for i, r in enumerate(rows)]))
    print list(diags)
    lines = rows + list(cols) + list(diags)

    return 'X' if ('XXX' in lines) else 'O' if ('OOO' in lines) else 'D'

print checkio(['XX.','XOO','XXO'])