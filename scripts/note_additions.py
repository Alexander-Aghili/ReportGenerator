import pandas as pd
import random

# Load your data
df = pd.read_csv('salesforce_accounts.csv')

# Lists of notes

reasons_lost = [
    "Pricing was not competitive compared to other vendors.",
    "Client decided to postpone the project due to budget constraints.",
    "Product did not meet the client's technical requirements.",
    "Lost to a competitor offering better terms.",
    "Lack of engagement from the client's decision-makers.",
    "Client chose to develop an in-house solution.",
    "Unable to reach agreement on contract terms.",
    "Client's priorities shifted to other projects.",
    "Negative feedback from a product trial.",
    "Insufficient ROI demonstrated during the proposal.",
    "Client's company underwent restructuring.",
    "Poor timing; client not ready to purchase.",
    "Limited resources on the client's side to implement.",
    "Client was dissatisfied with previous interactions.",
    "Internal changes in client's management team.",
    "Concerns over product scalability.",
    "Compliance issues with industry regulations.",
    "Client preferred a local vendor.",
    "The proposal did not align with the client's strategic goals.",
    "Lack of customization options in the offering.",
    "Client had existing contracts with competitors.",
    "Delays in response times during the sales process.",
    "Client required features not available in our product.",
    "Economic downturn affecting client's industry.",
    "Client experienced a merger/acquisition affecting decisions.",
    "Negative references from other clients.",
    "Product lacked integration capabilities needed.",
    "Client's procurement process was too complex.",
    "High total cost of ownership perceived by the client.",
    "Security concerns not adequately addressed."
]

issues_encountered = [
    "Difficulty scheduling meetings with key stakeholders.",
    "Delays in providing requested information to the client.",
    "Technical demonstrations failed to impress.",
    "Misalignment between sales team and client needs.",
    "Communication breakdowns leading to misunderstandings.",
    "Inadequate follow-up after initial contact.",
    "High turnover within the sales team causing inconsistency.",
    "Challenges in customizing the proposal.",
    "Limited support from internal technical experts.",
    "Competition provided faster responses.",
    "Miscommunication about product features.",
    "Client's questions were not adequately addressed.",
    "Overcomplicating the sales pitch.",
    "Underestimating the client's knowledge level.",
    "Failure to establish a strong relationship.",
    "Inaccurate assessment of client's needs.",
    "Language barriers causing misinterpretations.",
    "Scheduling conflicts delaying the process.",
    "Lack of localized content or support.",
    "Ineffective negotiation strategies.",
    "Ignoring client's feedback during discussions.",
    "Inadequate discovery phase.",
    "Overpromising and underdelivering in initial stages.",
    "Not involving necessary team members early on.",
    "Failure to differentiate from competitors.",
    "Insufficient market research prior to engagement.",
    "Poor presentation materials.",
    "Discrepancies in pricing details.",
    "Unclear communication about timelines.",
    "Lack of urgency conveyed to the client."
]

other_remarks = [
    "Potential for future opportunities if circumstances change.",
    "Recommended to stay in touch for upcoming projects.",
    "Client appreciated the professionalism despite not moving forward.",
    "Opportunity to revisit after the client's internal changes settle.",
    "Suggested adjustments for future proposals.",
    "Positive feedback received on certain aspects.",
    "Client interested in other products/services we offer.",
    "Establishing a long-term nurturing plan.",
    "Potential referral to other departments within the client’s company.",
    "Noted market trends affecting client decisions.",
    "Opportunity to collaborate on a smaller scale.",
    "Client open to pilot programs in the future.",
    "Importance of nhancing product features highlighted.",
    "Need to improve competitive positioning.",
    "Client expressed interest in future technological advancements.",
    "Importance of addressing client-specific compliance needs.",
    "Possibility to partner with client's preferred vendors.",
    "Need for better alignment with client's strategic vision.",
    "Feedback to be used for internal training purposes.",
    "Recognized areas for process improvement.",
    "Potential impact of geopolitical factors.",
    "Consider tailoring marketing efforts for the client's industry.",
    "Acknowledged strong relationships built during the process.",
    "Importance of demonstrating clear ROI.",
    "Noted client’s satisfaction with competitors' offerings.",
    "Highlighted the need for more flexible solutions.",
    "Emphasized enhancing customer support responsiveness.",
    "Identified as a key account for future targeting.",
    "Need to improve demonstration of product scalability.",
    "Recognized the value of better personalization in sales approach."
]

def assign_notes(row):
    notes = ''
    
    if row['opportunity_stage'] == 'Closed Lost':
        # Customize reasons based on industry
        if row['industry'] == 'Technology':
            reason_options = [
                "Product did not meet the client's technical requirements.",
                "Client required features not available in our product.",
                "Concerns over product scalability."
            ]
        elif row['industry'] == 'Healthcare':
            reason_options = [
                "Compliance issues with industry regulations.",
                "Product lacked necessary certifications.",
                "Security concerns not adequately addressed."
            ]
        else:
            reason_options = reasons_lost  # Use the full list
        
        # Randomly select 1 to 2 reasons
        num_reasons = random.randint(1, min(2, len(reason_options)))
        reasons = random.sample(reason_options, num_reasons)
        reason_text = '; '.join(reasons)
        notes += f"Reason for loss: {reason_text}\n"
        
        # Customize issues based on account type
        if row['account_type'] == 'Partner':
            issue_options = [
                "Challenges in customizing the proposal.",
                "Limited support from internal technical experts.",
                "Difficulty aligning our services with partner expectations."
            ]
        else:
            issue_options = issues_encountered  # Use the full list
        
        # Randomly select 1 to 2 issues
        num_issues = random.randint(1, min(2, len(issue_options)))
        issues = random.sample(issue_options, num_issues)
        issue_text = '; '.join(issues)
        notes += f"Issues encountered: {issue_text}\n"
        
        # Randomly select 1 to 3 other remarks
        num_remarks = random.randint(1, min(3, len(other_remarks)))
        remarks = random.sample(other_remarks, num_remarks)
        remark_text = '; '.join(remarks)
        notes += f"Other remarks: {remark_text}"
    else:
        # For other stages
        # Randomly select 1 to 3 remarks
        num_remarks = random.randint(1, min(3, len(other_remarks)))
        remarks = random.sample(other_remarks, num_remarks)
        remark_text = '; '.join(remarks)
        notes += f"Remarks: {remark_text}"
    
    return notes
# Apply the function
df['notes'] = df.apply(assign_notes, axis=1)

# Save the updated DataFrame
df.to_csv('salesforce_accounts_notes.csv', index=False)

