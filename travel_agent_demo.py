import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def make_travel_plan(origin: str, destination: str, days: int, budget_usd: int) -> str:
    prompt = f"""
You are a travel planning assistant.

Create a realistic {days}-day trip plan.
Origin: {origin}
Destination: {destination}
Budget: ${budget_usd}

Rules:
- Keep it realistic for the budget.
- Give a simple day-by-day itinerary (Day 1, Day 2, etc.).
- Include 1 short note about transport.
- Do not mention that you are an AI.
"""

    response = client.responses.create(
        model="gpt-4.1-mini",
        input=prompt
    )
    return response.output_text.strip()

if __name__ == "__main__":
    origin = input("Where are you travelling from? ")
    destination = input("Where are you travelling to? ")
    days = int(input("How many days? "))
    budget_usd = int(input("Budget in USD? "))

    plan = make_travel_plan(origin, destination, days, budget_usd)

    print("\n=== Travel Plan ===\n")
    print(plan)
