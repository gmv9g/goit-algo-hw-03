# завдання 2
def total_salary(path):
    total_salary = 0
    count = 0
    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                line = line.strip()
                if line:
                    parts = line.split(',')
                    if len(parts) == 2:
                        salary = int(parts[1].strip())
                        total_salary += salary
                        count += 1
                    else:
                        print(f"Invalid data format in line: {line}")
            
            if count > 0:
                average_salary = total_salary / count
            else:
                average_salary = 0
            
            return total_salary, average_salary

    except FileNotFoundError:
        print(f"File '{path}' not found.")
        return None, None
    except Exception as e:
        print(f"Error reading file '{path}': {str(e)}")
        return None, None

file_path = r"D:\\назва_директорії\\salary_file.txt.txt"
total, average = total_salary(file_path)
if total is not None and average is not None:
    print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
# задвання 2
def get_cats_info(path):
    cats_info = []

    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                line = line.strip()
                if line:
                    parts = line.split(',')
                    if len(parts) == 3:
                        cat_id = parts[0].strip()
                        cat_name = parts[1].strip()
                        cat_age = parts[2].strip()
                        cat_dict = {"id": cat_id, "name": cat_name, "age": cat_age}
                        cats_info.append(cat_dict)

        return cats_info

    except FileNotFoundError:
        print(f"Error: The file '{path}' was not found.")
        return []

cats_info = get_cats_info("cats_info.txt.txt")

for cat in cats_info:
    print(f"ID: {cat['id']}, Name: {cat['name']}, Age: {cat['age']}")