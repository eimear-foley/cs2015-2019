<!DOCTYPE html>
<head>
  <title>Staff Query</title>
  <style>
    body{
      background-color: white;
      font-family: 'Century Gothic', CenturyGothic, AppleGothic, sans-serif;
    }
    
    h3{
      color: #33a1de;
      text-align: center;
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
  <h3>Return name of staff member by staff number</h3>
  <section id="operations">
  <br>
  <form method="post">
    Staff No.:<br>
    <input type="text" name="staff_no" maxlength="4" value="">
    <br><br>
    <input type="submit" value="Get Name">
  </form>
  <br>
  
  <?php
  include "dream_setup.php";
  dream_connect() or exit();
  
  if ($_POST){
    $staff_no = $_POST['staff_no'];
    $query = ("SELECT `Fname`, `Lname` FROM `staff` WHERE Sno = '".$staff_no."'");
    $result = mysql_query($query)
      or die("cannot execute query");
    $row = mysql_fetch_row($result);
    if ($row){
      echo("<p>Staff member with staff no. " .$staff_no. " is: </p>");
      echo("<p>Name: " . $row[0] . " " . $row[1] . "</p>");
    } else {
      echo("<p>No staff member with staff number " . $staff_no . " exists.</p>");
    }
  }
  ?>
  </section>
  <div id="return">
    <h3>
      <a href="http://cs1dev.ucc.ie/~ecf1/databases/staff.html">Return to Staff Operations Overview</a>
    </h3>
  </div>
    
</body>
<html>
