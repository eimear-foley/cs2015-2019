<!DOCTYPE html>
<head>
  <title>Branch Update</title>
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
  <h3>Record the details of branch relocation.</h3>
  <section id="operations">
  <br>
  <form method="post">
    Branch No.: B3 <input type="radio" name="bno" value="B3" checked> B5 <input type="radio" name="bno" value="B5"> B7 <input type="radio" name="bno" value="B7"> B4 <input type="radio" name="bno" value="B4"> B2 <input type="radio" name="bno" value="B2">
    <br><br>
    New Address: <br>
    Street: <input type="text" value="" name="street"><br>
    Area:   <input type="text" value="" name="area"><br>
    City:   <input type="text" value="" name="city"> <br><br>
    <input type="submit" value="Update Branch Location">
  </form>
  <br>
  
  <?php
  include "dream_setup.php";
  dream_connect() or exit();
  
  if ($_POST){
    $bno = $_POST['bno'];
    $street = $_POST['street'];
    $area = $_POST['area'];
    $city = $_POST['city'];
    if ($bno && $street && $area && $city){
      $query = ("UPDATE branch SET Street = '".$street."', Area = '".$area."', City = '".$city."' WHERE Bno = '".$bno."'");
      $result = mysql_query($query)
	or die("cannot execute query");
      if ($result){
	echo("<p>Update successful.</p>");
	echo("<p>Branch number " .$bno. " now has address: " .$street. ", " .$area. ", " .$city. ".</p>");
      } else {
	echo("<p>Update unsuccessful.</p>");
      }
    } else {
      echo("<p>Please enter a correct address.</p>");
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
