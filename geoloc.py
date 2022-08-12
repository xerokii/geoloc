import csv
import urllib3
import requests
import json
from csv import DictReader
import pycountry
from ipaddress import IPv4Address

apikey = ##YOUR OWN API KEY FROM IPINFO.IO##
file = ##PATH OF YOUR CSV##
 
header=(['Address','Country','Events'])
with open('ipinfo_output.csv','w', newline='') as output:
    writer = csv.writer(output)
    writer.writerow(header)

with open (file,'r') as file_csv:
    read_csv = DictReader(file_csv)
    for row in read_csv:
        addr = IPv4Address(row['IP'])
        if addr.is_private == False:
            urlsource="https://ipinfo.io/"+row['IP']+"?token="+apikey

            response = requests.request("GET", urlsource)
            decodedResponse = json.loads(response.text)

            address = decodedResponse['ip']
            country = decodedResponse['country']
            events = row['count']

            #convert country code to country name
            country_name = (pycountry.countries.get(alpha_2=country)).name
        else:
            address= row['IP']
            country_name = "Internal"     
            events = row['count']

        with open('ipinfo_output.csv','a', newline='') as info:
            writer = csv.writer(info)
            writer.writerow([address,country_name,events])
