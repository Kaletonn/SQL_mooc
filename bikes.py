import sqlite3
from tokenize import Double

db = sqlite3.connect("bikes.db")
db.isolation_level = None

#toimii
def distance_of_user(user):
    count = db.execute("""SELECT sum(distance) 
                         FROM Trips T, Users U
                         Where T.user_id = U.id AND U.name = ? 
                         GROUP BY t.user_id""",[user]).fetchone()
    return count[0]

#toimii
def speed_of_user(user):
    a  = db.execute("""SELECT sum(distance) 
                        FROM Trips T, Users U
                        Where T.user_id = U.id AND U.name = ? 
                        GROUP BY t.user_id""",[user]).fetchone()
    matka = int(a[0])/1000
    
    b = db.execute("""SELECT sum(duration) 
                         FROM Trips T, Users U
                         Where T.user_id = U.id AND U.name = ? 
                         GROUP BY t.user_id""",[user]).fetchone()
    aika = int(b[0])/60
    nopeus = matka/aika
    return "{:.2f}".format(nopeus)

#toimii
def duration_in_each_city(day):
    a = db.execute("""
    SELECT C.name, SUM(T.duration) FROM Trips T, Stops S, Cities C
    WHERE C.id = S.city_id AND T.from_id = S.id
    AND T.day = ?
    GROUP BY C.id
    """,[day]).fetchall()
    return a

#toimii
def users_in_city(city):
    a = db.execute("""
    SELECT count(Distinct T.user_id) 
    FROM Trips T 
    LEFT JOIN Stops S ON T.from_id = S.id 
    LEFT JOIN Cities C ON C.id = S.city_id
    WHERE C.name=?
    GROUP BY c.id
    """,[city]).fetchone()
    kayttajat = a[0]
    return kayttajat

#toimii
def trips_on_each_day(city):
    matkat = db.execute("""
    SELECT T.day, count(T.user_id) 
    FROM Trips T 
    LEFT JOIN Stops S  ON T.from_id = S.id 
    LEFT JOIN Cities C ON C.id = S.city_id
    WHERE C.name=?
    GROUP BY T.day""",[city]).fetchall()
    return matkat

#toimii
def most_popular_start(city):
    stoppi = db.execute("""
    SELECT S.name, count(T.user_id) 
    FROM Trips T 
    LEFT JOIN Stops S ON T.from_id = S.id 
    LEFT JOIN Cities C ON C.id = S.city_id
    WHERE C.name=?
    GROUP BY S.id
    ORDER BY COUNT(T.user_id) DESC""",[city]).fetchone()
    return stoppi