import  dbinit
import webcheck

def backdbcheck():
    mydb = dbinit.initiate()
    dbcursor = mydb.cursor()
    dbcursor.execute("SELECT * FROM showstable ")
    result = dbcursor.fetchall()
    shows = []
    i=0;
    for x in result:
        curemail = x[0]
        shows.append(x[1])
        length=len(result)
        if(length-i>1):
            if(curemail==result[i+1][0]):
                i=i+1
                continue
            else:
                webcheck.webcheck(curemail, shows)
                shows.clear()
                i=i+1
        else:
            webcheck.webcheck(curemail, shows)
            shows.clear()
            i = i + 1
    return





