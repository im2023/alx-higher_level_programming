-- Using database to lists all genres a show.
SELECT x.name AS name
FROM tv_genres AS x
JOIN tv_show_genres AS b
ON b.genre_id = x.id
JOIN tv_shows AS c
ON b.show_id = c.id
WHERE c.title = 'Dexter'
ORDER BY x.name ASC;

