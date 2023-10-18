-- Lists all genres of the show Dexter in the database hbtn_0d_tvshows.
SELECT go.`name`
  FROM `tv_genres` AS go
       INNER JOIN `tv_show_genres` AS sho
       ON go.`id` = sho.`genre_id`

       INNER JOIN `tv_shows` AS ton
       ON ton.`id` = sho.`show_id`
       WHERE ton.`title` = "Dexter"
 ORDER BY go.`name`;
