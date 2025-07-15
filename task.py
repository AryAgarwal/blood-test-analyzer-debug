

from crewai import Task
from agents import doctor, nutritionist, exercise_specialist, verifier
from tools import BloodTestReportTool

# ✅ Task 1: Medical summary and user query resolution
help_patients = Task(
    description=(
        "Read the patient's blood test report and answer their query: {query}.\n"
        "Carefully analyze the lab markers and explain any abnormalities or noteworthy observations.\n"
        "Be informative, concise, and medically accurate in your explanation."
    ),
    expected_output=(
        "A summary of the patient's blood report in simple terms.\n"
        "Include any abnormal values, what they may indicate, and answer the user's question directly.\n"
        "Mention if follow-up with a real doctor is recommended."
    ),
    agent=doctor,
    tools=[BloodTestReportTool.read_data_tool],
    async_execution=False
)

# ✅ Task 2: Nutrition guidance based on blood markers
nutrition_analysis = Task(
    description=(
        "Using the blood report, analyze nutritional deficiencies or imbalances.\n"
        "Suggest diet improvements based on markers like Iron, B12, Vitamin D, Cholesterol, etc.\n"
        "Use only scientifically backed information and respond to the user query: {query}."
    ),
    expected_output=(
        "List key nutritional observations and provide practical dietary suggestions.\n"
        "Mention specific foods or nutrients if a deficiency is found.\n"
        "Avoid generic or unverified advice."
    ),
    agent=nutritionist,
    tools=[BloodTestReportTool.read_data_tool],
    async_execution=False
)

# ✅ Task 3: Personalized exercise plan (health-aware)
exercise_planning = Task(
    description=(
        "Read the blood test report and develop a safe, evidence-based fitness plan.\n"
        "Adjust intensity based on health indicators such as cholesterol, inflammation, glucose, etc.\n"
        "Answer the user's query: {query} and provide a sustainable plan."
    ),
    expected_output=(
        "A brief fitness routine tailored to the patient's profile.\n"
        "Explain why certain activities are recommended or avoided.\n"
        "Include notes on pacing, rest, and gradual progression."
    ),
    agent=exercise_specialist,
    tools=[BloodTestReportTool.read_data_tool],
    async_execution=False
)

# ✅ Task 4: Report verification (document structure + content check)
verification = Task(
    description=(
        "Determine if the uploaded file is a valid blood test report.\n"
        "Check for presence of standard lab markers, sections like CBC, Lipid Profile, etc.\n"
        "Answer: Is this a real medical document?"
    ),
    expected_output=(
        "Yes/No assessment of the document's authenticity as a blood report.\n"
        "Mention what key elements were found or missing.\n"
        "Give a short justification for the decision."
    ),
    agent=verifier,
    tools=[BloodTestReportTool.read_data_tool],
    async_execution=False
)
