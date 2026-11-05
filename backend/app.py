from flask import Flask, send_from_directory, request, jsonify
from pathlib import Path
from dataclasses import asdict

from mission_orchestrator import MissionOrchestrator
from llm_explainer import LLMExplainer

from dotenv import load_dotenv
load_dotenv()


app = Flask(__name__)

FRONTEND_DIR = Path(__file__).resolve().parent.parent / "frontend"


@app.route("/")
def home():
    return send_from_directory(
        FRONTEND_DIR,
        "index.html"
    )


@app.route("/api/analyze", methods=["POST"])
def analyze_mission():
    try:
        data = request.get_json()

        if not data or "mission" not in data:
            return jsonify({
                "error": "Mission input is required."
            }), 400

        user_input = data["mission"].strip()

        conversation_history = data.get(
            "conversation_history",
            []
        )

        if not user_input:
            return jsonify({
                "error": "Mission input cannot be empty."
            }), 400

        # Run the complete ORCA mission pipeline
        orchestrator = MissionOrchestrator()
        # result = orchestrator.run_mission(user_input)
        result = orchestrator.run_mission(
            user_input,
            conversation_history
            )

        recommendation = result["recommendation"]

        # Generate explanation using verified evidence
        explainer = LLMExplainer()
        explanation = explainer.explain_recommendation(
            recommendation,
            recommendation.evidence
        )

        response = {
            "mission": asdict(result["mission"]),
            "planner_result": result["planner_result"],
            "fused_data": result["fused_data"],
            "plans": result["plans"],
            "recommendation": asdict(recommendation),
            "ai_explanation": explanation
        }

        return jsonify(response)

    except Exception as e:
        import traceback

        print("\n========== ORCA API ERROR ==========")
        traceback.print_exc()
        print("====================================\n")

        return jsonify({
            "error": str(e)
        }), 500


if __name__ == "__main__":
    app.run(debug=True)