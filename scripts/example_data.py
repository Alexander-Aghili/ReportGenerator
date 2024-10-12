import random
from faker import Faker
import pandas as pd

# Initialize Faker for generating random data
fake = Faker()

# Lists to add variety in data
account_types = ['Partner', 'Customer', 'Reseller', 'Distributor', 'Consultant']
industries = ['Technology', 'Finance', 'Healthcare', 'Retail', 'Education', 'Manufacturing']
opportunity_stages = ['Prospecting', 'Qualification', 'Proposal', 'Negotiation', 'Closed Won', 'Closed Lost']

# Helper function to generate random phone numbers
def generate_phone_number():
    return f"(555) {random.randint(1000000, 9999999)}"

# Create 50 additional fictional entries with variety
new_entries = []
for _ in range(10000):
    entry = {
        'account_id': fake.uuid4(),
        'account_name': fake.company(),
        'account_type': random.choice(account_types),
        'industry': random.choice(industries),
        'annual_revenue': round(random.uniform(100000, 10000000), 2),
        'number_of_employees': random.randint(10, 5000),
        'website': fake.url(),
        'phone': generate_phone_number(),
        'fax': generate_phone_number(),
        'billing_street': fake.street_address(),
        'billing_city': fake.city(),
        'billing_state': fake.state(),
        'billing_postal_code': fake.postcode(),
        'billing_country': fake.country(),
        'contact_id': fake.uuid4(),
        'contact_first_name': fake.first_name(),
        'contact_last_name': fake.last_name(),
        'contact_email': fake.email(),
        'contact_phone': generate_phone_number(),
        'opportunity_id': fake.uuid4(),
        'opportunity_name': f"Opportunity {random.randint(1, 100)}",
        'opportunity_stage': random.choice(opportunity_stages),
        'opportunity_amount': round(random.uniform(5000, 500000), 2),
        'opportunity_close_date': fake.date_between(start_date='today', end_date='+90d').strftime('%Y-%m-%d')
    }
    new_entries.append(entry)

# Convert the new entries to a DataFrame
new_entries_df = pd.DataFrame(new_entries)

# Save the augmented data to a new CSV file
output_file_path = './augmented_salesforce_accounts.csv'
new_entries_df.to_csv(output_file_path, index=False)
