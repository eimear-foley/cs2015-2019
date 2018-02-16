#!/usr/local/bin/python3

from cgitb import enable
enable()

#imports
import pymysql as db
from cgi import FieldStorage, escape
from datetime import datetime
from os import environ
from hashlib import sha256
from time import time
from shelve import open
from http.cookies import SimpleCookie

#initializations
item_id = ""
price = 0
img_url = ""
img_alt = ""
description = ""
reviews = ""
form_result = ""
star = ""
review_id = ""
curr_time = ""
stock_result = ""
resubmit_review_id = ""
helpful = 0

#opening form_data object
form_data = FieldStorage()

if len(form_data) != 0: #if user/webpage sends us data
    try:
        #validation of form data
        item_id = escape(form_data.getfirst('item','').strip())
        item_id = int(item_id)
        
        star = escape(form_data.getfirst('star','1').strip())
        star = int(star)
        
        username = escape(form_data.getfirst('username','').strip())
        new_review = escape(form_data.getfirst('new_review','').strip())
        review_id = escape(form_data.getfirst('review_id','1').strip())
        
        curr_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S') #gives reviews timestamp
        
        #gives user cookie for unique session
        cookie = SimpleCookie()
        http_cookie_header = environ.get('HTTP_COOKIE') #get cookie headers
        if not http_cookie_header:
            sid = sha256(repr(time()).encode()).hexdigest() #if user does not have cookie give them cookie
            cookie['sid'] = sid
        else:
            cookie.load(http_cookie_header)
            if 'sid' not in cookie:  #if cookie but not the cookie we are looking for give user our cookie
                sid = sha256(repr(time()).encode()).hexdigest()
                cookie['sid'] = sid
            else:
                sid = cookie['sid'].value #if cookie we are looking for get cookie value
        session_store = open('sess_' + sid, writeback=True) #open session

        connection = db.connect('cs1dev.ucc.ie', 'ecf1', 'leethaiw', '2019_ecf1') #connect to db
        cursor = connection.cursor(db.cursors.DictCursor) #create cursor object

        cursor.execute("""SELECT price, img_alt, img_url, description, quantity FROM clothes
                  WHERE item_id = %s """, (item_id))
        #gets various page details e.g. img of clothes, price, description e.t.c
        for row in cursor.fetchall():
            price = row['price']
            img_url = row['img_url']
            img_alt = row['img_alt']
            description = row['description']

            if "check_database" in form_data:
                #adds item to bag and checks database if stock is available
                if row['quantity'] > 0: #if there is stock of of item in database table
                        qty = session_store.get(str(item_id))
                        if not qty:
                            qty = 1 #add item to bag
                        else:
                            qty += 1 #if item already in bag increase quantity by 1
                        session_store[str(item_id)] = qty
                        session_store.close() 
                        stock_result="""<br><br><p>Added to your bag!</p> <a style="color:black;" href="bag.py">Go to checkout.</a>"""
                else:
                    stock_result="""<p style="color:red;">Sorry we are out of stock of that item at the moment!</p>"""
            
        #if user resubmits form data, reset review_id to itself + 1 under new variable name resubmit_review_id 
        #so when the form is resubmitted the new hidden input for review_id in the form will be resubmit_review_id 
        #then the browser will see data has already been inserted into the table in the database for that item
        cursor.execute("""SELECT MAX(review_id) AS review_id FROM review_table""") 
        row = cursor.fetchone()
        try:
            resubmit_review_id = int(row['review_id']) + 1
        except TypeError:
            resubmit_review_id = 1
        
        if "submit_review" in form_data: #only updates review table if submit button clicked
            if new_review == "" or username == "" or star == "": #if user hasn't filled in all information
                form_result = "<p style='color: red;'>Please enter a username, a review and give a star rating!<p>"
            else:
                cursor.execute("""INSERT INTO review_table (username, item_id, review, star, review_id, curr_time, helpful_count)
                                  VALUES (%s, %s, %s, %s, %s, %s, %s)""", (username, item_id, new_review, star, review_id, curr_time, helpful))
                connection.commit() #updates reviews where item_id = X

        cursor.execute("""SELECT * FROM review_table 
                        WHERE item_id = %s
                        ORDER BY review_id DESC""", (item_id))
        #gets back all reviews from review_table and updates item.py?item=X with reviews for that item
        if cursor.rowcount == 0:
            reviews = "" #if there are no reviews for that item
        else: 
            reviews += '<br><h3 class="heading">Reviews</h3><br>' #otherwise gives reviews for item in seperate articles
            for row in cursor.fetchall(): 
                reviews += '<article><h3>%s</h3>  <h3>%s</h3><p>%s</p><span onclick="get_helpful_count(this)"><input type="hidden" value="%i" class="review_id" name="review_id"><p>Helpful? %i <img src="img/thumb-icon.png" alt="thumbs up" height="17" width="17"></p></span><p id="time">%s</p></article><br>' % (row['username'], "&#9733" * row['star'], row['review'], row['review_id'], row['helpful_count'], row['curr_time'])

    except db.IntegrityError: #if user refreshes page, this stops duplicate entries into the database
        form_result = ""
        cursor.execute("""SELECT * FROM review_table 
                        WHERE item_id = %s
                        ORDER BY review_id DESC""", (item_id))
        #gets back all reviews from review_table and updates item.py?item=X with reviews for that item
        if cursor.rowcount == 0:
            reviews = "" #if there are no reviews for that item
        else:
            reviews += '<br><h3 class="heading">Reviews</h3><br>' #otherwise gives reviews for item in seperate articles
            for row in cursor.fetchall(): 
                    reviews += '<article><h3>%s</h3>  <h3>%s</h3><p>%s</p><span onclick="get_helpful_count(this)"><input type="hidden" value="%i" class="review_id" name="review_id"><p>Helpful? %i <img src="img/thumb-icon.png" alt="thumbs up" height="17" width="17"></p></span><p id="time">%s</p></article><br>' % (row['username'], "&#9733" * row['star'], row['review'], row['review_id'], row['helpful_count'], row['curr_time'])

        cursor.close() #close db and cursor connection
        connection.close()

    except (db.Error, ValueError, IOError):
        result = """<p style="color:red;">Sorry we are experiencing problems at the moment please come back later!</p>"""
        
		
