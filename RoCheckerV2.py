import string, random, time, requests

print("Welcome to the new and improved RoChecker V2!\nHere are our updates:\n1. Ban filter (Find Available BUT banned names)\n2. Name size is configurable!\nIf you enjoy this script, or have any issues, contact the owner on Discord! (Azure#0263)\nCredit to 'Change Name' for the ban filter idea!\n\nTo begin, enter the amount of letters you want your name to be! (Maximum)!")

MaxAmount = int(input("Maximum Amount of Characters ??? - 20: "))

chars = string.ascii_letters + string.digits

def search():
  while True:
    time.sleep(0.1)
    name = ''.join(random.choice(chars) for i in range(0, MaxAmount))
    r = requests.get(f'http://api.roblox.com/users/get-by-username?username={name}')
    if r.text == '{"success":false,"errorMessage":"User not found"}':
      print(name + ' Valid')
    else:
      print(name + ' Invalid')
search()