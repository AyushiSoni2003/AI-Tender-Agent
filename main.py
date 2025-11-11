from db import get_all_tenders
from ai_agent import generate_proposal

def main():
    tenders = get_all_tenders()  # get all tenders from DB

    for tender in tenders:
        proposal = generate_proposal(tender)
        # save each proposal to a file
        with open(f"proposals/proposal_{tender.title}.txt", "w") as f:
            f.write(proposal)
        print(f"Proposal for {tender.title} saved!")

if __name__ == "__main__":
    main()
