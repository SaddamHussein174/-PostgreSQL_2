
# __________________Создание Б.Д_________________________________________________________________________________


CREATE TABLE IF NOT EXISTS Исполнители (
	id_artist SERIAL PRIMARY key,
	Имя VARCHAR(50) NOT NULL UNIQUE,
	id_genre INTEGER NOT NULL UNIQUE
);
CREATE TABLE IF NOT EXISTS Альбомы (
	id_album SERIAL PRIMARY key,
	Название_альбома VARCHAR(100)  NOT NULL,
	Год_выпуска VARCHAR(4) NOT NULL,
	id_artist INTEGER REFERENCES Исполнители(id_artist) NOT NULL
);
CREATE TABLE IF NOT EXISTS Треки (
	id_track SERIAL PRIMARY key,
	Название_трека VARCHAR(100)  NOT NULL,
	Длительность VARCHAR(10) NOT NULL,
	id_album INTEGER REFERENCES Альбомы(id_album) NOT NULL
);
CREATE TABLE IF NOT EXISTS Жанры (
	id_genre SERIAL PRIMARY key,
	Название_жанра VARCHAR(100)  NOT NULL UNIQUE
);
ALTER TABLE Исполнители ADD CONSTRAINT id_genre FOREIGN KEY (id_genre) REFERENCES Жанры(id_genre);


# _______________________Изменение Б.Д_________________________________________________________________________


CREATE TABLE IF NOT EXISTS Жанры_Исполнители (
	id_genre INTEGER REFERENCES Жанры(id_genre) NOT NULL,
	id_artist INTEGER REFERENCES Исполнители(id_artist) NOT NULL
);
CREATE TABLE IF NOT EXISTS Альбомы_Исполнители (
	id_album INTEGER REFERENCES Альбомы(id_album) NOT NULL,
	id_artist INTEGER REFERENCES Исполнители(id_artist) NOT NULL
);
CREATE TABLE IF NOT EXISTS Сборники (
	id_collection SERIAL PRIMARY key,
	Название_сборника VARCHAR(100)  NOT NULL,
	Год_выпуска VARCHAR(4) NOT NULL
);
CREATE TABLE IF NOT EXISTS Сборники_Исполнители (
	id_collection INTEGER REFERENCES Сборники(id_collection) NOT NULL,
	id_track INTEGER REFERENCES Треки(id_track) NOT NULL
);

# Использовать кириллицу для именования таблиц и полей - не рекомендуется я знаю, в следующих проектах так и буду
# делать, пока оставил так, чтоб не запутаться # спасибо за понимание!
