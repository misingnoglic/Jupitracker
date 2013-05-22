#!/usr/local/bin/python3.3


#This is the file you run, edit it with the correct info :)
from grades import *
jupiter = #Insert jupitergrades private link in quotes, starts with 'https://jupitergrades.com/login/private.php'
courselist= #list of courses you are taking, exactly as they are on jupitergrades, in this format:
            #['AP Govt./Econ H', 'Psych/CnslrnPrn', 'AP Physics', 'AP Calculus AB', 'Symph. Band', 'AP Lit/Comp7/8']
email = #Email grades will be notified with: e.g. 'misingnoglic@gmail.com'
phonemail = # Phone number ending in carrier email in quotes, list of carrier emails at http://en.wikipedia.org/wiki/List_of_SMS_gateways
#e.g. '3236666413@txt.att.net'

tolist = [email,phonemail] #delete one of these if user only wants emails or texts
names = courselist
gradechecker(jupiter, courselist, names, email, phonemail, tolist)
