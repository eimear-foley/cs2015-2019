Project Outline:

I have created an online womens clothing store.
This website consists of 6 HTML webpages, 5 CSS scripts, 5 python server-side programs, 2 javascript client-side programs (one of which is inside the <head> of item.py) and 2 database tables.

Summary of Files:

MAIN.CSS: 
This is my main css file; it is used in all the webpages in my website and consists of the design for the footer and header.

INDEX.HTML: 
This is the homepage of my website. It uses index.css.

ACCESSORIES.HTML, BOTTOMS.HTML, DRESSES.HTML, SHOES.HTML, TOPS.HTML: 
These webpages are linked in the header of my website and each webpage uses the category.css file to design the layout of the options available to buy under each category.

ITEM.PY: 
This is a self-processing page with two sticky forms. 
It uses the GOOD.CSS file to design the layout of all the elements belonging to the webpage. 
Both item.py and good.css are fully commented for a more in depth description of what they both do.

In bullet point form however, I will give a short(ish) outline of the different tasks item.py completes:

-gives user cookie and unique session store
-connects to the database
-uses a mysql query on the database table 'clothes', see CLOTHES3.SQL, to pull the relevant information on the item which we are viewing i.e. image of item, description of item e.t.c
-if the user clicks 'add to bag' this submits the form with the item information and checks if it is available to buy or not
-if not, an apology is returned with the rest of the page
-otherwise it adds the item_id of that item to your session store with the quantity 1 or if the item is already in your bag it increases the quantity by 1
-makes a form available to the user in order to make a review of the item
-the review is stored in the database table 'review_table', see REVIEW_TABLE.SQL
-the user's review contains their username, review, the star rating they gave the item of clothing and a timestamp. 
-the review also contains a 'Helpful?' "button". 
-this "button" is a <span> and contains the attribute "onclick='get_helpful_count(this)'"
-this runs the javascript program in the head of the item.py file (this program is also fully commented for a more in-depth understanding of how the program works)
-using AJAX this program sends a request to HELPFUL.PY which updates the database table 'review_table' to set 'helpful_count' to itself plus 1
-after the javascript receives responseText under the condition that "responseText.trim() === 'success'" then it updates the webpage 

I would also like to point out a speacial feature which I am particularly proud of: 
Upon refreshing item.py after making a review, the browser would resubmit the form data leading to duplicate reviews on the webpage and in my database table 'review_table'. To overcome these issues I used a query to the database to find the 'MAX(review_id)' i.e. the most recent review, and reset the value of the review_id to itself plus 1 under a new variable 'resubmit_review_id' and I then call this variable in the form using string formatting instead of review_id so that when the page is refreshed after making a review the browser thinks the review has already been made. For example I make a review with 'review_id='8'', item.py then sets the variable 'resubmit_review_id' to equal '9' so when the browser tries to resubmit the form data it thinks that a review with an id equalling 9 has already been made.

I would also like to note there is one issue I have identified with the 'Helpful?' "button" is that there is nothing from stopping one user upvoting the same review multiple times. To overcome this issue I would have to introduce a log-in system inserting a condition that the user can only upvote a review if they have an account and then store whether this user has already given a upvote on the review or not. However as this feature was added in the later stages of the continous assessment to my website there was not enough time to add a log-in system. I have decided to keep the 'Helpful?' feature however to showcase my use of javascript and the use of AJAX to connect to the server-side Python program.

BAG.PY: 

This is a self-processing page and contains a sticky form containing checkboxes.
bag.py uses BAG.CSS to design the table displaying the items in the bag or nothing if the session store is empty and the "button" to pay for the items in the bag.
It also calculates the total price the user must pay taking into account if the user must pay shipping or not.
This webpage also runs a javascript program, REMOVE.JS - (see comments in remove.js for in-depth description) - upon clicking the 'remove from bag' button and sends a request to REMOVE.PY to the remove the items from the session store that the user has chosen to remove from the bag. If remove.js receives 'success' only in the responseText it will update the webpage to remove the table row containing that item from the bag.

UPDATED_BAG.PY:

This program empties the session store and thanks the user for shopping and returns them to their now empty bag.

I would like to note one issue with the css for bag.py and updated_bag.py, the css for the footer does not appear to be working on these two webpages however they do work for all other webpages. I have appeared to have closed all my tags in my html for these two webpages so I am uncertain as to how this issue has arisen.

Issues Regarding Copyright:

All images of clothing displayed have been taken from asos.com and I give full copyright to asos for each of these images.
The browser icon I made myself.
The website logo was created using a font downloaded from http://www.dafont.com/
The social media icons in the footer and the thumbs up icon on the item.py?item=X pages were taken from google images under a search for images that were "free to use or share, even commercially".
Credit owed for CSS techniques to align images side by side (with and without captions) belong to http://hubpages.com/technology/how-to-align-images-side-by-side .
Credit owed for CSS techniques for pop up button on bag.py/updated_bag.py belong to http://www.sevensignature.com/blog/code/pure-css-popup-without-javascript/
 
All other items are of my own work or design.