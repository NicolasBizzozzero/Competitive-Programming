import threading
from threading import Thread, Event

from mcts import UCT, merge


class Merger(Event):
    def __init__(self, nb_thread, *args, **kwargs):
        super(Merger, self).__init__(*args, **kwargs)
        self.nb_thread = nb_thread
        self.nodes = []
        self.merged = None

    def get_root(self):
        return self.merged

    def add(self, node):
        if self.merged is None:
            self.merged = node


class MCTSThread(Thread):
    """docstring for Thread."""

    def __init__(self, state, batch_size, root, nb_epoch, merger):
        super(Thread, self).__init__()
        self.state = state
        self.batch_size = batch_size
        self.root = root
        self.max_epoch = nb_epoch
        self.merger = merger

    def run(self):
        for _ in range(self.max_epoch):
            self.root = UCT(self.state, self.batch_size, self.root)
            self.merger.add(self.root)
            self.merger.wait()
            self.root = self.merger.get_root()


def single_computer_start(game_state, root, batch_size, nb_epoch, nb_thread):
    merger = Merger(nb_thread)
    th = [MCTSThread(game_state, batch_size, root, nb_epoch, merger)
          for _ in range(nb_thread)]
    for t in th:
        t.run()
    return merger.get_root()
