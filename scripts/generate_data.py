import json
import random
import datetime

# Sample data to use
salespeople = ['Jane Smith', 'Mark Johnson', 'Emily Davis', 'Luke Wilson', 'Sarah Brown', 'Tom Anderson']
locations = ['New York, NY', 'San Francisco, CA', 'Chicago, IL', 'Austin, TX', 'Seattle, WA', 'Boston, MA']
industries = ['Technology', 'Finance', 'Healthcare', 'Education', 'Manufacturing', 'Retail']
client_statuses = ['Existing Client', 'Potential Client', 'Lead']
company_names = ['Acme Corp', 'Global Tech', 'Innovatech', 'NextGen Labs', 'FutureVision', 'Skyline Ventures']
competitors = ['TechNova Inc.', 'Alpha Solutions', 'BetaCorp', 'Gamma Enterprises', 'Delta Systems', 'None']

def generate_clients(num_clients=10):
    clients = []
    for i in range(num_clients):
        client = {}
        client_name = random.choice(company_names) + f' {i}'
        client['name'] = client_name
        client['status'] = random.choice(client_statuses)
        client['salesperson'] = random.choice(salespeople)
        client['data'] = {
            'Current ARR': random.randint(100000, 2000000) if client['status'] == 'Existing Client' else 0,
            'Number of Employees': random.randint(50, 1000),
            'Location': random.choice(locations),
            'Industry': random.choice(industries),
            'Churn Risk': random.choice(['Low', 'Medium', 'High']),
            'Potential Upsell': random.choice(['Yes', 'No']),
            'Competitors Engaged': random.choice(competitors),
            'Customer Since': random.randint(2015, 2023) if client['status'] == 'Existing Client' else 'N/A',
            'Last Contact Date': str(datetime.date.today() - datetime.timedelta(days=random.randint(1, 30)))
        }
        client['transcript'] = generate_transcript(client['salesperson'], client['name'])
        client['sales_notes'] = generate_sales_notes(client['salesperson'], client['name'], client['data'])
        clients.append(client)
    return clients

def generate_transcript(salesperson, client_name):
    # Generate a meaningful sales call transcript exceeding 1000 words
    topics = [
        "Discussing current satisfaction with products/services",
        "Exploring potential upsell opportunities",
        "Addressing concerns about competitors",
        "Negotiating pricing and contracts",
        "Scheduling next steps and follow-up actions"
    ]
    
    transcript = f"**Sales Call Transcript with {client_name}**\n"
    words_count = 0
    while words_count < 1000:
        topic = random.choice(topics)
        conversation = generate_conversation(salesperson, client_name, topic)
        transcript += conversation + "\n\n"
        words_count = len(transcript.split())
    return transcript.strip()

def generate_conversation(salesperson, client_name, topic):
    # Conversation templates for each topic
    client_rep = "Client Representative"
    dialogues = []

    if topic == "Discussing current satisfaction with products/services":
        dialogues = [
            f"{salesperson}: Hi, thanks for meeting today. How are you finding our services so far?",
            f"{client_rep}: Overall, we're pleased, but there are areas we think could improve.",
            f"{salesperson}: I appreciate your feedback. Could you elaborate on those areas?",
            f"{client_rep}: Sure, we're looking for faster support response times.",
            f"{salesperson}: Understood. I'll discuss this with our support team to enhance our responsiveness."
        ]
    elif topic == "Exploring potential upsell opportunities":
        dialogues = [
            f"{salesperson}: I wanted to share some new features that might benefit your operations.",
            f"{client_rep}: That sounds interesting. What are they?",
            f"{salesperson}: We have a new analytics module that provides deeper insights into your data.",
            f"{client_rep}: We could definitely use better analytics. Can you provide more details?",
            f"{salesperson}: Absolutely, I'll send over detailed information after our call."
        ]
    elif topic == "Addressing concerns about competitors":
        dialogues = [
            f"{salesperson}: I've heard that you're exploring options with other providers. Is there anything we can address?",
            f"{client_rep}: We're evaluating our options to ensure we're getting the best value.",
            f"{salesperson}: I understand. Let me know if there are specific areas where we can improve.",
            f"{client_rep}: We're particularly interested in more flexible pricing.",
            f"{salesperson}: Let's discuss pricing options to better suit your needs."
        ]
    elif topic == "Negotiating pricing and contracts":
        dialogues = [
            f"{salesperson}: I wanted to revisit our pricing structure with you.",
            f"{client_rep}: Yes, we're looking to optimize our costs.",
            f"{salesperson}: We can offer a discount if you extend your contract term.",
            f"{client_rep}: That could work. What kind of discount are we talking about?",
            f"{salesperson}: Let me prepare a proposal with the details for you."
        ]
    elif topic == "Scheduling next steps and follow-up actions":
        dialogues = [
            f"{salesperson}: To wrap up, I'll send the proposal and set up a demo for the new features.",
            f"{client_rep}: Great, we're looking forward to seeing how they can help us.",
            f"{salesperson}: Excellent. Is next Wednesday suitable for the demo?",
            f"{client_rep}: Yes, that works for us.",
            f"{salesperson}: Perfect, I'll send a calendar invite shortly."
        ]

    # Combine dialogues into a conversation
    conversation = "\n".join(dialogues)
    return conversation

def generate_sales_notes(salesperson, client_name, data):
    notes = f"**Salesperson:** {salesperson}\n"
    notes += f"**Client:** {client_name}\n"
    notes += f"**Date:** {str(datetime.date.today())}\n"
    notes += "**Notes:**\n"
    
    # Generate meaningful notes based on client data
    if data['Potential Upsell'] == 'Yes':
        notes += "- Client is interested in potential upsell opportunities.\n"
    if data['Churn Risk'] == 'High':
        notes += "- High churn risk detected; need to improve client engagement.\n"
    if data['Competitors Engaged'] != 'None':
        notes += f"- Client is in discussions with competitor {data['Competitors Engaged']}.\n"
    if data['Current ARR'] > 0:
        notes += "- Discussed contract renewal and possible pricing adjustments.\n"
    else:
        notes += "- Potential client; focus on demonstrating value proposition.\n"

    notes += "**Action Items:**\n"
    notes += "- Send detailed proposal and feature information.\n"
    notes += "- Schedule follow-up meeting next week.\n"

    return notes

if __name__ == "__main__":
    clients = generate_clients(10)
    with open('business_dataset.json', 'w') as f:
        json.dump(clients, f, indent=4)

