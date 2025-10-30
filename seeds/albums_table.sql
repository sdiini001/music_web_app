-- The job of this file is to reset all of our important database tables.
-- And add any data that is needed for the tests to run.
-- This is so that our tests, and application, are always operating from a fresh
-- database state, and that tests don't interfere with each other.

-- First, we must delete (drop) all our tables
DROP TABLE IF EXISTS albums;
DROP SEQUENCE IF EXISTS albums_id_seq;

-- Then, we recreate them
CREATE SEQUENCE IF NOT EXISTS albums_id_seq;
CREATE TABLE albums (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255),
    release_year int,
    artist_id int
);

-- Finally, we add any records that are needed for the tests to run
INSERT INTO albums (title, release_year, artist_id) VALUES ('Invisible Cities', 1994, 1);
INSERT INTO albums (title, release_year, artist_id) VALUES ('The Man Who Was ThursdGK',2000, 2);
INSERT INTO albums (title, release_year, artist_id) VALUES ('Bluets', 2003, 3);
INSERT INTO albums (title, release_year, artist_id) VALUES ('No Place on Earth', 1998, 3);
INSERT INTO albums (title, release_year, artist_id) VALUES ('Nevada', 1989, 1);