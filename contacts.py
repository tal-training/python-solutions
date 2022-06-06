import shelve
from appJar import gui

db=shelve.open("contacts.db")
if "contacts" in db.keys():
    contacts=db["contacts"]
else:
    contacts=dict()
    db["contacts"]=contacts
    
userPasswords={"admin":"abc123"}

menu="""
Contacts App
------------
1. Add contact
2. Search contacts
3. Get contact
4. List Contacts
9. Exit
"""

def login():
    username, password=input("username? "), input("password? ")
    return username in userPasswords and userPasswords[username]==password

def add(contact):
    contacts.update(contact)
    
def search(name):
    for k in contacts.keys():
        if k.count(name)>=1:
            return f"{k}: {contacts.get(k)}"

def get(name):
    return contacts.get(name, "contact doesn't exist")
    # this is the slow way:
    if name in contacts.keys():
        return name, contacts[name]
    else:
        return "contact doesn't exist"


def list():
    for c in contacts:
        print(c, contacts[c])
        
def save(contacts):
    db["contacts"]=contacts

app=gui('My Contacts')
app.addLabelEntry("Name")
app.addLabelEntry("Phone Number")
app.addLabelEntry("Email Address")

#app.addMenuItem("file", "open", load)
#app.addMenuItem("file", "save", save)
#app.showSplash("TEXT EDIT ++", fill='red', stripe='black', fg='white', font=44)
app.go()


while(True):
    choice=input(menu+'\r')
    if choice=='1':
        if login():
            name=input("New Contact name? ")
            phone=input("New Contact phone number? ")
            email=input("New Contact email address? ")
            contact={name:{"phone":phone, "email":email}}
            add(contact)
            save(contacts)
        else:
            print("unauthorized")
    if choice=='2':
        q=input("Search: ")        
        print(search(q))
    if choice=='3':
        name=input("Existing Contact name? ")
        print(get(name))
    if choice=='4':
        list()
    if choice=='9':
        break
    
db.close()
    
    
    
    
    