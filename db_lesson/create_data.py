import csv
import random
from faker import Faker

fake = Faker('ru_RU')


def get_fake_row():
    return [fake.name(), fake.city_name(), fake.street_address(),
            fake.large_company(),
            fake.job(), fake.phone_number(), fake.free_email(),
            fake.date_of_birth(minimum_age=18, maximum_age=70),
            random.randint(20000, 200000)]


def generate_data(num_rows=100):
    with open('salary.csv', 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f, delimiter=';')
        for i in range(num_rows):
            writer.writerow(get_fake_row())

if __name__ == '__main__':
    generate_data()
