#Check if left bracket and right bracket are balanced
def check_balance(brackets):  # The argument is a string
    left_b = 0
    for bracket in brackets:
        if bracket == "[":
            left_b += 1
        elif bracket == "]":
            left_b -= 1
            if left_b < 0:
                return False
    return left_b == 0
