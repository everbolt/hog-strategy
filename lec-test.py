from functools import lru_cache
memoize = lru_cache(None)

def six_sided(outcome):
    if 1 <= outcome <= 6:
        return 1/6
    else:
        return 0
    
dice = six_sided

def roll_dice(total, n):
    if total == 1:
        return roll_a_one(n)
    else:
        return roll_no_ones(total, n)

def roll_a_one(n):
    if n == 0:
        return 0
    return dice(1) + (1 - dice(1)) * roll_a_one(n - 1)

@memoize
def roll_no_ones(total, n):
    if total == 0 and n == 0:
        return 1
    elif n == 0:
        return 0
    elif total < 0:
        return 0
    else:
        chance, outcome = 0, 2
        while outcome <= 6:
            chance += dice(outcome) * roll_no_ones(total - outcome, n - 1)
            outcome += 1
        return chance

def roll_at_least(k, n):
    total, chance = k, 0
    while total <= 6 * n:
        chance += roll_dice(total, n)
        total += 1
    return chance

#Other game example to 21
goal = 21

def play(strat0, strat1):
    n = 0
    who = 0
    while n < goal:
        n = n + (strat1 if who == 1 else strat0)(n)
        who = 1 - who
    return who

def winner(n, strat, other):
    if n >= goal:
        return 0
    else:
        return 1 - winner(n + strat(n), other, strat)

@memoize
def optimal(n, other_strat):
    choice = 1
    future_strat = lambda future_n: optimal(future_n, other_strat)
    while choice <= 3:
        if winner(n + choice, other_strat, future_strat):
            return choice
        choice = choice + 1
    return 1

def print_perfect():
    n = 0
    perfect = lambda n: optimal(n, perfect)
    while n < goal:
        if winner(n, perfect, perfect) == 0:
            print("Perfect play from", n, "wins with choice", perfect(n))
        else:
            print("Looks bad from", n)
        n = n + 1