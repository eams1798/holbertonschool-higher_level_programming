-- list all genres not linked to the show Dexter
CREATE TABLE IF NOT EXISTS dexter_genres
AS (
	SELECT tv_genres.id, tv_genres.name
	FROM tv_genres
	INNER JOIN tv_show_genres
	ON tv_genres.id = tv_show_genres.genre_id
	INNER JOIN tv_shows
	ON tv_shows.id = tv_show_genres.show_id
			WHERE tv_shows.title = 'Dexter');

SELECT tv_genres.name
	FROM tv_genres
	LEFT JOIN dexter_genres
	ON tv_genres.id = dexter_genres.id
	WHERE dexter_genres.name
	IS NULL ORDER BY tv_genres.name;

DROP TABLE dexter_genres;
