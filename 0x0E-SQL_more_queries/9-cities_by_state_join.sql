-- Listing all cities in the database hbtn_0d_usa.
-- Records are sorted in order of ascending cities.id
SELECT a.`id`, a.`name`, q.`name`
  FROM `cities` AS a
       INNER JOIN `states` AS q
       ON a.`state_id` = q.`id`
 ORDER BY a.`id`;

