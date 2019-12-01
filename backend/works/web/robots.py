import re
import sys
import json
import requests

def err(msg):
    print("![web/robots] {}".format(msg))
    sys.exit(1)

def parse_args():
    if len(sys.argv) != 2:
        err("Parameters needed!")
    return json.loads(sys.argv[1])

def get(url):
    headers = { 'User-Agent': 'Alfred' }
    r = requests.get(url, headers=headers)
    return r

def format_domain(url):
    re_domain = r'https?:\/\/([-a-z0-9._]{0,256}\.)?[-a-zA-Z0-9_]{1,256}\.[a-zA-Z]{1,6}\/?'
    if not re.match(re_domain,url):
        err("The domain has not a valid format")
    return "{}/robots.txt".format(url)

if __name__ == '__main__':
    args = parse_args()
    domain = args['domain']
    url = format_domain(domain)
    response = get(url)

    if response.status_code != 200:
        err("The domain has not exists")
    
    print("+[web/robots] Result:\n{}".format(response.text))
