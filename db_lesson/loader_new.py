import time
import csv
from db_lesson.db import db_session
from db_lesson.model import Salary

def read_csv2(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        fields = ['name', 'city', 'address', 'company',
                  'position', 'phone', 'email', 'birthday', 'salary']
        reader = csv.DictReader(f, fields, delimiter=';')
        salary_data = []
        for row in reader:
            salary_data.append(row)
        save_salary_data2(salary_data)

def save_salary_data2(salary_data):
    db_session.bulk_insert_mappings(Salary, salary_data)
    db_session.commit()

if __name__ == '__main__':
    read_csv2('salary.csv')

if __name__ == '__main__':
    start = time.time()
    read_csv2('salary.csv')
    print('Данные загружены за ', time.time() - start)
