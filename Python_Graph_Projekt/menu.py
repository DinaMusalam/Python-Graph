# -*- coding: utf-8 -*-
from py2neo import Graph, Node, Relationship
import requests
import xmltodict
from xml.dom import minidom
from urllib import urlopen
from py2neo.cypher import CypherWriter
import sys
import os, functions
from urllib import quote_plus as urlencode
import unicodedata

#objekt som hänvisar till DBif
graph = Graph(urlencode("http://localhost:7474/db/data/").encode('utf-8'))
 
#hämta informationen från open data sourse för riksdagen 
dom = minidom.parse(urlopen('http://data.riksdagen.se/personlista/?utformat=xml'))
person_lista = dom.getElementsByTagName('person')
 

class Meny:

	

	def start_meny(self): # Första menyn, inloggning, skapa person eller avsluta
		os.system('cls' if os.name=='nt' else 'clear')
		choice = -1
		max = 2
		while choice != 0:
			title = "VÄLKOMMEN TILL GRAPHPROJEKTET!"
			print title
			print "-"*len(title)
			print "1. Hitta alla partier i en Valkrets"
			print "2. Hitta alla ledamöter i en Parti"
			print "0. Avsluta"

			choice = functions.input_int(max, 'Gör ett val: ', False)

			if choice == 1: # Hitta alla partier i en Valkrets
				print("Skriv in följande uppgifter:")
				
				input_valkrets = ""
				while input_valkrets == "":
					input_valkrets = raw_input("Valkrets namn: ")
				
				
				if input_valkrets != "":

					utfkod = input_valkrets.decode('utf-8')
					output= unicodedata.normalize('NFKD', utfkod).encode('ASCII','ignore')
					print("Alla partier i Valkrets  "+input_valkrets+" !")
										
					parti = graph.cypher.execute("MATCH (valkrets:Valkrets{name:'"+output+"'})--(partier:Partier) RETURN partier")
					print parti
					
					
				else:
					print("OBS: Du måste skriva valkrets namn!.")
			
			if choice == 2: # Hitta alla ledamöter i en Parti
				print("Skriv in följande uppgifter:")
				
				input_parti = ""
				while input_parti == "":
					input_parti = raw_input("Parti namn: ")
				
				
				if input_parti!= "":

					utfkodp = urlencode(input_parti.encode('utf-8'))
					outputp= unicodedata.normalize('NFKD', utfkodp).encode('ASCII','ignore')
					print("Alla ledamöter i "+ input_parti+" Parti:")
					
					person = graph.cypher.execute("MATCH (partier:Partier{name:'"+outputp+"'})--(ledamoter:Ledamot) RETURN ledamoter")
					print person
					
					
				else:
					print("OBS: Du måste skriva Parti namn.")

				
			elif choice == 0: # AVSLUTA
				os.system('cls' if os.name=='nt' else 'clear')
















			if choice == 1: # SKRIV UT PERSONINFORMATION
				#self.me.print_person()
				personinformation = self.me.get_person_data()
				for (k,v) in personinformation.iteritems():
					functions.print2(k.title()+": "+v.encode('utf-8'), 'blue', False)


m = Meny()
m.start_meny()
