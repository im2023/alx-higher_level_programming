-- Listing shows by their rating
SELECT a.title, SUM(b.rate) AS rating
FROM tv_shows AS d
JOIN tv_show_ratings AS b
ON d.id = b.show_id
GROUP BY d.title
ORDER BY rating DESC;

