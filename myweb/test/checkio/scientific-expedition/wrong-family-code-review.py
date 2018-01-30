#coding:utf8

def is_family(tree):
    family_tree = {}
    for father, son in tree:
        if son == father:
            return False
        if son in family_tree:
            return False
        if father in family_tree and family_tree[father] == son:
            return False
        family_tree[son] = father
    fathers = set(family_tree.values())
    for father in family_tree.values():
        if father in family_tree:
            fathers.discard(father)
    return len(fathers) == 1