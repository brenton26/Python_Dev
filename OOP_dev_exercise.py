'''

'''
from datetime import datetime, timedelta
import sqlite3


def initial_prompt():
    flag = False
    while (not flag):
        print("Options:")
        print("1) Register New Domain")
        print("2) Renew Domain")
        print("3) Delete Domain")
        print("4) Domain Info")
        print("5) Quit")
        user_selection = input("Selection: ")
        if user_selection == "1":
            domain_prompt()
        if user_selection == "2":
            pass
        if user_selection == "3":
            pass
        if user_selection == "4":
            pass             
        if user_selection == "5":
            flag = True



def domain_prompt():
    ans = input("Do you want to register a domain? (y/N): ").lower()
    if ans == 'y' or ans =='yes':
        print("Please provide the name of your domain, the number of days you")
        print("will be registering the domain for, and a required provider ID.")
        name = input("Domain name: ")
        period = input("Number of days domain is being registered for: ")
        provider_id = input("Provider ID: ")
        register_domain(name, period, provider_id)
        print("Domain successfully registered!")
    else:
        print("See you next time.")
    


# Keys represent hypothetical unique provider IDs that a customer must provide in order to register
VERIFIED_CONTACTS = {
    '265419': 'Provider-1',
    '606052': 'Provider-2',
    '050491': 'Provider-3',
    '811056': 'Provider-4',
    '409857': 'Provider-5',
    '462662': 'Provider-6',
    '903100': 'Provider-7',
    '882746': 'Provider-8',
    '195741': 'Provider-9',
    '736162': 'Provider-10'
}


def register_domain(domain_name, period_of_registration, contact_id):
    if contact_id in VERIFIED_CONTACTS:
        if len(domain_name)>=10:
            expiration_date = datetime.today() + timedelta(days=period_of_registration)
            provider = VERIFIED_CONTACTS[contact_id]

            conn = sqlite3.connect('domains.db')
            with conn:
                cur = conn.cursor()
                cur.execute("CREATE TABLE IF NOT EXISTS tbl_domains( \
                    ID INTEGER PRIMARY KEY AUTOINCREMENT, \
                    domain_name TEXT, \
                    expiration_date, DATETIME, \
                    provider TEXT \
                    )")
                cur.execute("INSERT INTO tbl_domains \
                    (domain_name, expiration_date, provider)  \
                    VALUES (?), ", domain_name, expiration_date, provider)
                conn.commit()
            conn.close()

                
        else:
            print("Domain name is required to be at least 10 characters")

    else: 
        print("Sorry, you are required to have a verified contact to register.")







class Domain:
    def __init__(self, name, expiration_date):
        self.name = name
        self.expiration_date = expiration_date
        self.expired = 

    def renew(self, domain_name, period_of_registration):
        pass

    def delete(self, domain_name):
        pass

    def info(self, domain_name):
        pass

if __name__ == "__main__":
    initial_prompt()
