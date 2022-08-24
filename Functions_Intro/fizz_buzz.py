def fizz_buzz(number: str = 0) -> str:
    """
    Return the next answer in the game of fizz buzz

    :param number: The number to check
    :return: If divisible by 3 'fizz',
    if divisible by 5 'buzz',
    if divisible by both 3 and 5 'fizz buzz',
    otherwise return the number
    """

    if number % 3 != 0 and number % 5 != 0:
        return str(number)
    elif number % 3 == 0 and number % 5 == 0:
        return "fizz buzz"
    elif number % 3 == 0:
        return "fizz"
    else:
        return "buzz"


print("Starting a new game of fizz buzz")
next_number = 0
while next_number < 99:
    next_number += 1
    print(fizz_buzz(next_number))
    next_number +=1
    correct_answer = fizz_buzz(next_number)
    player_input = input("Your go: ")
    # player_input = correct_answer
    if correct_answer != player_input:
        print("You lose, the correct answer was {}".format(correct_answer))
        break
else:
    print("Well done you have reached {}".format(next_number))