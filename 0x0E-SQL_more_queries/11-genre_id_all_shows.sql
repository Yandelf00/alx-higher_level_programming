-- Lists all shows contained in the database hbtn_0d_tvshows.
SELECT cho.`title`, go.`genre_id`
FROM `tv_shows` AS cho
LEFT JOIN `tv_show_genres` AS go ON cho.`id` = go.`show_id`
ORDER BY cho.`title`, go.`genre_id`;
