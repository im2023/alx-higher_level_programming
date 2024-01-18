-- Listing all shows contained in database least one genre linked.
SELECT x.title, y.genre_id
FROM tv_shows AS x, tv_show_genres AS y
WHERE y.show_id = x.id
ORDER BY x.title ASC, y.genre_id ASC;

