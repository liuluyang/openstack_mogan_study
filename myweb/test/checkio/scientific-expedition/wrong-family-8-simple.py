#coding:utf8

import copy
def is_family(tree):

    father = set([i for y in tree for i in y])-set([i[1] for i in tree])
    if len(father)!=1:
        return False
    checked = list(father)
    fathers = list(father)
    n , _len = 0, len(tree)
    while tree:
        tree_copy = copy.deepcopy(tree)
        fs = []
        #逻辑问题
        for f in fathers:
            for link in tree_copy:
                if f==link[0]:
                    if link[1] in fs+checked:
                        return False
                    if f!=link[1]:
                        fs.append(link[1])
                        tree.remove(link)
                    else:
                        return False
        if tree==tree_copy:
            return False
        fathers = fs
        checked.extend(fathers)

    return True



print is_family([
      ['Logan', 'Mike'],
      ['Logan', 'Jack'],
      ['Mike', 'Alexander']
    ])

print is_family([["Logan","Mike"],["Alexander","Jack"],["Jack","Alexander"]]) #出现了无限循环

# if __name__ == "__main__":
#     #These "asserts" using only for self-checking and not necessary for auto-testing
#     assert is_family([
#       ['Logan', 'Mike']
#     ]) == True, 'One father, one son'
#     assert is_family([
#       ['Logan', 'Mike'],
#       ['Logan', 'Jack']
#     ]) == True, 'Two sons'
#     assert is_family([
#       ['Logan', 'Mike'],
#       ['Logan', 'Jack'],
#       ['Mike', 'Alexander']
#     ]) == True, 'Grandfather'
#     assert is_family([
#       ['Logan', 'Mike'],
#       ['Logan', 'Jack'],
#       ['Mike', 'Logan']
#     ]) == False, 'Can you be a father for your father?'
#     assert is_family([
#       ['Logan', 'Mike'],
#       ['Logan', 'Jack'],
#       ['Mike', 'Jack']
#     ]) == False, 'Can you be a father for your brather?'
#     assert is_family([
#       ['Logan', 'William'],
#       ['Logan', 'Jack'],
#       ['Mike', 'Alexander']
#     ]) == False, 'Looks like Mike is stranger in Logan\'s family'
#     print("Looks like you know everything. It is time for 'Check'!")
