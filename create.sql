-- ----------------------
-- Create Genres table
-- ----------------------
CREATE TABLE genres
(
  id              INTEGER   NOT NULL,
  name_genre      CHAR(100) NOT NULL
);

-- ----------------------
-- Create people table
-- ----------------------
CREATE TABLE people
(
  id             INTEGER   NOT NULL,
  name_actor     CHAR(150) NOT NULL,
  birthday       DATE,
  gender         INTEGER
);

-- ----------------------
-- Create all_series table
-- ----------------------
CREATE TABLE all_series
(
  id             INTEGER        NOT NULL ,
  name_series    CHAR(150)      NOT NULL ,
  airing_date    DATE           NOT NULL 
);

CREATE TABLE rating_date
(
  id             INTEGER        NOT NULL ,
  series_id      INTEGER        NOT NULL ,
  average_rating DECIMAL(30, 5) NOT NULL ,
  date_rating    DATE           NOT NULL
);

-- ----------------------
-- Create genre_series table
-- ----------------------
CREATE TABLE genre_series
(
  id             INTEGER        NOT NULL ,
  genre_id       INTEGER        NOT NULL ,
  series_id      INTEGER        NOT NULL 
);

-- ----------------------
-- Create cast_series table
-- ----------------------
CREATE TABLE cast_series
(
  id             INTEGER        NOT NULL ,
  series_id      INTEGER        NOT NULL ,
  actor_id       INTEGER        NOT NULL 
);

ALTER TABLE genres ADD PRIMARY KEY (id);
ALTER TABLE people ADD PRIMARY KEY (id);
ALTER TABLE all_series ADD PRIMARY KEY (id);
ALTER TABLE rating_date ADD PRIMARY KEY (id);
ALTER TABLE genre_series ADD PRIMARY KEY (id);
ALTER TABLE cast_series ADD PRIMARY KEY (id);

ALTER TABLE genre_series ADD CONSTRAINT FK_Series_Genre_genre FOREIGN KEY (genre_id) REFERENCES genres (id);
ALTER TABLE genre_series ADD CONSTRAINT FK_Series_Genre_serie FOREIGN KEY (series_id) REFERENCES all_series (id);
ALTER TABLE cast_series ADD CONSTRAINT FK_Cast_Series_actor FOREIGN KEY (actor_id) REFERENCES people (id);
ALTER TABLE cast_series ADD CONSTRAINT FK_Cast_Series_serie FOREIGN KEY (series_id) REFERENCES all_series (id);
ALTER TABLE rating_date ADD CONSTRAINT FK_Rating_Series_serie FOREIGN KEY (series_id) REFERENCES all_series (id);