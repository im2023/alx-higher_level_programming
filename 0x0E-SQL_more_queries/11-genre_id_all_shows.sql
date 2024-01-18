-- Listing all shows contained in database
SELECT x.title, b.genre_id
FROM tv_shows AS x
LEFT JOIN tv_show_genres AS y
ON x.id = y.show_id
ORDER BY x.title ASC, y.genre_id ASC;

