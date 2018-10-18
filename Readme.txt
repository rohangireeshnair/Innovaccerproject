Technical Details:
        1.)Install Python3 and its following modules 
                                                        1.) beautifulSoup4/bs4
                                                        2.) urllib3
                                                        3.) email
        2.)The script uses an API called OMDB to identify the Imdb tittle of the tv show for accessing the appropriate webpage of Imdb.        
        3.)Enter the credentials of the database in dbinit.py
        4.)Start the script by executing Innovaccer.py 
        5.)Enter the Email and Enter the tv shows in a single line separated by commas(‘) without space between the tv shows and the comma


        6.)The script adds the data to the database and gives you an option to send the emails to all the emails addresses in database after each addition of data.
        7.) A background thread is also initialised by the script which send emails to the users in the database each day after checking the  Imdb  for any update in the airdates of the shows.
        8.) The script uses a gmail email id ‘showsreminderinnovaccer@gmail.com’ with password ‘innovaccer1@’, which can be changed in emailer.py.