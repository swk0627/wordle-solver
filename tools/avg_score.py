from wordle import wordle, parse_args


def avg_score():
    all_words = 'data/english-all.txt'
    hidden_words = 'data/english-hidden.txt'
    max_rounds = 10
    auto_solve = True
    f = open(hidden_words)
    words = f.read().splitlines()
    avg_score = 0
    for word in words:
        avg_score += wordle(all_words, hidden_words, max_rounds, word, auto_solve)
    avg_score /= len(words)
    print(avg_score)


if __name__ == '__main__':
    avg_score()