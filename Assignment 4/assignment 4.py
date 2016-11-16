import urllib.request
import json
from pprint import pprint

#Google API Key: AIzaSyC7za9dnqPz90wB-v5O-5UTE-ApNhUrryc
#URL https://maps.googleapis.com/maps/api/geocode/json?address=1600+Amphitheatre+Parkway,+Mountain+View,+CA&key=AIzaSyC7za9dnqPz90wB-v5O-5UTE-ApNhUrryc

#MBTA API: 
#URL http://realtime.mbta.com/developer/api/v2/stopsbylocation?api_key=wX9NwuHnZU2ToO7GmGR9uw&lat=42.346961&lon=-71.076640&format=json

def main():
    user_input = input('Please enter your location:')
    """
    This part of the function is accounting for the spaces for the user input. The URL format for the API uses a '%20' for a space. 
    """
    if ' ' in user_input:
        while ' ' in user_input:
            x = []
            for i in user_input:
                x.append(i)
            while ' ' in x:
                x[x.index(' ')] = '%20'
            user_input = ''.join(x)
    """
    This loads the Google API and uses the user input to search for the longitude and latitude. 
    This also inputs Massachusetts at the end of the search as we are looking for an MBTA stop, which only applies to MA. 
    """
    google_url = "https://maps.googleapis.com/maps/api/geocode/json?address="+user_input+"%20Massachusetts"+"&key=AIzaSyC7za9dnqPz90wB-v5O-5UTE-ApNhUrryc"
    f = urllib.request.urlopen(google_url)
    response_text = f.read().decode('utf-8')
    response_data = json.loads(response_text)
    # pprint(response_data)
    
    """
    This if statement checks to see if there is a Google search result. If there is not, it will ask the user to try again. 
    """

    if response_data['status'] != 'ZERO_RESULTS':
        # print('Function 1: The latitude is %f and the longitude is %f.' %(response_data["results"][0]["geometry"]['bounds']['northeast']['lat'], response_data["results"][0]["geometry"]['bounds']['northeast']['lng']))
        # print('Function 2: The latitude is %f and the longitude is %f.' %(response_data["results"][0]["geometry"]['location']['lat'], response_data["results"][0]["geometry"]['location']['lng']))
        pass
    else:
        print('Your input has 0 results. Please try again.')
        main()

    latitude = str(response_data["results"][0]["geometry"]['location']['lat'])
    longitude = str(response_data["results"][0]["geometry"]['location']['lng'])

    """
    This loads the MBTA API to find the closest MBTA stop. Specifically, this grabs the data from the API. 
    """

    mbta_url = "http://realtime.mbta.com/developer/api/v2/stopsbylocation?api_key=wX9NwuHnZU2ToO7GmGR9uw&lat="+latitude+"&lon="+longitude+"&format=json"
    g = urllib.request.urlopen(mbta_url)
    response_text_mbta = g.read().decode('utf-8')
    response_data_mbta = json.loads(response_text_mbta)
    # pprint(response_data_mbta)

    """
    This statement checks to see if there is a result from the MBTA API. If there is not, it will ask the user if they want to run the function again. If they do, the function will run again. 
    If there is, this will continually run to find a complete result with a complete parent station name and stop name.  
    """

    if response_data_mbta['stop'] != []:
        z = 0
        mbta_station_name = response_data_mbta['stop'][z]['parent_station_name']
        mbta_stop_name = response_data_mbta['stop'][z]['stop_name']
        while mbta_station_name == '' or mbta_stop_name == '':
            z += 1
            mbta_station_name = response_data_mbta['stop'][z]['parent_station_name']
            mbta_stop_name = response_data_mbta['stop'][z]['stop_name']
        print('The closest MBTA stop to your location is %s at the %s Station.' %(mbta_stop_name, mbta_station_name))
    elif response_data_mbta['stop'] == []:
        try_again = input("There are no nearby stops. Would you like to try again? (Y/N) ")
        if try_again.lower() == "y" or try_again.lower() == "yes" or try_again.lower() == "ye" or try_again.lower() == "ya" or  try_again.lower() =="fo sho":
            main()
        else:     
            pass

main()