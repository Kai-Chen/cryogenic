def chance_of_missing(num_of_keys: int, num_of_draws: int, total_choices: int):
    """Given total number of choices, the number of keys among the
    choices, and total number of draws, what are the chances of not
    being to draw a single key in all the draws.
    """
    r = 1
    for _ in range(num_of_draws):
        r = r * (total_choices - num_of_keys) / total_choices
        total_choices = total_choices - 1
    return r
