-- Netflix 
SELECT tv_shows.title, tv_show_genres.genre_id FROM tv_shows, tv_show_genres WHERE tv_show_genres.genre_id IS NOT NULL ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
