import argparse
import random

from solver import Solver


def parse_args():
    arg_parser = argparse.ArgumentParser()

    arg_parser.add_argument('--all-words', type=str, default='data/english-all.txt',
                            help='The path to a file which contains possible words as inputs.')
    arg_parser.add_argument('--hidden-words', type=str, default='data/english-hidden.txt',
                            help='The path to a file which contains possible words as an answer.')
    arg_parser.add_argument('--max-rounds', type=int, default=6,
                            help='The limit number of rounds.')
    arg_parser.add_argument('--answer', type=str, default=None,
                            help='The user-defined answer')
    arg_parser.add_argument('--auto-solve', default=False, action='store_true', 
                            help='Solve wordle automatically by entropy maximization.')

    args = arg_parser.parse_args()

    return args


def wordle(afile, hfile, limit, answer, auto_solve):
    with open(afile, mode='r') as f:
        awords = f.read().splitlines()
    with open(hfile, mode='r') as f:
        hwords = f.read().splitlines()
    
    if answer: ans = answer
    else: ans = hwords[random.randint(0, len(hwords) - 1)]

    cnt = 0
    solver = Solver(awords, hwords)

    while cnt < limit:
        print(f'Round {cnt+1}:')
        if auto_solve:
            hyp = solver.guess()
            print(hyp)
        else: hyp = input()
        if not hyp in awords:
            print('Unexpected word')
            continue
        else:
            tiles = solver.evaluate(hyp, ans)
            print(' '.join(map(str, tiles)))

        if tiles == [2, 2, 2, 2, 2]:
            print('Correct!')
            break

        if cnt == limit - 1:
            print(f'The answer was {ans}.')
            print('Failure')
            break

        if auto_solve: solver.update(hyp, tiles)
        
        cnt += 1

    return cnt
        

if __name__ == '__main__':
    args = parse_args()
    wordle(args.all_words, args.hidden_words, args.max_rounds, args.answer, args.auto_solve)