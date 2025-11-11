import os
from google import genai
from dotenv import load_dotenv

load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

if not GOOGLE_API_KEY:
    raise ValueError("GOOGLE_API_KEY not found in environment variables.")

client = genai.Client(api_key=GOOGLE_API_KEY)

def generate_proposal(tender):
    try:
        prompt = f"""
       You are a professional proposal writer. Based on the following tender details, write a complete proposal.

    Tender Title: {tender.title}
    Description: {tender.description}
    Requirements: {tender.requirements}
    Budget: {tender.budget}
    Deadline: {tender.deadline}
        
    The proposal should use the following details dynamically:

        1. Executive Summary  
        2. Understanding of the Tender  
        3. Proposed Solution / Approach  
        4. Timeline and Deliverables  
        5. Budget Justification  
        6. Conclusion

        Company Name: XYZ Solutions
        Representative Name: XYZ
        Title: Project Manager
        City: Jaipur
        Email: contact@XYZ.in
        Phone: +91-1234567890

        Make it formal, professional, and easy to read.

        If any placeholder-like text exists in the tender description, replace it with the provided company and city details.
        Provide the final proposal in plain text format without any markdown or special formatting.
        Write details like address , email, phone number only if provided otherwise skip those details. 
        mark date of proposal submission as current date.
        """

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )
        return response.text.strip()

    except Exception as e:
        print(f"Gemini API error: {e}")
        return "Error generating proposal."
