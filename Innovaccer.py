import dbinit
import dbcheck
import backdbcheck
import sys

# Getting the cursor through dbinitiate
try:
    mydb=dbinit.initiate()
    dbcursor = mydb.cursor()
    thread = dbcheck.dbcheckc(1, "dbcheck", 1)
    thread.start()



    while (True):
        email = input("Enter the email address")
        showstring = input("Enter the tv shows")
        showlist = showstring.split(",")
        sql = None
        for x in showlist:
            sql = "INSERT INTO showstable (email, show1) VALUES (%s, %s)"
            # val = ('{},{}' .format(email, x))
            val = (email, x)
            dbcursor.execute(sql, val)
            mydb.commit()

        print('The email and shows are added to database')
        response = input("Do you want to send the mails to all the entries now?. Enter yes/no")
        if(response=='yes'):
            backdbcheck.backdbcheck() #Each time a new entry is added mail is sent to the entire entry in database.
except KeyboardInterrupt:
    sys.exit(0)