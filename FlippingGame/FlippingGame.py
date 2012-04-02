from System import Random

class FlippingGame(object):
    def __init__(self, bankroll=500, history=[], seed=None):
        self.history = history
        self.bankroll = self.initial_bankroll = bankroll
        self.rand = Random(seed) if seed is not None else Random()

    def flip(self, guess, wager):
        result = self._do_flip()
        self.history.append((result, guess, wager))
        if result == guess:
            self.bankroll += wager
            return True, result
        else:
            self.bankroll -= wager
            return False, result

    def _do_flip(self):
        return "TF"[self.rand.Next(2)]
