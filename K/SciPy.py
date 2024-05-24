from scipy.stats import norm
# В-9 Каравайцева Вероника Александровна

checklist = {
    'mathExpect': 60,
    'MSD': 5,
    'MinWt': 50,
    'MaxWt': 70,
    'Deviation': 8
}

# norm - нормальное распределение, cdf = кумулятивная функция распределения
# Вероятность попадания в диапазон от 50 до 70 заготовки

# а)
probability = (norm.cdf(checklist['MaxWt'], loc=checklist['mathExpect'], scale=checklist['MSD']) -
               norm.cdf(checklist['MinWt'], loc=checklist['mathExpect'], scale=checklist['MSD']))

# б)
prob_of_dev = (norm.cdf(checklist['mathExpect'] + checklist['Deviation'], checklist['mathExpect'], checklist['MSD']) -
               norm.cdf(checklist['mathExpect'] - checklist['Deviation'], checklist['mathExpect'], checklist['MSD']))

# Правило трех сигм
# в)
sigma3 = (norm.cdf(checklist['mathExpect'] + 3*checklist['MSD'], checklist['mathExpect'], checklist['MSD']) -
               norm.cdf(checklist['mathExpect'] - 3*checklist['MSD'], checklist['mathExpect'], checklist['MSD']))

# Вывод результатов
print('Вероятность, что случайно выбранное яйцо будет в диапазоне [50; 70]:', f'{float("%.4f"%probability)*100}%')
print(f'Вероятность отклонения: {prob_of_dev * 100}%')
print(f'Вероятность по правилу "трёх сигм": {float("%.4f"%sigma3)}')