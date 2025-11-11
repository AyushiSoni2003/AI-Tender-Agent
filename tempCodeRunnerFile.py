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
        You are an expert tender proposal writer.

        Based on the following tender details, write a detailed and persuasive **proposal**:

        Tender Title: {tender.title}
        Description: {tender.description}
        Requirements: {tender.requirements}
        Budget: {tender.budget}
        Deadline: {tender.deadline}

        Format the proposal with the following structure:

        1. Executive Summary  
        2. Understanding of the Tender  
        3. Proposed Solution / Approach  
        4. Timeline and Deliverables  
        5. Budget Justification  
        6. Conclusion

        Make it formal, professional, and easy to read.
        """

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )
        return response.text.strip()

    except Exception as e:
        print(f"Gemini API error: {e}")
        return "Error generating proposal."
