import csv
import time

from db_lesson.db import db_session
from db_lesson.model import Salary

def read_csv(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        fields = ['name', 'city', 'address', 'company',
                  'position', 'phone', 'email', 'birthday',
                  'salary']
        reader = csv.DictReader(f, fields, delimiter=';')
        for row in reader:
            save_salary_data(row)

def save_salary_data(row):
    salary = Salary(name=row['name'], city=row['city'],
            address=row['address'],
            company=row['company'], position=row['position'],
            phone=row['phone'],
            email=row['email'], birthday=row['birthday'],
            salary=row['salary'])
    db_session.add(salary)
    db_session.commit()

if __name__ == '__main__':
    read_csv('salary.csv')

if __name__ == '__main__':
    start = time.time()
    read_csv('salary.csv')
    print('Данные загружены за ', time.time() - start)