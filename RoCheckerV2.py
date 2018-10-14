import string, random, time
from requests_html import HTMLSession

print("Welcome to the new and improved RoChecker V2!\nHere are our updates:\n1. Ban filter (Find Available BUT banned names)\n2. Name size is configurable!\nIf you enjoy this script, or have any issues, contact the owner on Discord! (Azure#0263)\nCredit to 'Change Name' for the ban filter idea!\n\nTo begin, enter the amount of letters you want your name to be! (Minimum and Maximum)!")

MaxAmount = int(input("Maximum Amount of Characters ??? - 20: "))

chars = string.ascii_letters + string.digits
session = HTMLSession()

while True:
    name = ''.join(random.choice(chars) for i in range(0, MaxAmount))
    r = session.get(f'https://www.roblox.com/UserCheck/doesusernameexist?username={name}')
    if r.html.search('True'):
        print(name, "[TAKEN]")
    else:
        r2 = session.get(f'https://www.roblox.com/User.aspx?Username={name}', allow_redirects=True)
        if r2.html.search("404"):
          print(name, "[BANNED]")
        else:
          print(f"{name} [AVAILABLE]!")
          f = open('names.txt', 'a+')
          f.write(name + "[AVAILABLE]\n")
          f.close()
        time.sleep(0.1)
