#!/usr/local/bin/python3

from cgi import FieldStorage, escape
import pymysql as db

print('Content-Type: text/plain')
print()

form_data = FieldStorage()

if len(form_data) != 0: #if the user has sent us data
    try:
        review_id = escape(form_data.getfirst('review_id').strip()) #get and validate review_id
        review_id = int(review_id) #make integer

        connection = db.connect('cs1dev.ucc.ie', 'ecf1', 'leethaiw', '2019_ecf1') #connect to db
        cursor = connection.cursor(db.cursors.DictCursor) #create cursor object

        cursor.execute("""UPDATE review_table
                          SET helpful_count = helpful_count + 1 
                          WHERE review_id = %s""", (review_id)) #update the table with the new helpful_count
        connection.commit() 
        print('success')
        cursor.close()  
        connection.close()
    except (ValueError, db.Error):
        print('problem')
