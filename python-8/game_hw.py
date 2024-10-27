"""NUMBER GUESSING GAME: 
The computer generates a random integer in the range and guess that integer in the minimum number of guesses.
"""

import random
import numpy as np

def random_predict(number: int = 1) -> int:
    """Guessing the number.
    Args:
        number (int, optional): a random number in the range, defaults to 1
    Returns:
        int: attemtps count
    """
    count = 0 # attempt count
    low = 1 # the lower limit of the range (inclusive)
    high = 101 # the upper limit of the range (exclusive)
    while True:
        count += 1
        predict_number = np.random.randint(low, high)  # to generate a random integer from low to high
        if number == predict_number:
            break  # to terminate the loop if the number is guessed
        elif number < predict_number:
            high = predict_number # to narrow the "guess" array from the lower limit to predict_number
        else: 
            low = predict_number # to narrow the "guess" array from predict_number to the upper limit    
    return count


def score_game(random_predict) -> int:
    """Calculating how many attempts in average does the algorithm need to guess the number for 1000 repetions.
    Args:
        random_predict ([type]): "Guessing the number" function
    Returns:
        int: average number of attempts
    """
    count_ls = []
    np.random.seed(20) # to fix seed of reproducibility
    random_array = np.random.randint(1, 101, size=(1000))  # to generate a list of random numbers, "size" indicates quantity of numbers
    
    for number in random_array:
        count_ls.append(random_predict(number))
        score = int(np.mean(count_ls))
        
    print(f"Среднее количество попыток, за которое ваш алгоритм угадывает число: {score}")
    return score


if __name__ == "__main__":
    # RUN
    score_game(random_predict)