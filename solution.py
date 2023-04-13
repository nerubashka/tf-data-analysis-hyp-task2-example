import pandas as pd
import numpy as np


chat_id = 460109099 # Ваш chat ID, не меняйте название переменной
alpha = 0.04

def solution(x: np.array, y: np.array) -> bool:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    p_val = anderson_ksamp([x, y])[2]
    return p_val < alpha # Ваш ответ, True или False
