class Bts:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def qianxu(tree, array=[]):
    if tree is None:
        return []
    else:
        array.append(tree.val)
        qianxu(tree.left, array)
        qianxu(tree.right, array)
    return array


def zhongxu(tree, array=[]):
    if tree is None:
        return []
    else:
        zhongxu(tree.left, array)
        array.append(tree.val)
        zhongxu(tree.right, array)
    return array


def houxu(tree, array=[]):
    if tree is None:
        return []
    else:
        houxu(tree.left, array)
        houxu(tree.right, array)
        array.append(tree.val)
    return array


root = Bts(10)
root.left = Bts(5)
root.right = Bts(15)
root.left.left = Bts(2)
root.left.right = Bts(6)
print(qianxu(root))
print(zhongxu(root))
print(houxu(root))
