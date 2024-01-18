-- Listing all Comedy shows in a database
SELECT d.title
FROM tv_shows AS d
JOIN tv_show_genres AS b
ON d.id = b.show_id
JOIN tv_genres AS c
ON b.genre_id = c.id
WHERE c.name = 'Comedy'
ORDER BY d.title ASC;

