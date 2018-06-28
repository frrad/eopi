from binary_tree import BinaryTree 

def reconstruct_tree(IO, PO):
    node = BinaryTree()
    node.data = PO[0]
    LIO, RIO = [], []
    i += 1
    while IO[i] != PO[0]:
        LIO.append(IO[i])
        i += 1
    RIO = IO[i+1:]
    LPO = PO[1:i+1]
    RPO = PO[i+1:]
    node.left = reconstruct_tree(LIO, LPO)
    node.right = reconstruct_tree(RIO, RPO)

    return node
