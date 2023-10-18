-- Lists all shows in hbtn_0d_tvshows that have at least one genre linked.
SELECT cho.`title`, oo.`genre_id`
FROM `tv_shows` AS cho
INNER JOIN `tv_show_genres` AS oo ON cho.`id` = oo.`show_id`
ORDER BY cho.`title`, oo.`genre_id`;
