from py2neo import Graph, Node, Relationship
import requests
import xmltodict
from xml.dom import minidom
from urllib import urlopen
 
graph = Graph("http://localhost:7474/db/data/")
 
#hämta informationen från open data sourse för riksdagen 
dom = minidom.parse(urlopen('http://data.riksdagen.se/personlista/?utformat=xml'))
person_lista = dom.getElementsByTagName('person')
 
# Gå igenom alla personer och skapa noder
for person in person_lista:
    # namn på personer 
    namnobj=person.getElementsByTagName("sorteringsnamn")
    # parti till personer 
    partiobj=person.getElementsByTagName("parti")
    # valkrets till personer 
    valkretsobj=person.getElementsByTagName("valkrets")
    # Skapa noden för en ledamot
    ledamot_name=namnobj[0].firstChild.nodeValue
     
    #ledamot = Node("Ledamot", name=ledamot_name)
    ledamot = graph.merge_one("Ledamot", "name", ledamot_name)
        
    print (ledamot_name)
    # Skapa noden för en valkrets
    valkrets_name=valkretsobj[0].firstChild.nodeValue
        
    #valkrets = Node("Valkrets", name=valkrets_name)
    valkrets = graph.merge_one("Valkrets", "name", valkrets_name)
    
    print (valkrets_name)
    # Skapa noden för en partier
    parti_name=partiobj[0].firstChild.nodeValue
    
    #parti = Node("Partier", name=parti_name)
    parti = graph.merge_one("Partier", "name", parti_name)
    
    print (parti_name)
    # Skapa reltionen mellan en ledamot och parti
    ledamot_parti_relationship = Relationship(ledamot, "MEMBER_OF", parti)
    # Spara relationen i grafdatabasen
    graph.create(ledamot_parti_relationship)
    # Skapa reltionen mellan en ledamot och valkrets
    ledamot_valkrets_relationship = Relationship(ledamot, "REPRESENTS", valkrets)
    # Spara relationen i grafdatabasen
    graph.create(ledamot_valkrets_relationship)
    # Skapa reltionen mellan en parti och valkrets
    parti_valkrets_relationship = Relationship(parti, "EXISTS IN", valkrets)
    # Spara relationen i grafdatabasen
    graph.create(parti_valkrets_relationship)
