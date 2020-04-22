from datetime import datetime, timedelta
import sqlite3


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


class Domain:
    def __init__(self, name, expiration_date):
        self.name = name
        self.expiration_date = expiration_date
         
    @staticmethod
    def register(domain_name, period_of_registration, contact_id):
        if contact_id in VERIFIED_CONTACTS:
            if len(domain_name)>=10:
                expiration_date = datetime.strftime(datetime.today() + timedelta(days=period_of_registration), '%Y%m%d')
                provider = VERIFIED_CONTACTS[contact_id]
                conn = sqlite3.connect('domains.db')
                with conn:
                    cur = conn.cursor()
                    cur.execute("CREATE TABLE IF NOT EXISTS tbl_domains( \
                        domain_name TEXT PRIMARY KEY, \
                        expiration_date TEXT, \
                        provider TEXT \
                        )")
                    sql = "INSERT INTO tbl_domains \
                        (domain_name, expiration_date, provider)  \
                        VALUES (?,?,?)"
                    params = (domain_name, expiration_date, provider)
                    cur.execute(sql, params)
                    conn.commit()
                conn.close()
                domain_name = Domain(name=domain_name, expiration_date=expiration_date)
                print("\n* * * * * * * * * * * * * * * *\nDomain successfully registered!\n* * * * * * * * * * * * * * * *")
            else:
                print("\n\nDomain name is required to be at least 10 characters\n")
        else: 
            print("\nnSorry, you are required to have a *verified* provider ID to register.\n")

    #Checks if registration is expired or not
    def is_expired(self):
        return int(datetime.now().strftime('%Y%m%d')) >= int(self.expiration_date)

    #Renews registration
    @staticmethod
    def renew(domain_name, days_extended):        
        conn = sqlite3.connect('domains.db')
        with conn:
            cur = conn.cursor()
            try:
                sql = "SELECT expiration_date FROM tbl_domains WHERE domain_name=?"
                cur.execute(sql, (domain_name,))
                current_exp_date = cur.fetchone()[0]
                new_exp_date = datetime.strftime(datetime.strptime(current_exp_date, '%Y%m%d') + timedelta(days=days_extended), '%Y%m%d')
                sql = "UPDATE tbl_domains \
                    SET expiration_date = ? \
                    WHERE domain_name = ?"
                params = (new_exp_date, domain_name)
                cur.execute(sql, params)                
                conn.commit()
            except:
                print("Domain does not yet exist, you can register it")       
        conn.close()

    @staticmethod
    def delete(domain_name):
        conn = sqlite3.connect('domains.db')
        with conn:
            cur = conn.cursor()
            cur.execute("DELETE FROM tbl_domains WHERE domain_name=?", domain_name)
            print("Successfully deleted")

    @staticmethod
    def see_domains():
        print()
        conn = sqlite3.connect('domains.db')
        with conn:
            cur = conn.cursor()
            cur.execute("SELECT * FROM tbl_domains")
            table = cur.fetchall()
            counter = 1
            for row in table:
                print(counter)
                print(f"Domain: {row[0]}")
                print(f"Provider: {row[2]}")
                print(f"Expires: {datetime.strftime(datetime.strptime(row[1], '%Y%m%d'), '%D')}")
                counter+=1
        conn.close()
        input()

#Home Page
def initial_prompt():
    quit_program = False
    while not quit_program:
        print("\nOptions:")
        print("1) Register New Domain")
        print("2) Renew Domain")
        print("3) Delete Domain")
        print("4) Domain Info")
        print("5) Quit")
        user_selection = input("Selection: ")
        if user_selection == "1":
            domain_prompt()
        if user_selection == "2":
            renew_prompt()
        if user_selection == "3":
            delete_prompt()
        if user_selection == "4":
            Domain.see_domains()             
        if user_selection == "5":
            print("Goodbye")
            quit_program = True

#Option 1
def domain_prompt():
    flag = False
    while not flag:
        ans = input("Are you sure you want to register a domain? (y/N): ").lower()
        if ans == 'y' or ans =='yes':
            flag = True
            print("\nPlease provide the name of your domain, the number of days you")
            print("will be registering the domain for, and a required provider ID.")
            name = input("Domain name: ")
            while True:
                period = input("Number of days domain is being registered for: ")
                try: 
                    period = int(period)
                    break
                except:
                    print("\nPlease enter a whole number\n")        
            provider_id = input("Provider ID: ")
            Domain.register(name, period, provider_id)
            
        if ans == 'n' or ans == "no":
            flag = True
            print("\n\n\nThen what DO you want to do?")

#Option 2
def renew_prompt():
    flag = False
    while not flag:
        ans = input("Are you sure you want to renew your domain? (y/N): ").lower()
        if ans == 'y' or ans =='yes':
            flag = True
            domain = input("What domain name are you renewing?: ")
            while True:
                days = input("How many days do you want to renew your domain name for?: ")
                try: 
                    days = int(days)
                    break
                except:
                    print("\nPlease enter a whole number\n")
            Domain.renew(domain, days)
        if ans == 'n' or ans =='no':
            flag = True 
            print("\n\n\nThen what DO you want to do?")   

def delete_prompt():
    flag = False
    while not flag:
        ans = input("Are you sure you want to delete your domain? (y/N): ").lower()
        if ans == 'y' or ans =='yes':
            flag = True
            domain_to_delete = input("What domain do you want to delete?: ")
            conn = sqlite3.connect('domains.db')
            with conn:
                cur = conn.cursor()
                cur.execute("SELECT COUNT(1) FROM tbl_domains WHERE domain_name=?", (domain_to_delete,))
                if cur.fetchone()[0] == 0:
                    print("\nThat domain name does not exist.")
                else:
                    cur.execute("DELETE FROM tbl_domains WHERE domain_name=?", (domain_to_delete,))
                    print("\nSuccessfully deleted")

        if ans == 'n' or ans =='no':
            flag = True 
            print("\n\n\nThen what DO you want to do?")            

if __name__ == "__main__":
    initial_prompt()
