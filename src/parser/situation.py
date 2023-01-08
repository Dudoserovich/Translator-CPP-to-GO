from src import grammar as gr


class Situation:

    def __init__(self, k: int, left: gr.Term, after_dot: [], before_dot=None):
        if before_dot is None:
            self.beforeDot = []
        else:
            self.beforeDot = before_dot
        self.k = k
        self.left = left
        if type(after_dot) is list:
            self.afterDot = after_dot
        else:
            self.afterDot = [after_dot]

    def move_dot(self):
        self.beforeDot.append(self.afterDot.pop(0))

    def set_k(self, k: int):
        self.k = k

    def get_k(self):
        return self.k