import numpy
import random
from itertools import chain
from threading import Lock

def softmax(x):
    """Compute softmax values for each sets of scores in x."""
    return numpy.exp(x) / numpy.sum(numpy.exp(x), axis=0)


class GameState(object):
    """ A state of the game, i.e. the game board. These are the only functions which are
        absolutely necessary to implement UCT in any 2-player complete information deterministic
        zero-sum game, although they can be enhanced and made quicker, for example by using a
        GetRandomMove() function to generate a random move during rollout.
        By convention the players are numbered 1 and 2.
    """
    def __init__(self):
            self.playerJustMoved = 2 # At the root pretend the player just moved is player 2 - player 1 has the first move

    def clone(self):
        """ Create a deep clone of this game state.
        """
        st = GameState()
        st.playerJustMoved = self.playerJustMoved
        return st

    def do_move(self, move):
        """ Update a state by carrying out the given move.
            Must update playerJustMoved.
        """
        self.playerJustMoved = 3 - self.playerJustMoved

    def get_moves(self):
        """ Get all possible moves from this state.
        """

    def get_result(self, playerjm):
        """ Get the game result from the viewpoint of playerjm.
        """

    def __repr__(self):
        """ Don't need this - but good style.
        """
        pass

    def features(self):
        pass
        # Flatten et de dimension fixe


class Node(object):
    """ A node in the game tree. Note wins is always from the viewpoint of playerJustMoved.
        Crashes if state not specified.
    """
    def __init__(self, parent, state, evaluation, move = None):
        self.move = move # the move that got us to this node - "None" for the root node
        self.childNodes = []
        self.reward = 0
        self.visits = 0
        self.state = state
        self.features = state.features()
        self.untriedMoves = state.get_moves() # future child nodes
        self.playerJustMoved = state.playerJustMoved # the only part of the state that the Node needs later
        self.parentNode = parent

        self.lock = Lock()

        self.evaluation = evaluation

    def next_child(self):
        s = sorted(self.childNodes, key = lambda c: self.evaluation(c, self))[-1]
        return s

    def add_child(self, move, state):
        """ Remove m from untriedMoves and add a new child node for this move.
            Return the added child node
        """
        with self.lock:       
            n = Node(evaluation = self.evaluation, move = move, parent = self, state = state)
            self.untriedMoves.remove(move)
            self.childNodes.append(n)
        return n

    def update(self, reward):
        """ Update this node - one additional visit and result additional wins. result must be from the viewpoint of playerJustmoved.
        """
        with self.lock:
            self.visits +=1
            self.reward += reward

    def root(self):
        return self.move is None


def merge(children, parent=None):
    if parent is None:
        is_root = True
        parent = Node(None, GameState(), None)
    else:
        is_root = False

    move_player = {}
    for node in children:
        k = (node.move, node.playerJustMoved)
        if k not in move_player:
            move_player[k] = []
        move_player[k].append(node)

    ret = []
    for k, v in move_player.items():
        if len(v) == 1:
            continue
        n = Node(parent, v[0].state.clone(), parent.state, move=k[0])
        temp = chain([n.childNodes for n in v])
        temp = [v for w in temp for v in w]
        childs = merge(temp, n)
        n.childNodes = childs
        n.reward += sum([a.reward for a in v])
        n.visits += sum([a.visits for a in v])
        ret.append(n)
    if is_root:
        ret = ret[0]
    return ret

def get_moves(node):
    ret = []
    while node is not None:
        ret.append(node.move)
        node = node.parentNode
    return ret[::-1]

def get_random_leaf(node):
    while node is not None:
        node = random.choice(node.childNodes)
    return node.parentNode


def UCT(rootstate, itermax, rootnode, verbose = False):
    """ Conduct a UCT search for itermax iterations starting from rootstate.
        Return the best move from the rootstate.
        Assumes 2 alternating players (player 1 starts), with game results in the range [0.0, 1.0]."""

    for i in range(itermax):
        node = rootnode
        state = rootstate.clone()

        # Select
        while node.untriedMoves == [] and node.childNodes != []: # node is fully expanded and non-terminal
            node = node.next_child()
            state.do_move(node.move)

        # Expand
        if node.untriedMoves != []: # if we can expand (i.e. state/node is non-terminal)
            m = random.choice(node.untriedMoves)
            state.do_move(m)
            node = node.add_child(m,state) # add child and descend tree

        # Rollout - this can often be made orders of magnitude quicker using a state.GetRandomMove() function
        while state.get_moves() != []: # while state is non-terminal
            state.do_move(random.choice(state.get_moves()))

        # Backpropagate
        while node != None: # backpropagate from the expanded node and work back to the root node
            node.update(state.get_result(node.playerJustMoved)) # state is terminal. update node with result from POV of node.playerJustMoved
            node = node.parentNode

        return rootnode

def uct_eval(c, parent):
    return c.wins/c.visits + sqrt(2*log(parent.visits)/c.visits)
