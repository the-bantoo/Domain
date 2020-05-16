import requests
import socket
url_base = "https://api.sandbox.namecheap.com/xml.response?ApiUser=duncannkhata&ApiKey=c01bb036e0074f26ab3a6bb56f4b31ea&UserName=duncannkhata&ClientIp=41.223.116.249&"

get_url = url_base + "Command=namecheap.domains.dns.getHosts&SLD=duncan&TLD=com"

response = requests.get(get_url)        # To execute get request 
#print(response, "<br>")     # To print http response code  
print(response.text)            # To print formatted JSON response

# Name="erp" Type="A" Address="1.1.1.1" MXPref="10" TTL="60"

#New Host


"""
get domain records:
- duncan.com: {"type": A, "host": erp, "value":"1.1.1.1", "TTL":"1M"}

insert new domain records
- &HostName2=mynewcomp&RecordType2=A&Address2=12.56.67.78&TTL2=1000


join old record
- hosts = []
i = 1

post_url = base_url

for record in response:
    host = record.getxml("Name")
    addre = record.getxml("Address")
    TTL = record.getxml("TTL")
    host_type = record.getxml("Type")
    
    host_label = "&HostName" + str(i) + "=" + host +  # repeat for other columns...
    new record = host_label + host_name + host_address + TTL


    
    
"""

