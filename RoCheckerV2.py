import string, random, time, threading
from requests_html import HTMLSession

print("Welcome to the new and improved RoChecker V2!\nHere are our updates:\n1. Ban filter (Find Available BUT banned names)\n2. Name size is configurable!\nIf you enjoy this script, or have any issues, contact the owner on Discord! (Azure#0263)\nCredit to 'Change Name' for the ban filter idea!\n\nTo begin, enter the amount of letters you want your name to be! (Maximum)!")

MaxAmount = int(input("Maximum Amount of Characters ??? - 20: "))

chars = string.ascii_letters + string.digits
session = HTMLSession()


def search():
  while True:
    time.sleep(0.1)
    name = ''.join(random.choice(chars) for i in range(0, MaxAmount))
    r = session.get(f'https://www.roblox.com/UserCheck/doesusernameexist?username={name}')
    if r.html.search('true'):
      print(f"{name} [TAKEN]!")

    if r.html.search('false'):
      try:
        r2 = session.get(f'https://www.roblox.com/User.aspx?Username={name}', allow_redirects=True)
        
        if r2.html.search('404'):
          print(f"{name} [BANNED]")
        else:
          print(f"{name} [AVAILABLE]")
      except:
        break
search()
