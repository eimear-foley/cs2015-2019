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
	<h3>Find the staff number, last name and first name of those earning more or less than a given salary.</h3>
	<section id="operations">
	    <form method="post">
		Salary is...<br>
		Less <input type="radio" value="<" name="salary" checked> More <input type="radio" value=">" name="salary"><br><br>
		..than <input type="text" value="" name="amount"><br><br>
		<input type="submit" value="Find staff member">
	    </form>
	    <br>
	<?php
	  include "dream_setup.php";
	  dream_connect() or exit();

	  if ($_POST){
		$salary = $_POST['salary'];
		$amount = $_POST['amount'];
		if ($amount && $amount > 0){
			if ($salary == "<"){
				$query = ("SELECT Fname, Lname, Sno FROM staff WHERE Salary < '".$amount."'");
			} else {
				$query = ("SELECT Fname, Lname, Sno FROM staff WHERE Salary > '".$amount."'");
			}
			$result = mysql_query($query)
				or die("Cannot execute query");
			if (mysql_num_rows($result) > 0){
				$outstring = "<p>Staff members earning " .$salary. " " . $amount . " are:</p>";
				$outstring .= "<table><tr><th>First Name</th><th>Last Name</th><th>Staff Number</th></tr>";
				while ($row = mysql_fetch_assoc($result)){
					$outstring .= ("<tr><td>" .$row[Fname]. "</td><td>" .$row[Lname]. "</td><td>" .$row[Sno]. "</td></tr>");
				}
				$outstring .= "</table>";
				echo($outstring);
			} else {
				echo("<p>No staff member earns in that salary range.</p>");
			}
		} else {
			echo("<p>Please enter a numerical value.</p>");
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
