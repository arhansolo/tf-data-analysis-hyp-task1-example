import pandas as pd
import numpy as np


chat_id = 186513775 # Ваш chat ID, не меняйте название переменной

def solution(x_success: int, 
             x_cnt: int, 
             y_success: int, 
             y_cnt: int) -> bool:
    x_mean = x_success / x_cnt
    y_mean = y_success / y_cnt
    
    # Расчет стандартных отклонений
    x_std = np.sqrt((x_mean * (1 - x_mean)) / x_cnt)
    y_std = np.sqrt((y_mean * (1 - y_mean)) / y_cnt)
    
    # Расчет коэффициентов Z
    z_x = (x_mean - y_mean) / np.sqrt(y_std**2 + x_std**2)
    
    # Уровень значимости 0.01
    alpha = 0.01
    
    # Проверка статистической значимости
    if abs(z_x) > 2.33:  # Значение Z для уровня значимости 0.01
        return True  # Отклонить нулевую гипотезу
    else:
        return False  # Не отклонять нулевую гипотезу
