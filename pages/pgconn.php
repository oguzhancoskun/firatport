<?php
$db = pg_connect("host=localhost port=5432 dbname=dbfport user=fport password=fportpass");
$result = pg_query($db,"SELECT * FROM sunucular ORDER BY id DESC LIMIT 12");

?>