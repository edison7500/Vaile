#!/usr/bin/env python3
# coding: utf-8

#-:-:-:-:-:-:-:-:-:-:-:-:#
#    Vaile Framework     #
#-:-:-:-:-:-:-:-:-:-:-:-:#

#Author : @_tID
#This module requires Vaile Framework
#https://github.com/VainlyStrain/Vaile


import time
import os
import sys
from core.methods.tor import session
from time import sleep
from tld import get_fld
from core.Core.colors import *

sublist = []
flist = []
found = []
total = []

info = "This module tries to find subdomains and stores them in a file."
searchinfo = "Subdomain Gatherer"
properties = {}

def subdombrute(web):
    try:
        print(GR+' [*] Importing wordlist path to be bruteforced... "files/subdomains.lst"')
        with open('files/fuzz-db/subdomain_paths.lst','r') as lol:
            for path in lol:
                a = path.replace("\n","")
                sublist.append(a)

    except IOError:
        print(R+' [-] Wordlist not found!')

    global found
    if 'http://' in web:
        web = web.replace('http://','')
    elif 'https://' in web:
        web = web.replace('https://','')
    else:
        pass

    web = 'http://' + web

    tld0 = get_fld(web)

    if len(sublist) > 0:
        for m in sublist:
            furl = str(m) + '.' + str(tld0)
            flist.append(furl)

    if flist:
        time.sleep(0.5)
        print(R+'\n      B R U T E F O R C E R')
        print(R+'     =======================\n')
        print(GR+' [*] Bruteforcing for possible subdomains...')
        for url in flist:
            if 'http://' in url:
                url = url.replace('http://','')
            elif 'https://' in url:
                url = url.replace('https://','')

            try:
                ip = socket.gethostbyname(url)
                print('\n'+O+' [+] Subdomain Found :'+C+color.TR3+C+G+url+C+color.TR2+C+P+'\t\t['+str(ip)+']')
                found.append(url)
            except:
                sys.stdout.write(B+'\r [*] Checking : '+C+url)
                sys.stdout.flush()
    return found

def outer(web):
    requests = session()
    global final
    final = []
    wew = []
    time.sleep(0.4)
    print(R+'\n    A P I   R E T R I E V E R  ')
    print(R+'   ===========================')

    print(GR + color.BOLD + ' [!] Retriving subdomains...')
    time.sleep(0.4)
    print(""+ GR + color.BOLD + " [~] Result: "+ color.END)
    dom = 'http://' + web
    text = requests.get('http://api.hackertarget.com/hostsearch/?q=' + dom).text
    result = str(text)
    if 'error' not in result:
        print(color.END + result+C)
        mopo = result.splitlines()
        for mo in mopo:
            ro = mo.split(',')[0]
            final.append(str(ro))

def report(web, found, final):

    print(R+'\n   R E P O R T')
    print(R+'  =============\n')
    if ((len(found) > 0) or (len(final) > 0)):
        print(O+' [!] Subdomains found for'+C+color.TR3+C+G+web+C+color.TR2+C)
        print(C+'  |')
        for m in found:
            print(C+ '  +-- ' +GR+ m)
            total.append(m)
        for p in final:
            if p not in found:
                print(C+ '  +-- '+GR+p)
                total.append(p)

    else:
        print(R+' [-] No Subdomains found for ' + O+web+C)
    print('\n')
    return total

def subdom(web):

    global fileo

    if 'http' in web:
        web = web.replace('http://','')
        web = web.replace('https://','')
    webb = web
    if "@" in web:
        webb = web.split("@")[1]
    fileo = 'tmp/logs/'+webb+'-logs/'+str(webb)+'-subdomains.lst'
    p = open(fileo,'w+')
    p.close
    #print(R+'\n   =====================================')
    #print(R+'    S U B D O M A I N   G A T H E R E R')
    #print(R+'   =====================================\n')
    from core.methods.print import posintact
    posintact("subdomain gatherer")
    time.sleep(0.7)
    print(B+' [*] Initializing Step [1]...')
    subdombrute(web)
    print(C+'\n [+] Module [1] Bruteforce Completed!\n')
    print(B+' [*] Initializing Step [2]...')
    outer(web)
    print(C+' [+] Module [2] API Retriever Completed!\n')
    acc = report(web, found, final)
    print(C+' [*] Writing found subdomains to a file...')
    if acc:
        for pwn in acc:
            vul = str(pwn) + '\n'
            miv = open(fileo, 'a')
            miv.write(vul)
            miv.close()
    print(C+' [+] Done!')

def attack(web):
    subdom(web)
