from appJar import gui
import shelve

db=shelve.open("contacts2.db")
if "contacts" in db.keys():
    contacts=db["contacts"]
else:
    contacts=dict()
    db["contacts"]=contacts
    
userPasswords={"admin":"abc123"}

def login(username, password):
    return username in userPasswords and userPasswords[username]==password

def add():
    name, phone, email=main_form.getAllInputs().values()
    contact={name:{"phone":phone, "mail":email}}
    contacts.update(contact)
    save(contacts)
    
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

def show():
    for c in contacts:
        print(c, contacts[c])
        
def save(contacts):
    db["contacts"]=contacts

def switch(action):
    if action=="Add":
        user=main_form.stringBox("Login", "Enter Admin Username")
        password=main_form.stringBox("Login", "Enter Admin Password")
        if login(user, password):
            main_form.addLabel("Add")
            main_form.addLabelEntry("Name")
            main_form.addLabelEntry("Phone Number")
            main_form.addLabelEntry("Email Address")
            main_form.addButton("Add Contact", add)
        else:
            main_form.infoBox(title="Error", message="Unauthorized")


main_form=gui("My Contacts", "800x600")
main_form.addButtons(["Add", "Search", "Get"], switch)
main_form.go()
   
db.close()
    
    
    
    
    