class Transition:
    def __init__(self, entry, extract, push=None):
        self.entry = entry
        self.extract = extract
        self.push = [self.extract, self.entry] if push is None else push

    def equals(self, let: str, let_pile: str):
        return self.entry == let and self.extract == let_pile

    def get(self):
        t_graphic = ""
        for tr in self.push:
            t_graphic += "{}".format(tr)
        return "{}, {} / {}".format(self.entry, self.extract, t_graphic)
