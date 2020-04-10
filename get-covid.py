import argparse
import requests
import json
import os


def main():
    
    url = "https://covid-19-coronavirus-statistics.p.rapidapi.com/v1/stats"

    querystring = {"country": args.country}

    API_KEY = os.environ.get('API_KEY')

    headers = {
        'x-rapidapi-host': "covid-19-coronavirus-statistics.p.rapidapi.com",
        'x-rapidapi-key': API_KEY
        }

    response = requests.request("GET", url, headers=headers, params=querystring)

    json_data = json.loads(response.text)

    #print(json_data['data']['covid19Stats'])

    print('\t'.join(['Province', 'Country', 'Confirmed', 'Deaths']))

    for data in json_data['data']['covid19Stats']:

        print( data['province'],"\t", data['country'],"\t",data['confirmed'],"\t",data['deaths'])



if __name__ == '__main__':
    parser = argparse.ArgumentParser( description="A Covid-19 reporting tool")

    parser.add_argument('-c', '--country', action='store',
    help='A Country name',
    required=False,
    default='Canada')

    args = parser.parse_args()
    main()