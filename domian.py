import requests
import xml.etree.ElementTree as ET
import json

user="duncannkhata"
api_key = "c01bb036e0074f26ab3a6bb56f4b31ea"
client_ip = "165.56.181.198"

base_url = "https://api.sandbox.namecheap.com/xml.response?ApiUser=" + user + "&ApiKey=" + api_key + "&UserName=" + user + "&ClientIp="+ client_ip

def get_hosts(domain):
    sld = domain.split('.')[0]
    tld = domain.split('.')[1]

    domain = "&SLD={sld}&TLD={tld}".format(sld = sld, tld = tld)
    get_command = "&Command=namecheap.domains.dns.getHosts"
    get_url = base_url + get_command + domain
    get_response = requests.get(get_url)        # To execute get request 
    return get_response


"""
TODO
- Add error checking, input validation
- connection testing
- add namecheap vars to settings like (client_ip - use server ip), username
- verify successful get, post, stop if not successful
"""
def add_host(sub_domain, server_ip):
    sld = sub_domain.split('.')[1]
    tld = sub_domain.split('.')[2]

    domain = "&SLD={sld}&TLD={tld}".format(sld = sld, tld = tld)
    existing_hosts = get_hosts(sld+"."+tld)
    
    post_command = "&Command=namecheap.domains.dns.setHosts"
    # add old host records to new record here using for loop

    #print("*************************** \n", existing_hosts.text)

    #Read the existing domain record
    #my_dict = json.loads(xmltodict.parse(existing_hosts.text), indent=2)
    root = ET.fromstring(existing_hosts.text)
    hosts = ""
    all_hosts = ""
    i = 1
    for host in root[3][0]:
        #if('Domain' in str(child.attrib)): # test whether response has domains

        h = json.loads(json.dumps(host.attrib, indent=2))
        hosts = "&HostName{0}={name}&RecordType{0}={type}&Address{0}={addr}&TTL{0}={ttl}" \
                "".format(i, name = h['Name'], type = h['Type'], addr =  h['Address'], ttl =  h['TTL'])
        all_hosts = all_hosts + hosts
        i = i+1

    new_host = "&HostName{0}={name}&RecordType{0}={type}&Address{0}={addr}&TTL{0}={ttl}" \
                "".format(i, name = sub_domain.split('.')[0], type = "A", addr = server_ip, ttl = 700)
    all_hosts = all_hosts + new_host
    print(all_hosts)
    
    post_url = base_url + post_command + domain + all_hosts
    
    post_response = requests.post(post_url)
    #print(post_response.text)
    

add_host("fourth.duncan.com", "1.1.1.1")

print(get_hosts("duncan.com").text)