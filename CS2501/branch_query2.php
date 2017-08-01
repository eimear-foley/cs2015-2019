<!DOCTYPE html>
<head>
  <title>Branch Query</title>
  <style>
    body{
      background-color: white;
      font-family: 'Century Gothic', CenturyGothic, AppleGothic, sans-serif;
    }
    
    h3{
      color: #33a1de;
      text-align: center;
    } 
    table, tr, td, th{
	border-collapse: collapse;
	padding: .5em;
	border: 1px solid black;
    }
    #operations, #return{
      width: 50%;
      margin-left: auto;
      margin-right:auto;
      border: 1px solid black;
      padding: 1em;
    }
    #return{
	margin-top: 1em;
	text-align: center;
    }
    
    #return a{
	text-decoration: none;
	color:#33a1de;
    }
    
    #return a:hover{
	color: #19506f;
    }
  </style>
</head>
<body>
  <h3>Find the address & phone for a branch.</h3>
  <section id="operations">
  <br>
  <form method="post">
    Branch No.: B3 <input type="radio" name="bno" value="B3" checked> B5 <input type="radio" name="bno" value="B5"> B7 <input type="radio" name="bno" value="B7"> B4 <input type="radio" name="bno" value="B4"> B2 <input type="radio" name="bno" value="B2">
    <br><br>
    <input type="submit" value="Get Address and Phone">
  </form>
  <br>
  
  <?php
  include "dream_setup.php";
  dream_connect() or exit();
  
  if ($_POST){
    $bno = $_POST['bno'];
    $query = ("SELECT Street, Area, City, Pcode, Tel_No FROM  branch WHERE branch.Bno = '".$bno."'");
    $result = mysql_query($query)
      or die("cannot execute query");
    $row = mysql_fetch_row($result);
    if ($row){
      $outstring = "<p>Branch Address: " .$row[0]. ", " .$row[1]. ", " .$row[2]. ", " .$row[3]. "</p>";
      $outstring .= "<p>Telephone number: " .$row[4]. "</p>";
      echo($outstring);
    }
  } 
  ?>
  </section>
  <div id="return">
    <h3>
      <a href="http://cs1dev.ucc.ie/~ecf1/databases/branch.html">Return to Branch Operations Overview</a>
    </h3>
  </div>
    
</body>
<html>
