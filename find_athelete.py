import datetime
import sqlalchemy
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

DB_PATH = "sqlite:///sochi_athletes.sqlite3"
Base = declarative_base()

class Athelete(Base):
    __tablename__ = 'athelete'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    age = sqlalchemy.Column(sqlalchemy.Integer)
    birthdate = sqlalchemy.Column(sqlalchemy.Text)
    gender = sqlalchemy.Column(sqlalchemy.Text)
    height = sqlalchemy.Column(sqlalchemy.Float)
    weight = sqlalchemy.Column(sqlalchemy.Integer)
    name = sqlalchemy.Column(sqlalchemy.Text)
    gold_medals = sqlalchemy.Column(sqlalchemy.Integer)
    silver_medals = sqlalchemy.Column(sqlalchemy.Integer)
    bronze_medals = sqlalchemy.Column(sqlalchemy.Integer)
    total_medals = sqlalchemy.Column(sqlalchemy.Integer)
    sport = sqlalchemy.Column(sqlalchemy.Text)
    country = sqlalchemy.Column(sqlalchemy.Text)

class User(Base):
    __tablename__ = "user"
    # идентификатор пользователя, первичный ключ
    id = sqlalchemy.Column(sqlalchemy.String(36), primary_key=True)
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
    user_id = input("Ввети идентификатор пользователя: ")
    return int(user_id)

def dat(date):
    a = date.split('-')
    data_f = map(int, a)
    date2 = datetime.date(*data_f)
    return date2

def nearbid(user, session):
    athletes = session.query(Athelete).all()
    athletes_id_bd = {}
    for at in athletes:
        dt = dat(at.birhdate)
        athletes_id_bd[at.id] = dt

    user_dt = dat(user.birthdate)
    min_dist = None
    athlete_id = None
    athlete_bd = None

    for id_, bd in athlete_id.items():
        dist = abs(user_dt - bd)
        if not min_dist or dist < min_dist:
            min_dist = dist
            athlete_id = id_
            athlete_bd = bd

    return athlete_id, athlete_bd

def nearbh(user, session):
    athletes = session.query(Athelete).filter(Athelete.height != None).all()
    atlhete_id_h = {athlete.id: athlete.height for athlete in athletes}

    user_height = user.height
    min_dist = None
    athlete_id = None
    athlete_height = None

    for id_, height in atlhete_id_h.items():
        if height is None:
            continue

        dist = abs(user_height - height)
        if not min_dist or dist < min_dist:
            min_dist = dist
            athlete_id = id_
            athlete_height = height

    return athlete_id, athlete_height

def main():
    session = connect_bd()
    user_id = request_data()
    user = session.query(User).filter(User.id == user_id).first()
    if not user:
        print("Такого пользователя не нашлось:(")
    else:
        bd_athlete, bd = nearbid(user, session)
        height_athlete, height = nearbh(user, session)
        print(
            "Ближайший по дате рождения атлет: {}, его дата рождения: {}".format(bd_athlete, bd)
        )
        print(
            "Ближайший по росту атлет: {}, его рост: {}".format(height_athlete, height)
        )

if __name__ == "__main__":
    main()
