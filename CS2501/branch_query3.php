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
  <h3>Find all staff members working at a given branch.</h3>
  <section id="operations">
  <br>
  <form method="post">
    Branch No.: B3 <input type="radio" name="bno" value="B3" checked> B5 <input type="radio" name="bno" value="B5"> B7 <input type="radio" name="bno" value="B7"> B4 <input type="radio" name="bno" value="B4"> B2 <input type="radio" name="bno" value="B2">
    <br><br>
    <input type="submit" value="Get Staff Members">
  </form>
  <br>
  
  <?php
  include "dream_setup.php";
  dream_connect() or exit();
  
  if ($_POST){
    $bno = $_POST['bno'];
    $query = ("SELECT staff.Fname, staff.Lname FROM staff JOIN branch WHERE branch.Bno = '".$bno."' AND staff.Bno = branch.Bno");
    $result = mysql_query($query)
      or die("cannot execute query");
    $outstring = "<p>Staff Members working at branch number " .$bno. " are:</p>";
    $outstring .= "<table><tr><th>First Name</th><th>Last Name</tr>";
    while ($row = mysql_fetch_assoc($result)){
	$outstring .= ("<tr><td>" .$row[Fname]. "</td><td>" .$row[Lname]. "</td></tr>");
    }
    $outstring .= "</table>";
    echo($outstring);
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