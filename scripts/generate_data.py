import pandas as pd
import random
from faker import Faker
from datetime import datetime, timedelta
from openai import OpenAI

# Initialize Faker
fake = Faker()

client = OpenAI()

# Helper functions
def random_date(start, end):
    """Generate a random date between start and end."""
    return start + timedelta(days=random.randint(0, (end - start).days))

def generate_notes():
    """Generate sales notes using OpenAI API."""
    prompts = [
        "Write a positive note where the customer praises the affordability of the product.",
        "Write a note where the customer complains about the lack of certain key features.",
        "Write a neutral note about the customer asking for more customization options.",
        "Write a positive note where the customer expresses delight with the product's performance.",
        "Write a negative note where the customer mentions unresolved technical issues.",
        "Write a note where the customer thanks the team for excellent customer service.",
        "Write a note about a customer being frustrated by long response times for support.",
        "Write a positive note where the customer recommends the product to others.",
        "Write a note where the customer requests more comprehensive training materials.",
        "Write a note about the customer giving mixed feedback on the overall value for money.",
        "Write a positive note about a customer being impressed by the sleek design.",
        "Write a note where the customer criticizes the lack of transparency in pricing.",
        "Write a note about the customer showing interest in expanding the current contract.",
        "Write a note where the customer expresses dissatisfaction with delivery delays.",
        "Write a note where the customer appreciates the recent updates to the software.",
        "Write a note about a customer being unhappy with frequent system downtimes.",
        "Write a note where the customer suggests a new feature for better analytics.",
        "Write a note about the customer praising the intuitive user interface.",
        "Write a note where the customer expresses frustration over hidden fees.",
        "Write a note where the customer highlights excellent post-sales support."
    ]
    prompt = random.choice(prompts)

    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {
                "role": "user",
                "content": prompt 
                }
            ]
        )

    res = completion.choices[0].message
    print(res)
    return res

# Generate example sales data
data = []
for i in range(100):  # Generate 100 entries
    customer_name = fake.company()
    headquarters = fake.city()
    monthly_revenue = round(random.uniform(10000, 500000), 2)  # Revenue in dollars
    start_date = random_date(datetime(2020, 1, 1), datetime(2023, 1, 1))
    end_date = start_date + timedelta(days=random.randint(30, 730))  # 1 month to 2 years
    sales_contact = fake.name()
    notes = generate_notes()
    data.append([
        customer_name,
        headquarters,
        monthly_revenue,
        start_date.strftime('%Y-%m-%d'),
        end_date.strftime('%Y-%m-%d'),
        sales_contact,
        notes
    ])
    print(data[i])

# Create DataFrame
columns = [
    "Customer Name", 
    "Customer Headquarters", 
    "Customer Monthly Revenue", 
    "Contract Start Date", 
    "Contract End Date", 
    "Sales Contact", 
    "Sales Notes"
]
df = pd.DataFrame(data, columns=columns)

# Save to CSV
df.to_csv("sales_data_with_varied_notes.csv", index=False)


