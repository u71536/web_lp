from db import db_session
from models import User

first_user = User(name='Иван Петров', salary=100, email='ivan@example.com')
db_session.add(first_user)
db_session.commit()