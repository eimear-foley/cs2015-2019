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
		margin-right: auto;
		border: 1px solid black;
		padding: 1em;
	    }
	    table, tr, td, th{
		border-collapse: collapse;
		padding: .5em;
		border: 1px solid black;
	    }
	     #return{
		text-align: center;
		margin-top: 1em;
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
	<h3>Find the address of the branch employing a staff member</h3>
	<section id="operations">
	    <form method="post">
		First Name: <br>
		<input type="text" value="" name="fname"><br><br>
		Last Name: <br>
		<input type="text" value="" name="lname"><br><br>
		<input type="submit" value="Find Branch Address">
	    </form>
	    <br>
	<?php
	  include "dream_setup.php";
	  dream_connect() or exit();

	  if ($_POST){
		$fname = $_POST['fname'];
		$lname = $_POST['lname'];
		if ($lname && $fname){
			$query = "SELECT branch.Street, branch.Area, branch.City FROM staff JOIN branch WHERE staff.Fname = '".$fname."' AND staff.Lname = '".$lname."' AND staff.Bno = branch.Bno";
			$result = mysql_query($query)
				or die("Cannot execute query");
			if (mysql_num_rows($result) > 0){
				$outstring = "<p>Staff member " .$fname. " " . $lname . " works at:</p>";
				$row = mysql_fetch_assoc($result);
				$outstring .= "<p>Branch Address: " .$row[Street]. ", " .$row[Area]. ", " .$row[City]. "</p>";
				echo($outstring);
			} else {
				echo("<p>Staff member does not exist or incorrect name.</p>");
			}
		} else {
			echo("<p>Please enter a staff member's name.</p>");
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
