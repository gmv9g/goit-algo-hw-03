# ЗАВДАННЯ 1
from datetime import datetime

def get_days_from_today(date_str):
    try:
        target_date = datetime.strptime(date_str, '%Y-%m-%d').date()
        
        current_date = datetime.today().date()
        
        delta = current_date - target_date
        
        return delta.days
    
    except ValueError:
        print("Неправильний формат дати. Використовуйте формат 'РРРР-ММ-ДД'.")
        return None

if __name__ == "__main__":
    date_input = input("Введіть дату у форматі 'РРРР-ММ-ДД': ")
    days_difference = get_days_from_today(date_input)
    if days_difference is not None:
        print(f"Кількість днів між {date_input} і сьогодні: {days_difference}")





# ЗАВДАННЯ 2
import random
def get_numbers_ticket(min_num, max_num, quantity):

    if min_num < 1 or max_num > 1000 or quantity < 1 or quantity > (max_num - min_num + 1):
        return []
    
 
    random_numbers = random.sample(range(min_num, max_num + 1), quantity)
    

    return sorted(random_numbers)


if __name__ == "__main__":
    min_num = 1
    max_num = 49
    quantity = 6
    
    lottery_numbers = get_numbers_ticket(min_num, max_num, quantity)
    print("Ваші лотерейні числа:", lottery_numbers)