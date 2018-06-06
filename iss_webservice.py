#import stuff
import urllib.request
import json
import webbrowser
import time

on = True

while on:
    choice = input('Welcome to Jack\'s ISS extraviganza! For the current location press 1. To find out when it will be overhead press 2:  ' )
    # Who is in what space craft?
    if choice == '1':
        url = 'http://api.open-notify.org/astros.json'
        response = urllib.request.urlopen(url)
        result = json.loads(response.read())

        people = result['people']
        for i in people:
            print(i['name'],'in',i['craft'], sep=' ')
    
        # Where is the ISS
    
        positionurl = 'http://api.open-notify.org/iss-now.json'
        positionresponse = urllib.request.urlopen(positionurl)
        positionresult = json.loads(positionresponse.read())

        if positionresult['message'] == 'success' :
            iss_position = positionresult['iss_position']
            print('Long:',iss_position['longitude'],'Lat:',iss_position['latitude'])
            searchurl = 'https://www.google.co.uk/maps/place/'+iss_position['latitude']+'+'+iss_position['longitude']
            webbrowser.open(searchurl, new=2)
            
        choice2 = input('search again? (Y/N) ')
        if choice2 =='N' or choice2 =='n':
            on = False
            
    elif choice =='2':
        try:
            locationlat = float(input('What is your latitude? '))
            locationlong = float(input('What is your longitude? '))
            url =  'http://api.open-notify.org/iss-pass.json?lat='+str(locationlat)+'&lon='+str(locationlong)
            response = urllib.request.urlopen(url)
            result = json.loads(response.read())
            over = result['response'][1]['risetime']
            print('The next time you can see the ISS is: ',time.ctime(over))
            
        except ValueError:
            print('That is not a number you dick')

        choice2 = input('search again? (Y/N) ')
        if choice2 =='N'or choice2 =='n':
            on = False
    
    else: print('FUCK OFF and choose a valid option')
        
 