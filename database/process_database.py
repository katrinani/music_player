"""
sudo -u postgres psql - вход в консоль постгреса
Команды:
    CREATE USER - WITH PASSWORD '';  - создание пользователя
    CREATE DATABASE -; - создание базы данных
    GRANT ALL PRIVILEGES ON DATABASE - TO -; - выдача прав пользователю

sudo service postgesql start - запуск серввера
systemctl status postgresql - проверка работает ли сервер
sudo grep port /etc/postgresql/*/main/postgresql.conf - проверка порта сервера
sudo grep listen_addresses /etc/postgresql/*/main/postgresql.conf - проверка хоста срвера
"""
import psycopg2
import configparser

config = configparser.ConfigParser()
config.read("../config.ini")
USER = config["Database"]["user"]
PASSWORD = config["Database"]["password"]

conn = psycopg2.connect(
    database="allsongs",
    user=USER,
    password=PASSWORD,
    host='localhost',
    port=5432
)
conn.autocommit = True
cursor = conn.cursor()


def create_and_filling_database():
    create = '''CREATE TABLE IF NOT EXISTS spotify_data(
        track_id VARCHAR(255) NOT NULL,
        track_name VARCHAR(255),
        track_artist VARCHAR(255),
        track_popularity INT,
        track_album_id VARCHAR(255),
        track_album_name VARCHAR(255),
        track_album_release_date DATE,
        playlist_name VARCHAR(255),
        playlist_id VARCHAR(255),
        playlist_genre VARCHAR(255),
        playlist_subgenre VARCHAR(255),
        danceability FLOAT,
        energy FLOAT,
        key INT,
        loudness FLOAT,
        mode INT,
        speechiness FLOAT,
        acousticness FLOAT,
        instrumentalness FLOAT,
        liveness FLOAT,
        valence FLOAT,
        tempo FLOAT,
        duration_ms INT
    );'''
    cursor.execute(create)

    copy = '''COPY spotify_data(track_id,track_name,track_artist,track_popularity,\
    track_album_id,track_album_name,track_album_release_date,playlist_name,playlist_id,playlist_genre,\
    playlist_subgenre,danceability,energy,key,loudness,mode,speechiness,acousticness,instrumentalness,\
    liveness,valence,tempo,duration_ms) 
    FROM '/tmp/new_spotify_song.csv' 
    DELIMITER ',' 
    CSV HEADER
    '''
    cursor.execute(copy)

    # sql3 = '''select * from spotify_data;'''
    # cursor.execute(sql3)
    # for song in cursor.fetchmany(size=5):
    #     print(song)


if __name__ == "__main__":
    create_and_filling_database()
