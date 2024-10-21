import numpy as np

def random_predict(number:int=1) -> int:
    count = 0
    while True:
        count += 1
        predict_number = np.random.randint(1,101)
        if number == predict_number:
            break
    return(count)
print(f"Количество попыток: {random_predict()}")

def score_game(random_predict) -> int:
    """За какое количество попыток в среднем из 1000 подходов угадывает наш алгоритм
    Args: random_predict ([type]): функция угадывания
    Returns: int: среднее количество попыток
    """
    
    count_ls = [] # a list to save a number of tries
    np.random.seed(1) # to fix seed of reproducibility
    random_array = np.random.randint(1,101, size=(1000)) # to guess a list of numbers
      
    for number in random_array:
        count_ls.append(random_predict(number))
    score = int(np.mean(count_ls))
    print(f'Ваш алгоритм угадывает число в среднем за: {score} попыток')
    return(score)

if __name__ == '__main__':
    score_game(random_predict)