import urllib3
import json
from bs4 import BeautifulSoup
import re
import emailer
import datetime
import time
def webcheck(email, shows):
    monthdict = {'Jan.': '01', 'Feb.': '02', 'Mar.': '03', 'Apr.': '04', 'May.': '05', 'Jun.': '06', 'Jul.': '07', 'Aug.': '08', 'Sep.': '09', 'Oct.': '10', 'Nov.': '11', 'Dec.': '12'}
    http = urllib3.PoolManager()
    msg = ''
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    for show in shows:
        request = ('http://www.omdbapi.com/?apikey=2a92affd&t={}'.format(show))
        request = request.replace(" ", "%20")
        req = http.request('GET',request)
        reply = json.loads(req.data.decode('utf-8'))
        if(reply.get("Response")=='True'):
            title = reply.get("imdbID")
            year = reply.get("Year")
            totseason = reply.get("totalSeasons")
            if(len(year)==9):
                yearend = year.split(year[4])
                yearend = yearend[1]
                msg = msg + 'Tv series name : {} \n'.format(reply.get("Title"))
                msg = msg + 'The show had finished streaming all its episodes in {} \n\n\n'.format(yearend)
            else:
                try:
                    url = 'https://www.imdb.com/title/{}/episodes?season={}'.format(title, int((totseason), 10)+1)
                    #Here total season is increased by one because sometimes even when new season isn't released imdB page might exits even though omdB api returns one less season, and even if the season number in query is increased by 1 imdb returns the web page of the latest season.
                except:
                    url = 'https://www.imdb.com/title/{}/episodes?season={}'.format(title, totseason)#incase totseason isn't string
                req = http.request('GET', url)
                if(req.status==200):
                    soup = BeautifulSoup(req.data, 'html.parser')
                    airdate_box = soup.find_all('div', attrs={'class':'airdate'})
                    match = re.findall('\d{2} \w{3}. \d{4}|\d{1} \w{3}. \d{4}', str(airdate_box))
                    match2 = re.findall('\d{2} \w{3}. \d{4}|\d{1} \w{3}. \d{4}|\w{3}. \d{4}|\d{4}', str(airdate_box))
                    match1 = re.findall('airdate', str(airdate_box))
                    datetoday = datetime.date.today().strftime('%Y-%m-%d')
                    datetoday1 = time.strptime(datetoday, '%Y-%m-%d')
                    if(len(match)==0): #this means only year for the release of next season is mentioned
                        yearmatch = re.findall('\d{4}', str(airdate_box))
                        releaseyear = yearmatch[0]
                        msg = msg + 'Tv series name : {} \n'.format(reply.get("Title"))
                        msg = msg + 'The next season begins in {} \n\n\n'.format(releaseyear)
                    else:
                        if((len(match1)>len(match))&(len(match1)!=len(match2))):   #In this case imdB hasn't released the date of next episode/season
                            msg = msg + 'Tv series name : {} \n'.format(reply.get("Title"))
                            msg = msg + "IMDB hasn't announced the airdate of the next episode/season \n\n\n"

                        if(len(match1)==len(match2)):
                            for y in match2:
                                splitairdate = y.split(" ")
                                if(len(splitairdate)==3):
                                    msgairdate = splitairdate[2]+"-"+monthdict.get(splitairdate[1])+"-"+splitairdate[0]
                                    thisdate = time.strptime(msgairdate, '%Y-%m-%d')
                                    if(thisdate>datetoday1):
                                        msg = msg + 'Tv series name : {} \n'.format(reply.get("Title"))
                                        msg = msg + 'Next episode airs on {}\n\n\n'.format(msgairdate)
                                        break
                                if (len(splitairdate) == 2):
                                    msg = msg + 'Tv series name : {} \n'.format(reply.get("Title"))
                                    msg = msg + 'Next episode airs on {}\n\n\n'.format(y)
                                    break

    emailer.sendemail(email, msg)

