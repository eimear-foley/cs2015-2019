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
	<h3>Record a new staff member's details.</h3>
	<section id="operations">
	    <form method="post">
		Staff No.:<br>
		<input type="text" value="" name="staff_no" maxlength="4"><br><br>
		First Name: <br>
		<input type="text" value="" name="fname"><br><br>
		Last Name: <br>
		<input type="text" value="" name="lname"><br><br>
		Address: <br>
		<input type="text" value="" name="address"><br><br>
		Telephone: <br>
		<input type="text" value="" name="telephone" maxlength="13" placeholder="1234-567-8910"><br><br>
		Position: <br>
		<select name="position" required>
		  <option value="Manager">Manager</option>
		  <option value="Deputy">Deputy</option>
		  <option value="Assistant">Assistant</option>
		  <option value="Snr Asst">Senior Assistant</option>
		</select><br><br>
		Sex: Male <input type="radio" name="sex" value="M" checked> Female <input type="radio" name="sex" value="F">
		<br><br>
		DOB: <br>
		<input type="date" value="" name="dob"><br><br>
		Salary: <br>
		<input type="number" min="9000" max="50000" name="salary"><br><br>
		NIN: <br>
		<input type="text" value="" name="nin" maxlength="9"><br><br>
		Branch No.: B3 <input type="radio" name="bno" value="B3" checked> B5 <input type="radio" name="bno" value="B5"> B7 <input type="radio" name="bno" value="B7"> B4 <input type="radio" name="bno" value="B4"> B2 <input type="radio" name="bno" value="B2"><br><br>
		<input type="submit" value="Add new staff member">
	    </form>
	    <br>
	<?php
	  include "dream_setup.php";
	  dream_connect() or exit();

	  if ($_POST){
		$staff_no = $_POST['staff_no'];
		$fname = $_POST['fname'];
		$lname = $_POST['lname'];
		$address = $_POST['address'];
		$telephone = $_POST['telephone'];
		$position = $_POST['position'];
		$sex = $_POST['sex'];
		$dob = $_POST['dob'];
		$salary = intval($_POST['salary']);
		$nin = $_POST['nin'];
		$bno = $_POST['bno'];
		if ($staff_no && $fname && $lname && $address && $telephone && $position && $sex && $dob && $salary && $nin && $bno){
			$insert= "INSERT INTO staff VALUES('".$staff_no."', '".$fname."', '".$lname."', '".$address."', '".$telephone."','".$position."', '".$sex."', '".$dob."', '".$salary."', '".$nin."', '".$bno."')";
			$result = mysql_query($insert)
				or exit("Cannot execute insert");
			if ($result){
				echo("<p> New staff member " .$fname. " " .$lname. " now works at branch number " .$bno. ".</p>");
			} else {
				echo("<p>New staff member could not be added to database.</p>");
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
