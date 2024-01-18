-- Listing shows and genres linked to show.
SELECT d.title, c.name
FROM tv_shows AS d
LEFT JOIN tv_show_genres AS b
ON d.id = b.show_id
LEFT JOIN tv_genres AS c
ON b.genre_id = c.id
ORDER BY d.title ASC, c.name ASC;