print('Content-Type: text/html')
print()

print("""<!DOCTYPE html>
<html lang="en">
    <head>
        <title>iShopClothing</title>
        <meta charset="utf-8">
        <link rel="stylesheet" href="main.css">
        <link rel="stylesheet" href="good.css">
	<link rel="icon" href="img/shopping_cart.PNG">
	<script>

	     var request;
	     var helpful_count;
	     var review_id;
	     var currentSpan;
	     
	     function get_helpful_count(span){
	       review_id = document.getElementsByClassName('review_id');   //gets all hidden inputs
	       var required_input = span.firstChild.value;                 //value of hidden input in span we clicked
	       for (var i = 0; i < review_id.length; i++){                 //go through each item in the list of hidden inputs
	         if (review_id[i].value === required_input){               //check which hidden input is the same as the hidden input of the span we clicked
	           review_id = review_id[i].value;                         //set the value of correct hidden input to the variable review_id
	         }
	       }
               review_id = review_id.toString();            
               currentSpan = span;                        //set the span we clicked to a variable
               helpful_count = span.innerHTML;            //open the inner HTML of the span we clicked
               helpful_count = helpful_count.split(" ");  //use .split(" ") to seperate all the elements of the span into a list of strings
               helpful_count = helpful_count[5];          //get the item in the 5th position of the list which is the helpful_count
               send_request();                            //send request to server
             }

             function send_request(){
               var url = 'helpful.py?review_id=' + review_id;                         //create url with review_id of span we clicked
               request = new XMLHttpRequest();                                        //create and send request
               request.addEventListener('readystatechange', handle_response, false);
               request.open('GET', url, true);
               request.send(null);
             }

             function handle_response(){
               if (request.readyState === 4) {                               //if ready state is 4 and request status is okay and the server returns 'success'
                   if (request.status === 200) {
                     if (request.responseText.trim() === 'success') {
	               helpful_count = Number(helpful_count) + 1             //update the helpful count on the webpage   
	               currentSpan.innerHTML = "<input type='hidden' value='%i' class='review_id' name='review_id'><p>Helpful? " + helpful_count + "<img src='img/thumb-icon.png' alt='thumbs up' height='17' width='17'></p>";
	             }
	  
                   }
       
                }
    
              }
	

	</script>
    </head>
    <body>
	
	    <nav id="top">
		    <div>
			<marquee behavior="scroll" direction="right" scrollamount="15" text-indent="20px">FREE SHIPPING OVER &euro;50 - LIMITED TIME ONLY</marquee>
		    </div>
			<a href="bag.py">My Bag</a>
		</nav>
		<br>
	    <header>
		    <a href="index.html"><img src="img/logo2.PNG" alt="iShopClothing Logo"></a>
		</header>
		<br>
		<nav id="links">
			    <ul>
				    <li><a href="index.html">HOME</a></li>
					<li><a href="dresses.html">DRESSES</a></li>
					<li><a href="bottoms.html">BOTTOMS</a></li>
					<li><a href="tops.html">TOPS</a></li>
					<li><a href="shoes.html">SHOES</a><li>
					<li><a href="accessories.html">ACCESSORIES</a></li>
				</ul>
				
		</nav>
		<br>
		<main>
		    <section>
                        <figure>
			        <img src="%s" alt="%s">
                        </figure>
                
				<div id="pay">
					<p>%s</p>
					<form action="item.py?item=%i" method="post">
						<label for="price">Price: </label>
						<input type="text" value="&euro;%.2f" name="&euro;%.2f" id="price" disabled>
						<br>
						<input type="hidden" value="%i" name="item" id="item"/>                        
						<br>
						<input type="submit" value="Add To Bag" name="check_database">
						%s
					</form>
				</div>
				<br>
		    </section>
		     <br>
                        <section id="review_section">
                            <br>
                            <div id="review">
<h3 class="heading">Customer Review</h3>
<br>
<p>Leave a review and give this item of clothing a rating!</p>
<br>

%s 
<form action="item.py?item=%i" method="post">

<input type="text" name="username" id="username" placeholder="Name">
<br>
<br>
<textarea name="new_review" id="new_review" placeholder="Leave your review here..." rows="5" cols="50">
</textarea>
<br><br>
<label for="star">Give a star rating: </label>
<select name="star" required>
    <option value="1">1</option>
    <option value="2">2</option>
    <option value="3">3</option>
    <option value="4">4</option>
    <option value="5">5</option>
</select>
<input type="hidden" value="%i" name="review_id" id="review_id">
<input type="hidden" value="%i" name="item" id="item">
<br><br>
<input type="submit" value="Submit Review" name="submit_review">
</form>

   %s 
</div>
</section>
		</main>

		<br>
		<footer id="footer">
		         <table id="footer_table">
		                <thead>
		                   <tr>
		                       <th>INFORMATION</th>
		                       <th>HELP</th>
		                       <th>SOCIAL</th>
		                   </tr>
		                </thead>
		                <tbody>
		                   <tr>
		                       <td><a href="">terms &amp; conditions</a></td>
		                       <td><a href="">contact us</a></td>
							   <td style="vertical-align:top;" rowspan="4">
							       <a href="https://www.facebook.com/"><img src="img/facebook.png" height="35" width="35" alt="facebook icon"></a>
							       <a href="https://www.instagram.com/"><img src="img/instagramicon.png" height="35" width="35" alt="instgram icon"></a>
							       <a href="https://twitter.com/?lang=en"><img src="img/twitter_icon.png" height="35" width="35" alt="twitter icon"></a>
								</td>
		                   </tr>
		                   <tr>
		                        <td><a href="">privacy policy</a></td>
		                        <td><a href="">faqs</a></td>
						   </tr>
		                   <tr>
		                        <td></td>
		                        <td><a href="">size guide</a></td>
		                   </tr>
		                   <tr>
		                        <td></td>
		                        <td></td>
		                   </tr>
		                </tbody>
			</table> 
			<p>&copy; iShopClothing</p>
		</footer>
   
    </body>
</html>""" % (int(review_id), img_url, img_alt, description, item_id, price, price, item_id, stock_result, form_result, item_id, resubmit_review_id, item_id, reviews))
