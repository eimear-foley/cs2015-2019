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
     
    if len(session_store) == 0: #if session is empty return empy bag
        result = '<p>No items in shopping cart.</p>'
        result += """<br><br><div style="margin-left: 0%;" id="box" style="margin-right: 80%;">
                        <a id="button" href="index.html">Continue Shopping</a>
                   </div>"""
        result += '<div style="height:320px; width:600px;"></div>'
        
    else: #otherwise connect to db to get relevant info about items chosen by user
        connection = db.connect('cs1dev.ucc.ie', 'ecf1', 'leethaiw', '2019_ecf1') #connect to db
        cursor = connection.cursor(db.cursors.DictCursor) #create cursor object

        result = """<form id="bag" action="bag.py" method="post">
		    <table id="table"> 
                    <tr><th colspan="5" id="top">Your Bag</th></tr>
                    <tr><th>Item</th><th>Quantity</th><th>Price</th><th>Remove From Bag</th></tr>
                    """
                    #give result in table format
        
        price = 0
        for item_id in session_store: 
            cursor.execute("""SELECT description, price, img_url, img_alt FROM clothes
                               WHERE item_id = %s""", (item_id))
            row = cursor.fetchone()
            
            result += """<tr>
			  <td><a href="item.py?item=%i"><img src="%s" alt="%s" width="75" height="75"></a><p>%s</p></td>
			  <td>%i</td>
			  <td>&euro;%5.2f</td>
			  <td><input type="checkbox" value="%s" name="item_id" class="item_id"></td>
			</tr>""" % (int(item_id), row['img_url'],row['img_alt'],row['description'], session_store.get(item_id), row['price']*session_store.get(item_id), item_id)
            price += (row['price']*session_store.get(item_id)) #price of good times quantity of good chosen
        result += """<tr>
		    <td style="font-weight: bold; text-align: left;">Merchandise Total</td>
		    <td></td>
		    <td>&euro;%6.2f</td>
		    <td rowspan="3"><button id="remove">Remove From Bag</button></td>
		  </tr>""" % (price)

        if price > 50: #this section of code refers to offer for free shipping over 50 euro
            shipping = 0
            result += """<tr>
			<td style="font-weight: bold; text-align: left;">Shipping</td>
			<td></td>
			<td>&euro;%5.2f</td>
		      </tr>""" % (shipping)
        else:
            shipping = 6
            result += """<tr>
			<td style="font-weight: bold; text-align: left;">Shipping</td>
			<td></td>
			<td>&euro;%5.2f</td>
		      </tr>""" % (shipping)
        total = price + shipping #gives user shopping total
        result += """<tr>
		    <td style="font-weight: bold; text-align: left;">Total</td>
		    <td></td>
		    <td style="font-weight: bold;">&euro;%6.2f</td>
		  </tr>""" % (total)
        result += '</table></form>'
        result += """<br>
                     <div id="box">
                        <a id="button" href="updated_bag.py#popup">Pay now!</a>
                    </div>"""
        cursor.close()  #close db and cursor connection
        connection.close()
    session_store.close() #close session connection
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
        <script src="remove.js"></script>
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
                      <div style="width: 1000px height: 350px"></div>
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
            <p style="background-color:black;">&copy; iShopClothing</p>
        </footer>
         </body>
</html>""" % (result)) 
