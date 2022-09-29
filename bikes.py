import sqlite3
from tokenize import Double

db = sqlite3.connect("bikes.db")
db.isolation_level = None


def distance_of_user(user):
    print(user)
    count = db.execute("""SELECT sum(distance) 
                         FROM Trips T, Users U
                         Where T.user_id = U.id AND U.name = ? 
                         GROUP BY t.user_id""",[user]).fetchone()
    return count


def speed_of_user(user):
    a  = db.execute("""SELECT sum(distance) 
                        FROM Trips T, Users U
                        Where T.user_id = U.id AND U.name = ? 
                        GROUP BY t.user_id""",[user]).fetchone()
    print(a)
    matka = int(a[0])/1000
    
    b = db.execute("""SELECT sum(duration) 
                         FROM Trips T, Users U
                         Where T.user_id = U.id AND U.name = ? 
                         GROUP BY t.user_id""",[user]).fetchone()
    print(b)
    aika = int(b[0])/60
    nopeus = matka/aika
    return "{:.2f}".format(nopeus)


def duration_in_each_city(day):
    a = db.execute("""
    SELECT C.name, SUM(T.duration) FROM Trips T, Stops S, Cities C
    WHERE C.id = S.city_id AND T.from_id = S.city_id AND T.day = ?
    GROUP BY C.id
    """)
    return "JEE"


def users_in_city(city):
    return "jee"


def trips_on_each_day(city):
    return "jee"


def most_popular_start(city):
    return "jee"