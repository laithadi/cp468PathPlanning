class Node:
    """
    Node class to is to help us keep track of a coordinates index, parent (previous move or coordinate),
    g(n), h(n), and the cost f(n) = g(n) + h(n).
    """

    def __init__(self, index, parent, g_score, h_score):
        self.index = index
        self.parent = parent
        self.g_score = g_score
        self.h_score = h_score
        self.cost = h_score + g_score 

