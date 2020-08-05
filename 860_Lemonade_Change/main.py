def lemonadeChange(bills):
    """
    :type bills: List[int]
    :rtype: bool
    """

    n_fives = 0
    n_tens = 0
    n_twenties = 0

    for bill in bills:
        if bill == 5:
            n_fives += 1
        if bill == 10:
            # We need a 5.
            if n_fives == 0:
                return False
            n_fives -= 1
            n_tens += 1
        if bill == 20:
            # We need 'at least' one 5.
            if n_fives == 0:
                return False
            if n_tens == 0:
                # Do we have three 5s instead?
                if n_fives < 3:
                    return False
                n_fives -= 3
            else:
                n_tens -= 1
                n_fives -= 1
            n_twenties += 1
    return True

print(lemonadeChange([5,5,5,10,20]))
print(lemonadeChange([5,5,10]))
print(lemonadeChange([10,10]))
print(lemonadeChange([5,5,10,10,20]))
