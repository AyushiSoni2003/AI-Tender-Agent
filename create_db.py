# create_db.py
from db import Base, engine, Session, Tender

# Create all tables (if not already created)
Base.metadata.create_all(engine)

# Create a new session
session = Session()

# Add one sample tender
sample_tenders = [
       {
        "title": "Construction of Smart City Control Room",
        "description": "Setup of a centralized monitoring and control system for Smart City operations.",
        "requirements": "Vendors must have prior experience in IoT integration and smart surveillance systems.",
        "budget": 12000000,
        "deadline": "2025-12-31",
    },
    {
        "title": "Procurement of Electric Buses",
        "description": "Supply and maintenance of 50 electric buses under the green mobility initiative.",
        "requirements": "Manufacturers with valid RTO certification and after-sales service centers in India.",
        "budget": 80000000,
        "deadline": "2025-11-30",
    },
    {
        "title": "Development of E-Governance Portal",
        "description": "Creation of a citizen service platform for online applications and grievance redressal.",
        "requirements": "Experience with secure web app development using modern frameworks like Django or Flask.",
        "budget": 4000000,
        "deadline": "2025-12-15",
    },
    {
        "title": "Construction of Solar-Powered Water Pumping Stations",
        "description": "Installation of solar panels and water pumps in 100 rural locations.",
        "requirements": "Bidders must be registered solar EPC contractors with 3+ years of field experience.",
        "budget": 6000000,
        "deadline": "2025-12-20",
    },
]

# insert tenders into the database
for tender_data in sample_tenders:
    tender = Tender(**tender_data)
    session.add(tender)

# Add to session and commit
session.add(tender)
session.commit()

print("Database initialized and sample tender added successfully!")
