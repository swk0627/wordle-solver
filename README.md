# Wordle Solver

## Description
This repository provides a Wordle solver by entropy maximization. The solver calculates the entropies for all variations of tiles by possible inputs in each round. And, it returns the word which has the highest entropy.

## Usage

* Play without solver
    + Original Wordle
        ```
        python wordle.py --all-words data/english-all.txt
        --hidden-words data/english-hidden.txt --max-rounds 6
        ```

    + Pokemon Wordle (Japanese)
        ```
        python wordle.py --all-words data/pokemon-all.txt
        --hidden-words data/pokemon-hidden.txt --max-rounds 10
        ```

* Auto-solve
    + Original Wordle
        ```
        python wordle.py --all-words data/english-all.txt
        --hidden-words data/english-hidden.txt --max-rounds 6 --auto-solve
        ```

    + Pokemon Wordle (Japanese)
        ```
        python wordle.py --all-words data/pokemon-all.txt
        --hidden-words data/pokemon-hidden.txt --max-rounds 10 --auto-solve
        ```
