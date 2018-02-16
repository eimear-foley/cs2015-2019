#!/usr/local/bin/python3

from cgitb import enable 
enable()

from os import environ
from hashlib import sha256
from time import time
from shelve import open
from http.cookies import SimpleCookie
import pymysql as db

result = ''
try:
    #gives user cookie for unique session
    cookie = SimpleCookie()
    http_cookie_header = environ.get('HTTP_COOKIE') #get cookie headers
    if not http_cookie_header: 
        sid = sha256(repr(time()).encode()).hexdigest()
        cookie['sid'] = sid #if user does not have cookie give them cookie
    else:
        cookie.load(http_cookie_header)
        if 'sid' not in cookie: #if cookie but not 'sid' then give user cookie
            sid = sha256(repr(time()).encode()).hexdigest()
            cookie['sid'] = sid
        else:    
            sid = cookie['sid'].value #if cookie we are looking for get cookie value
    session_store = open('sess_' + sid, writeback=True) #open session

    if len(session_store) == 0: #if shopping cart is empty return empty bag
        result= """<p>No items in shopping cart.</p>
                   <br>
                   <div class="box" style="margin-right: 80%;">
                        <a class="button" href="index.html">Continue Shopping</a>
                   </div>"""
    else: #otherwise connect to db to update it
        connection = db.connect('cs1dev.ucc.ie', 'ecf1', 'leethaiw', '2019_ecf1') #connect to db
        cursor = connection.cursor(db.cursors.DictCursor) #create cursor object

        for item_id in session_store:

            cursor.execute("""UPDATE clothes
                                SET quantity = quantity - %s
                                    WHERE item_id = %s """, (session_store.get(item_id), item_id))
            del session_store[item_id] #delete items in session storage so when user returns to bag it will still be empty

            #return empty bag and popup thanking user for shopping at our site
            result = """<p>No items in shopping cart.</p> 
                        <br><br>
                        <div style="margin-left: 0%;" id="box" style="margin-right: 80%;">
                            <a id="button" href="index.html">Continue Shopping</a>
                        </div>"""
            result += """<div id="popup" class="overlay">

                                <div class="pop_up">
                                    <h3>Payment Confirmed</h3>
                                        <a class="close" href="#">x</a>
                                    <div class="content">Thank you for shopping with <i>iShopClothing</i></div>
                                    </div>
                                </div>"""
        connection.commit()        
        cursor.close()  
        connection.close()
    session_store.close()
    print(cookie)
except (db.Error, IOError):
    result = '<p>Sorry! We are experiencing problems at the moment. Please call back later.</p>'

print('Content-Type: text/html')
print()

print("""<!DOCTYPE html>
<html lang="en">
    <head>
        <title>iShopClothing</title>
        <meta charset="utf-8">
        <link rel="stylesheet" href="bag.css">
        <link rel="stylesheet" href="main.css">
	<link rel="icon" href="img/shopping_cart.PNG">
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
                      %s
                      <br>
                      <div id="space" style="width: 1000px; height: 350px;"></div>
                </main>
                <br>
		<footer id="footer" style="background: black;">
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
			<p style="background: black;">&copy; iShopClothing</p>
		</footer>
         </body>
</html>""" % (result)) 
