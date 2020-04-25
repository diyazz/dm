
import sqlalchemy
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

DB_PATH = "sqlite:///sochi_athletes.sqlite3"
Base = declarative_base()

class User(Base):
    '''Описывает структуру таблицы user для хранения регистрационных данных пользователей'''
    # задаем название таблицы
    __tablename__ = "user"
    # идентификатор пользователя, первичный ключ
    id = sqlalchemy.Column(sqlalchemy.INTEGER, primary_key=True)
    # имя пользователя
    first_name = sqlalchemy.Column(sqlalchemy.Text)
    # фамилия пользователя
    last_name = sqlalchemy.Column(sqlalchemy.Text)
    # адрес электронной почты пользователя
    email = sqlalchemy.Column(sqlalchemy.Text)

    gender = sqlalchemy.Column(sqlalchemy.Text)

    birthdate = sqlalchemy.Column(sqlalchemy.Text)

    height = sqlalchemy.Column(sqlalchemy.FLOAT(24))
def connect_bd():
    '''Устанавливает соединение к базе данных, создает таблицы, если их еще нет и возвращает объект сессии'''
    # создаем соединение к базе данных
    engine = sqlalchemy.create_engine(DB_PATH)
    # создаем описанные таблицы
    Base.metadata.create_all(engine)
    # создаем фабрику сессию
    session = sessionmaker(engine)
    # возвращаем сессию
    return session()

def request_data():
    '''Запрашивает у пользователя данные и добавляет их в список users'''

    # выводим приветствие
    print("Привет! Я запишу твои данные!")
    # запрашиваем у пользователя данные
    first_name = input("Введи своё имя: ")
    last_name = input("А теперь фамилию: ")
    email = input("Мне еще понадобится адрес твоей электронной почты: ")

    birthdate = input("Введи дату рождения в формате yyyy-mm-dd. ")
    height = input("Введи свой рост ")

    gender = input("Введи свой пол Male или Female ")
    # генерируем идентификатор пользователя и сохраняем его строковое представление

    # создаем нового пользователя
    user = User(

        first_name=first_name,
        last_name=last_name,
        gender=gender,
        email=email,
        birthdate=birthdate,
        height=height
    )
    # возвращаем созданного пользователя
    return user

def main():
    session = connect_bd()
    user = request_data()
    session.add(user)
    session.commit()
    print("Твои данные сохранены.")


main()