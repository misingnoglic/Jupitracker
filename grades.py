#!/usr/local/bin/python3.3

from time import sleep,ctime
import urllib.request
import smtplib

user= #Put in Gmail email in quotes. This is the email that will send updates
password=#Put password to above email in quotes


def gradefinder(X, html):
    x=len(X)
    gradenum = html.find(X)
    after=(html[gradenum+x+130:gradenum+x+138])
    if ("%" in after)==False: return None
    x=after.find('%')
    return after[:x]


def login():
    smtpserv="smtp.gmail.com:587"
    mailserver=smtplib.SMTP(smtpserv)
    mailserver.starttls()
    mailserver.login(user,password)

def message(tolist, message):
    smtpserv="smtp.gmail.com:587"
    mailserver=smtplib.SMTP(smtpserv)
    mailserver.starttls()
    mailserver.login(user,password)
    mailserver.sendmail(user,tolist,message)

def gradechecker(jupiter, courselist, names, email, phonemail, tolist):
    '''Main Program, constantly checks grades'''
    #Boring HTML stuff, DLing jupiter source
    response = urllib.request.urlopen(jupiter)
    html = response.read()
    html=str(html)
    fgrades = [gradefinder(x, html) for x in courselist] #makes list of grades to compare
    grades = fgrades #not sure why that's there but it works
    print(ctime())
    print([x for x in zip(names, fgrades)]) #lets you know what initial grades are
    ty= ("Thank you for joining, your grades are being checked for changes.")
    msg = ('Subject: %s\n\n%s' % ("Thank you for signing up", ty))
    #message(tolist, msg)
    while True:
        sleep(600) #Every minute it checks. I can change this inverval

        ##Same boring HTML stuff##
        website = urllib.request.urlopen(jupiter)
        code = website.read()
        strcode=str(code)
        ###

        grades = [gradefinder(x, strcode) for x in courselist]
        if fgrades != grades:
            if grades!=[None for x in range(len(fgrades))]:
                for x in range(0,len(courselist)):
                    if fgrades[x]!=grades[x]:
                        login()
                        print(ctime())
                        grademessage =  'Your grade in ' + str(names[x]) + ' has changed from a ' + str(fgrades[x]) +'% to a '+str(grades[x])+'%'
                        print(grademessage)
                        msg = ('Subject: %s\n\n%s' % ("Your grade in " + str(names[x]) + " has changed!", grademessage))
                        message(tolist, msg)
                fgrades = grades
