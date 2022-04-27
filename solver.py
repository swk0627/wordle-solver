import math


class Solver:

    def __init__(self, awords, hwords):
        self.awords = awords
        self.hwords = hwords

    def evaluate(self, hyp, ans):
        tiles = [0 for _ in range(5)]
        for i in range(min(len(hyp), len(ans))):
            if hyp[i] == ans[i]:
                tiles[i] = 2
                ans = list(ans)
                ans[i] = '0'
                ans = ''.join(ans)
            if tiles[i] != 2 and hyp[i] in ans:
                tiles[i] = 1
        return tiles

    def entropies(self):
        entropies = [0 for _ in range(len(self.awords))]
        for i, hyp in enumerate(self.awords):
            probabilities = [0 for _ in range(3 ** 5)]
            for ans in self.hwords:
                tiles = self.evaluate(hyp, ans)
                tiles = map(str, tiles)
                probabilities[int(''.join(tiles), 3)] += 1 / len(self.hwords)
            for j in range(len(probabilities)):
                if probabilities[j] != 0: entropies[i] += probabilities[j] * math.log2(1 / probabilities[j])
        return entropies

    def guess(self):
        entropies = self.entropies()
        opt_word = self.awords[entropies.index(max(entropies))]
        return opt_word

    def update(self, hyp, tiles):
        new_awords = []
        new_hwords = []
        for cand in self.awords:
            if tiles == self.evaluate(hyp, cand):
                new_awords.append(cand)
                if cand in self.hwords:
                    new_hwords.append(cand)
        self.awords = new_awords
        self.hwords = new_hwords