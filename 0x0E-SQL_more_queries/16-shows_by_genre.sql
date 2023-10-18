-- Lists all shows and genres linked to the show from the
SELECT tho.`title`, goo.`name`
FROM `tv_shows` AS tho
LEFT JOIN `tv_show_genres` AS ss
ON tho.`id` = ss.`show_id`

LEFT JOIN `tv_genres` AS goo
ON ss.`genre_id` = goo.`id`
ORDER BY tho.`title`, goo.`name`;
