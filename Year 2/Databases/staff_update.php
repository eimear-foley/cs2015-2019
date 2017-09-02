<!DOCTYPE html>
<head>
	<title>Staff Update</title>
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
	<h3>Promote/Demote a staff member.</h3>
	<section id="operations">
	    <form method="post">
		Staff No.:<br>
		<input type="text" value="" name="staff_no" maxlength="4"><br><br>
		New Position: <br>
		<select name="position" required>
		  <option value="Manager">Manager</option>
		  <option value="Deputy">Deputy</option>
		  <option value="Assistant">Assistant</option>
		  <option value="Snr Asst">Senior Assistant</option>
		</select><br><br>
		<input type="submit" value="Promote/Demote Staff Member">
	    </form>
	    <br>
	<?php
	  include "dream_setup.php";
	  dream_connect() or exit();

	  if ($_POST){
		$staff_no = $_POST['staff_no'];
		$position = $_POST['position'];
		if ($staff_no && $position ){
			$update = "UPDATE staff SET Position = '".$position."' WHERE Sno = '".$staff_no."'";
			$result = mysql_query($update)
				or exit("Cannot execute query");
			if ($result){
				$query = "SELECT Fname, Lname FROM staff WHERE Sno = '".$staff_no."'";
				$result = mysql_query($query)
				  or exit("Cannot execute query");
				$row = mysql_fetch_row($result);
				echo("<p>" .$row[0]. " " .$row[1]. " is now a " .$position. ".</p>");
			} else {
				echo("<p>Staff member's position could not be changed.</p>");
			}
		} else {
			echo("<p>Please enter the correct details.</p>");
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
