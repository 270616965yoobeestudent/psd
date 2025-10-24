import os
from textwrap import dedent

from google import genai


def instructor_chatbot():
    """Command-line chatbot that fetches itineraries from Gemini models."""
    print(
        "Welcome to AI Itinerary recommender! "
        "Answer a few questions to get personalized itinerary advice.\n"
    )

    days = input("How many (days): ")
    location = input("Where is the destination (city name): ")
    age = input("Enter your age: ")

    prompt = dedent(
        f"""
        You are a professional tourist itinerary recommender. Provide a detailed plan based on the user's answers.

        User Details:
        - Trip length: {days} days
        - Destination: {location} (city)
        - Age: {age} years old

        Instructions:
        - Begin with a brief overview that ties the details together.
        - Provide a day-by-day itinerary.
        - Each day should list up to three activities with the place name, address (or neighborhood if exact address is unknown), and a short description.
        - Tailor the tone to an enthusiastic expert named Hadi.
        """
    ).strip()

    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        print("Error: Set the GEMINI_API_KEY environment variable before running the chatbot.")
        return

    client = genai.Client(api_key=api_key)

    try:
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=prompt,
            config={
                "temperature": 0.7,
                "max_output_tokens": 400,
            },
        )

        print("\nMy name is Hadi, your AI itinerary expert:\n")
        print(response.text)

    except Exception as exc:
        print("Error communicating with Gemini API:", exc)


if __name__ == "__main__":
    instructor_chatbot()
