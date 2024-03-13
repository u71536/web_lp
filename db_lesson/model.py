from sqlalchemy import Column, Integer, String, Date, Text
from db import Base, engine


class Salary(Base):
    __tablename__ = "salaries"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    city = Column(String)
    address = Column(Text)
    company = Column(String)
    position = Column(String)
    phone = Column(String)
    email = Column(String)
    birthday = Column(Date)
    salary = Column(Integer)

    def __repr__(self):
        return f"Salary {self.id}, {self.name}, {self.company}"


if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)
