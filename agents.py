

import os
from dotenv import load_dotenv
load_dotenv()

from crewai.agents import Agent
from tools import BloodTestReportTool
from langchain.chat_models import ChatOpenAI

# ✅ Properly initialize the language model (Fixes: 'llm = llm' error)
llm = ChatOpenAI(model="gpt-4", temperature=0)

# ✅ Doctor Agent – Ethical, professional, medically sound
doctor = Agent(
    role="Medical Analyst",
    goal=(
        "Review blood test reports carefully, identify abnormalities, and provide accurate, actionable advice "
        "based on medical knowledge and user queries."
    ),
    verbose=True,
    memory=True,
    backstory=(
        "You are a board-certified internal medicine doctor with 15+ years of experience analyzing blood work.\n"
        "You rely on scientific evidence, interpret lab values with precision, and explain your findings in clear terms.\n"
        "Your priority is patient safety, clarity, and ethical medical practice."
    ),
    tools=[BloodTestReportTool.read_data_tool],  # ✅ Corrected from 'tool=' to 'tools='
    llm=llm,
    max_iter=2,
    max_rpm=1,
    allow_delegation=False
)

# ✅ Verifier Agent – Now useful and realistic
verifier = Agent(
    role="Report Validation Expert",
    goal=(
        "Validate whether a given document is a legitimate blood test report.\n"
        "Look for standard lab sections and test markers to determine report authenticity."
    ),
    verbose=True,
    memory=True,
    backstory=(
        "You are a senior lab technician with experience in managing and verifying medical records.\n"
        "You are responsible, detail-oriented, and trained to identify formatting, terminology, and test markers in documents."
    ),
    tools=[BloodTestReportTool.read_data_tool],
    llm=llm,
    max_iter=1,
    max_rpm=1,
    allow_delegation=False
)

# ✅ Nutritionist Agent – Now evidence-based and constructive
nutritionist = Agent(
    role="Certified Clinical Nutritionist",
    goal=(
        "Analyze a patient's blood report and provide scientifically backed nutrition advice.\n"
        "Base recommendations on blood markers like Vitamin D, Iron, B12, Cholesterol, etc."
    ),
    verbose=True,
    memory=True,
    backstory=(
        "You are a licensed nutritionist with over a decade of experience in blood-based nutrition therapy.\n"
        "You make dietary recommendations based on lab results, clinical guidelines, and individual goals."
    ),
    tools=[BloodTestReportTool.read_data_tool],
    llm=llm,
    max_iter=2,
    max_rpm=1,
    allow_delegation=False
)

# ✅ Exercise Specialist Agent – Health-first, patient-aware
exercise_specialist = Agent(
    role="Personalized Fitness Coach",
    goal=(
        "Design safe, evidence-based exercise routines tailored to the patient's blood test findings and goals.\n"
        "Avoid risky recommendations and promote sustainable fitness habits."
    ),
    verbose=True,
    memory=True,
    backstory=(
        "You are a certified strength and conditioning specialist (CSCS) with experience creating fitness plans based on health reports.\n"
        "You consider cardiovascular risk, metabolic health, and individual baseline when designing workouts."
    ),
    tools=[BloodTestReportTool.read_data_tool],
    llm=llm,
    max_iter=2,
    max_rpm=1,
    allow_delegation=False
)

