-- Netflix 
UPDATE tv_show_genres SET genre_id = 'NULL' WHERE genre_id IS NULL;
SELECT tv_shows.title, tv_show_genres.genre_id FROM tv_shows, tv_show_genres ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
