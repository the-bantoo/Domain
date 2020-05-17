import requests
import socket
user="duncannkhata"
api_key = "c01bb036e0074f26ab3a6bb56f4b31ea"
client_ip = "41.223.116.249"
domain = "&SLD=duncan&TLD=com"

base_url = "https://api.sandbox.namecheap.com/xml.response?ApiUser=" + user + "&ApiKey=" + api_key + "&UserName=" + user + "&ClientIp="+ client_ip

get_command = "&Command=namecheap.domains.dns.getHosts"
get_url = base_url + get_command + domain

get_response = requests.get(get_url)        # To execute get request 
#print(response, "<br>")     # To print http response code  
# print(get_response.text)            # To print formatted JSON response

# Name="erp" Type="A" Address="1.1.1.1" MXPref="10" TTL="60"

#New Host

post_command = "&Command=namecheap.domains.dns.setHosts"
# add old host records to new record here using for loop
records = "&HostName1=mynewcomp&RecordType1=A&Address1=12.56.67.78&TTL1=60"

post_url = base_url + post_command + domain + records

post_response = requests.post(post_url)
print(post_response.text)

print("*************************** \n",get_response.text) 


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

