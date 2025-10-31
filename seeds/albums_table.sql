-- The job of this file is to reset all of our important database tables.
-- And add any data that is needed for the tests to run.
-- This is so that our tests, and application, are always operating from a fresh
-- database state, and that tests don't interfere with each other.

-- First, we must delete (drop) all our tables
DROP TABLE IF EXISTS artists cascade;
DROP SEQUENCE IF EXISTS artists_id_seq;
CREATE TABLE artists (
    id SERIAL PRIMARY KEY,
    name text,
    genre text
);

DROP TABLE IF EXISTS albums;
DROP SEQUENCE IF EXISTS albums_id_seq;

-- Then, we recreate them
CREATE SEQUENCE IF NOT EXISTS albums_id_seq;
CREATE TABLE albums (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255),
    release_year int,
    artist_id int,
    constraint fk_artist foreign key(artist_id)
    references artists(id)
    on delete cascade
);

-- Finally, we add any records that are needed for the tests to run

INSERT INTO artists (name, genre) VALUES ('Pixies', 'Rock');
INSERT INTO artists (name, genre) VALUES ('ABBA', 'Pop');
INSERT INTO artists (name, genre) VALUES ('Taylor Swift', 'Pop');
INSERT INTO artists (name, genre) VALUES ('Nina Simone', 'Jazz');
INSERT INTO artists (name, genre) VALUES ('Beyonce', 'Pop');

INSERT INTO albums (title, release_year, artist_id) VALUES ('Album Title 1', 1994, 1);
INSERT INTO albums (title, release_year, artist_id) VALUES ('Album Title 2',2000, 2);
INSERT INTO albums (title, release_year, artist_id) VALUES ('Album Title 3', 2003, 3);
INSERT INTO albums (title, release_year, artist_id) VALUES ('Album Title 4', 1998, 3);
INSERT INTO albums (title, release_year, artist_id) VALUES ('Album Title 5', 1989, 1);