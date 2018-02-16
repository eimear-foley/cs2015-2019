(function(){
  var remove_item = [];
  var request;
  var checkboxes;
  
  document.addEventListener('DOMContentLoaded', init, false)
  
  function init(){  
    var remove_button = document.getElementById('remove');              //get remove button on bag.py
    checkboxes = document.getElementsByClassName('item_id');            //get the hidden input with all the item_id's in the checkboxes
    if (checkboxes.length !== 0){                                       //if the bag ISN'T empty add an event listener
      remove_button.addEventListener('click', testCheckbox, false);
    }
  }
  
  function testCheckbox(){                                   
    for (var item = 0; item < checkboxes.length; item++)   //test all the items in the list 'checkboxes' to see if they're checked or not
      if (checkboxes[item].checked){
	remove_item.push(checkboxes[item].value)           //if they're checked add them to list remove_item
      }
      send_request();                                      //send request to server
    }
  
  function send_request(){
    var url = 'remove.py?item_id=' + remove_item[0];       //create url setting item_id to first item in list remove_item
    for (var i = 1; i < remove_item.length; i++){          //add all other items to the url 
      url += '&item_id=' + remove_item[i];
    }
    request = new XMLHttpRequest();                        //create and send request
    request.addEventListener('readystatechange', handle_response, false);
    request.open('GET', url, true);
    request.send(null);
  }

  function handle_response(){
    if (request.readyState === 4) {                           //if ready state is 4, request status is OK and server return 'success'
       if (request.status === 200) {
          if (request.responseText.trim() === 'success') {
	    for (var i = 0; i < remove_item.length; i++){                   //for each item in our remove_item list
	      for (var item = 0; item < checkboxes.length; item ++){        
		if (remove_item[i] === checkboxes[item].value){             //get the corresponding checkbox
		  var tbody = checkboxes[item].parentNode.parentNode.parentNode;      //get the <tbody> which is the great grandparent of the checkbox
		  var trow = checkboxes[item].parentNode.parentNode;                  //get the <tr> which is the grandparent of the checkbox
		  tbody.removeChild(trow);                                            //delete the <tr> as to update the webpage to show this item has been removed from the bag
		}
	      }
	    }
          }
       }
    }
  }

	    
}) ();