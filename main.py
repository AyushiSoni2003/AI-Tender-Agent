# app.py
from db import get_tender_data
from ai_agent import generate_proposal

def main():
    tender_id = 1  # example tender
    tender = get_tender_data(tender_id)

    if tender:
        proposal = generate_proposal(tender)
        print("Generated Proposal : ", proposal)
    else:
        print("Tender not found!")

if __name__ == "__main__":
    main()
