-- Listing genres from database and displaying number of shows linked
SELECT d.name AS genre, COUNT(b.genre_id) AS number_of_shows
FROM tv_genres d
INNER JOIN tv_show_genres b
ON d.id = b.genre_id
GROUP BY b.genre_id
ORDER BY number_of_shows DESC;

