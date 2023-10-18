-- Lists all shows in the database hbtn_0d_tvshows without a genre linked.
SELECT cho.`title`, go.`genre_id`
FROM `tv_shows` AS cho
LEFT JOIN `tv_show_genres` AS go ON cho.`id` = go.`show_id`
WHERE go.`genre_id` IS NULL
ORDER BY cho.`title`, go.`genre_id`;
