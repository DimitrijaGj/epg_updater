#! /usr/bin python
import requests
import os
"""Za update na EPG lista za IPTV 
os modul moze ama i ne mora da se koriste
module requests se instalira so comandata pip3 install 
requests"""

url = "http://line.dighub.cc/xmltv.php?"
username = "username=64035b848807e"
password="password=659988378b"

""" user i pass staveni kako variabli za da 
mozat da se koristat niz kodo bez potreba od 
pisuvanje sekoj pat"""
site=url+username+"&"+password
#site gi püovrzuva site da se dobie URL
print(site)
#proverka dali e URL so pravilna forma
check=requests.get(site)
print(check)
#proverka na HTTP Code od sajto treba da e 200, znaci OK
#ako e nekoj drug proveri na https://de.wikipedia.org/wiki/HTTP-Statuscode
r=requests.get(site)
#se povikuva sodrzinata na sajto
with open("/Users/dimitrija_gjoshev/Documents/TestSQL/epg_update.xml", "w") as file:
    #tuka se koriste apsolutan path. Crontab ne znae pri executijata kaj da ga zapise fajlo ako ima relativan path
    #!!! so znaci deka [/Users/dimitrija_gjoshev/Documents/TestSQL/epg_update.xml] treba da bide zameneto so tvoj apsoluten
    #path moze da se najde so vnesuvanje na pwd u terminalo
    file.write(r.text)
    """
    so open ("[ime na fajl.format na file], "w"- e za 
    write sekoj pat fileto ke bide unisten i rekreiran so 
    druga sodrzina) se kreira file vo folderot kade e skriptata
    """
