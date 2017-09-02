<?php function dream_connect (){
  $conn_id = @mysql_connect ("cs1.ucc.ie", "ecf1", "leethaiw");
  if ($conn_id && mysql_select_db ("Dreamhome_ecf1", $conn_id))
    return ($conn_id);
  return (FALSE);
}
?>
