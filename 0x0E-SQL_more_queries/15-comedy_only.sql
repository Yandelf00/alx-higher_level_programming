-- Lists all comedy shows in the database hbtn_0d_tvshows.
SELECT tho.`title`
FROM `tv_shows` AS tho
INNER JOIN `tv_show_genres` AS sho
ON tho.`id` = sho.`show_id`

INNER JOIN `tv_genres` AS go
ON go.`id` = sho.`genre_id`
WHERE go.`name` = "Comedy"
ORDER BY tho.`title`;
