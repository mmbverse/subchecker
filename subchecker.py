#!/usr/bin/env python3

import requests, argparse, urllib3, threading
urllib3.disable_warnings()

parser = argparse.ArgumentParser(description="Subdomain or URL Checker Tool")
parser.add_argument("-u", "--url", type=str, metavar="",  help="enter URL")
parser.add_argument("-l", "--list", type=str, metavar="", help="enter the path to file of list of URLs")
args = parser.parse_args()

def req(url):
    if "http://" in url or "https://" in url:
        u = url
        try:
            res = requests.get(u, allow_redirects=False, timeout=3)
            print(str(res.url))
        except: pass    
    else:
        u = "https://" + url
        try:
            res = requests.get(u, allow_redirects=False, timeout=3)
            print(str(res.url))
        except: 
            try:
                u = u.replace("https://", "http://")
                res = requests.get(u, allow_redirects=False, timeout=3)
                print(str(res.url))
            except: pass
    
if args.url: req(args.url)

if args.list:
    list = args.list
    file = open(list, "r")
    
    urls = file.readlines()
    file.close()
    
    for url in urls:
        url = url.strip()
        t = threading.Thread(target=req, args=(url,))
        t.start()
