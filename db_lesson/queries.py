from db_lesson.model import Salary
from sqlalchemy.sql import func

from db import db_session

def top_salary(email_domain, limit_1):
    top_salary = Salary.query.filter(Salary.email.like(f"%{email_domain}")).order_by(Salary.salary.desc()).limit(limit_1)
    for salary in top_salary:
        print(f'{salary.email}З/п {salary.salary} живет в {salary.city}')



def average_salary():
    result = db_session.query(func.avg(Salary.salary)).scalar()
    print(f"Средняя зарплата {result:.2f}")

if __name__ == '__main__':
    average_salary()

if __name__ == '__main__':
    top_salary("gmail.com", 5)