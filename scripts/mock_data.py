from faker import Faker
import random
from datetime import datetime, timedelta

fake = Faker()

# Number of records to generate
NUM_SALES_REPS = 10
NUM_ACCOUNTS = 50
NUM_CONTACTS = 200
NUM_OPPORTUNITIES = 100

# Generate sales_reps data
sales_reps = []
for i in range(1, NUM_SALES_REPS + 1):
    rep = {
        'id': i,
        'first_name': fake.first_name(),
        'last_name': fake.last_name(),
        'email': fake.email(),
        'phone_number': fake.phone_number(),
        'region': random.choice(['North America', 'EMEA', 'APAC', 'Latin America']),
        'hire_date': fake.date_between(start_date='-5y', end_date='today'),
        'manager_id': None  # Optionally, set up a manager hierarchy
    }
    sales_reps.append(rep)

# Generate accounts data
accounts = []
for i in range(1, NUM_ACCOUNTS + 1):
    owner = random.choice(sales_reps)
    account = {
        'id': i,
        'account_name': fake.company(),
        'account_type': random.choice(['Prospect', 'Customer', 'Partner', 'Reseller']),
        'industry': random.choice(['Technology', 'Healthcare', 'Finance', 'Retail', 'Manufacturing']),
        'revenue': round(random.uniform(1e5, 1e7), 2),
        'employee_count': random.randint(10, 10000),
        'region': random.choice(['North America', 'EMEA', 'APAC', 'Latin America']),
        'billing_address': fake.address(),
        'account_owner': f"{owner['first_name']} {owner['last_name']}",
        'phone_number': fake.phone_number(),
        'website': fake.url()
    }
    accounts.append(account)

# Generate contacts data
contacts = []
for i in range(1, NUM_CONTACTS + 1):
    account = random.choice(accounts)
    owner = random.choice(sales_reps)
    contact = {
        'id': i,
        'first_name': fake.first_name(),
        'last_name': fake.last_name(),
        'title': random.choice(['CEO', 'CTO', 'CFO', 'Manager', 'Director', 'Engineer', 'Sales Rep']),
        'email': fake.email(),
        'phone_number': fake.phone_number(),
        'company_id': account['id'],
        'contact_owner': f"{owner['first_name']} {owner['last_name']}",
        'mailing_address': fake.address(),
        'created_date': fake.date_between(start_date='-5y', end_date='today'),
        'last_activity_date': fake.date_between(start_date='-1y', end_date='today'),
    }
    contacts.append(contact)

# Generate opportunities data
opportunity_stages = ['Prospecting', 'Qualification', 'Proposal', 'Negotiation', 'Closed Won', 'Closed Lost']
opportunities = []
for i in range(1, NUM_OPPORTUNITIES + 1):
    account = random.choice(accounts)
    owner = random.choice(sales_reps)
    stage = random.choice(opportunity_stages)
    is_closed = stage in ['Closed Won', 'Closed Lost']
    close_date = fake.date_between(start_date='-1y', end_date='today') if is_closed else None
    opportunity = {
        'id': i,
        'opportunity_name': f"{account['account_name']} - {fake.bs()}",
        'opportunity_stage': stage,
        'close_date': close_date,
        'amount': round(random.uniform(1e3, 1e6), 2),
        'probability': 100 if stage == 'Closed Won' else (0 if stage == 'Closed Lost' else random.randint(10, 90)),
        'opportunity_owner': f"{owner['first_name']} {owner['last_name']}",
        'account_id': account['id'],
        'created_date': fake.date_between(start_date='-2y', end_date='today'),
        'last_modified_date': fake.date_between(start_date='-1y', end_date='today'),
    }
    opportunities.append(opportunity)

# Output the data
print("Sales Reps:")
for rep in sales_reps[:5]:
    print(rep)

print("\nAccounts:")
for acc in accounts[:5]:
    print(acc)

print("\nContacts:")
for con in contacts[:5]:
    print(con)

print("\nOpportunities:")
for opp in opportunities[:5]:
    print(opp)

