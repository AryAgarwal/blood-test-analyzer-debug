## Importing libraries and files
import os
from dotenv import load_dotenv
load_dotenv()

from crewai_tools import tools
from crewai_tools.tools.serper_dev_tool import SerperDevTool

## Creating search tool
search_tool = SerperDevTool()

from langchain.document_loaders import PyPDFLoader  # ✅ PDF reader from LangChain

# ✅ Custom PDF reader tool for extracting blood test data
class BloodTestReportTool:
    @staticmethod  # ✅ Make method statically callable
    def read_data_tool(file_path: str = 'data/sample.pdf') -> str:
        """
        Reads a blood test PDF and returns cleaned text.

        Args:
            file_path (str): Path to the PDF file.

        Returns:
            str: Extracted and cleaned full text from the report.
        """
        try:
            docs = PyPDFLoader(file_path=file_path).load()
            full_report = "\n".join(
                doc.page_content.replace("\n\n", "\n").strip() for doc in docs
            )
            return full_report.strip()
        except Exception as e:
            return f"Error reading PDF at {file_path}: {str(e)}"

# ✅ Nutrition tool with basic marker detection
class NutritionTool:
    @staticmethod
    def analyze_nutrition_tool(blood_report_data: str) -> str:
        """
        Analyzes nutrition-related markers in the blood report.

        Args:
            blood_report_data (str): Extracted text from the blood test.

        Returns:
            str: Nutrition suggestions based on detected deficiencies.
        """
        recommendations = []

        if "Vitamin D" in blood_report_data and "low" in blood_report_data.lower():
            recommendations.append("- Your Vitamin D is low. Consider more sunlight and Vitamin D3 supplements.")

        if "Iron" in blood_report_data and "low" in blood_report_data.lower():
            recommendations.append("- Low iron detected. Increase intake of iron-rich foods like spinach, lentils, and red meat.")

        if "B12" in blood_report_data and "low" in blood_report_data.lower():
            recommendations.append("- Vitamin B12 deficiency noted. Add eggs, fish, dairy, or B12 supplements.")

        if not recommendations:
            return "No significant nutrition deficiencies detected. Maintain a balanced diet with fruits, vegetables, and protein."

        return "\n".join(recommendations)

# ✅ Exercise planning tool with logic based on common markers
class ExerciseTool:
    @staticmethod
    def create_exercise_plan_tool(blood_report_data: str) -> str:
        """
        Recommends an exercise plan based on health status in blood markers.

        Args:
            blood_report_data (str): Text extracted from the blood report.

        Returns:
            str: Suggested exercise plan.
        """
        plan = []

        if "Cholesterol" in blood_report_data and "high" in blood_report_data.lower():
            plan.append("- High cholesterol: Focus on 30 minutes of daily cardio (e.g. brisk walking, cycling, swimming).")

        if "Glucose" in blood_report_data and "high" in blood_report_data.lower():
            plan.append("- Elevated glucose: Try moderate-intensity exercise 5 days a week, such as jogging or yoga.")

        if "Hemoglobin" in blood_report_data and "low" in blood_report_data.lower():
            plan.append("- Low hemoglobin: Start with low-impact activity like walking or light stretching until levels normalize.")

        if not plan:
            return "All markers seem normal. Recommend a balanced routine of cardio + strength training 3–5 times per week."

        return "\n".join(plan)
