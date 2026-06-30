from crewai import Agent, Task, Crew, LLM
from dotenv import load_dotenv
import os

# ==============================
# Load API Key
# ==============================
load_dotenv()
api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    raise ValueError(" GROQ_API_KEY not found in .env file")

# ==============================
# LLM
# ==============================
llm = LLM(
    model="groq/llama-3.3-70b-versatile",
    temperature=0,
    api_key=api_key
)

# ==============================
# Guardrail Function
# ==============================
def is_travel_query(user_input):
    keywords = [
        "trip", "travel", "itinerary", "route",
        "budget", "visit", "tour", "plan", "days"
    ]
    return any(word in user_input.lower() for word in keywords)

# ==============================
# Agents 
# ==============================
route_agent = Agent(
    role="Travel Route Finder",
    goal="Only provide travel routes",
    backstory="You ONLY answer travel-related queries. Reject others.",
    llm=llm
)

cost_agent = Agent(
    role="Travel Cost Estimator",
    goal="Only estimate travel cost",
    backstory="You ONLY answer travel-related queries. Reject others.",
    llm=llm
)

planner_agent = Agent(
    role="Travel Planner",
    goal="Only create travel itinerary",
    backstory="You ONLY answer travel-related queries. Reject others.",
    llm=llm
)

# ==============================
# MAIN FUNCTION
# ==============================
def run_travel_planner(user_input: str) -> str:
    try:
        # Guardrail 1: Input validation
        if not is_travel_query(user_input):
            return " I can only help with travel planning queries (trips, routes, itinerary, budget)."

        #  Guardrail 2: Strict instructions
        route_task = Task(
            description=f"""
            User Query: {user_input}

            Instruction:
            - Answer ONLY if it is a travel-related query
            - Provide transport routes (bus/train/flight)
            - Do NOT answer unrelated questions
            """,
            expected_output="Travel routes only",
            agent=route_agent
        )

        cost_task = Task(
            description=f"""
            User Query: {user_input}

            Instruction:
            - Provide cost estimation
            - Stay within travel context only
            """,
            expected_output="Cost breakdown only",
            agent=cost_agent
        )

        planner_task = Task(
            description=f"""
            User Query: {user_input}

            Instruction:
            - Create day-wise itinerary
            - STRICTLY travel planning only
            - No extra explanations
            """,
            expected_output="Structured itinerary",
            agent=planner_agent
        )

        crew = Crew(
            agents=[route_agent, cost_agent, planner_agent],
            tasks=[route_task, cost_task, planner_task],
            verbose=False
        )

        result = crew.kickoff()

        # Guardrail 3: Clean output
        return f"✈️ Travel Plan:\n\n{result}"

    except Exception as e:
        return f" Error: {str(e)}" 

        
