-- Listing shows in database with genre linked.
SELECT x.title, y.genre_id
FROM tv_shows AS x
LEFT JOIN tv_show_genres AS y
ON x.id = y.show_id
WHERE y.genre_id IS NULL
ORDER BY x.title ASC, y.genre_id ASC;

