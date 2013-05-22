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



##def name(string):
##    '''finds the name of the course from the string'''
##    n = string.find("</a>")
##    return string[:n]
##
##names = [name(x) for x in courselist] #for texting


#response = urllib.request.urlopen(jupiter)
#html = response.read()
#html=str(html)
#Email stuff
def login():
    smtpserv="smtp.gmail.com:587"
    mailserver=smtplib.SMTP(smtpserv)
    mailserver.starttls()
    mailserver.login(user,password)

def message(tolist, message):
    user="mising.grade.tracker@gmail.com"
    password="tommywiseau"
    smtpserv="smtp.gmail.com:587"
    mailserver=smtplib.SMTP(smtpserv)
    mailserver.starttls()
    mailserver.login(user,password)
    mailserver.sendmail(user,tolist,message)

#login()
#message('misingnoglic@gmail.com','The script has started hopefully')

###


##def gradefinder(stringbefore, html):
##    '''Finds the grade for one class'''
##    if (stringbefore in html)==False: return None #If a teacher hid a grade, this makes the program not crash
##    gradeplace = html.find(stringbefore) + len(stringbefore) #finds location of string
##    grade = (html[gradeplace:gradeplace+10]) #cuts the string to what is needed
##    end = grade.find('%')
##    return float((html[gradeplace:gradeplace+end])) #gets exactly the number
##
##def stringfinder(course):
##    '''Finds the string to put into the Variables'''
##    gradenum = html.find(course)
##    bigarea = html[gradenum:gradenum+300]
##    end = bigarea.find('&nbsp')
##    newstring = bigarea[:end]
##    reverse = newstring[::-1]
##    num = reverse.find(">")
##    return newstring[:end-num]
##    Old function that used to work
##    gradenum = html.find(grade)
##    bigarea = html[gradenum-300:gradenum]
##    shit = bigarea.find(course)
##    return html[(gradenum-300)+shit:gradenum]

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
