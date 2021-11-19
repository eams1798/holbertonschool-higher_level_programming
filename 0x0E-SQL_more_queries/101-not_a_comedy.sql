-- lists all shows without the genre Comedy in the database hbtn_0d_tvshows
DROP TABLE IF EXISTS comedy_shows;
CREATE TABLE comedy_shows AS( SELECT tv_shows.id, tv_shows.title FROM tv_shows
	INNER JOIN tv_show_genres
	ON tv_shows.id = tv_show_genres.show_id
	INNER JOIN tv_genres
		ON tv_genres.id = tv_show_genres.genre_id
		WHERE tv_genres.name = 'Comedy'
	ORDER BY tv_shows.title);

SELECT tv_shows.title
	FROM tv_shows
	LEFT JOIN comedy_shows
	ON tv_shows.id = comedy_shows.id 
	WHERE comedy_shows.title IS NULL
	ORDER BY tv_shows.title;

DROP TABLE comedy_shows;
