from agents.base_agent import BaseAgent

class QuestionAgent(BaseAgent):
    def can_handle(self, state):
        return "questions" in state["pending_tasks"]

    def act(self, state):
        state["outputs"]["questions"] = {
            "Informational": [
                "What is GlowBoost Vitamin C Serum?",
                "Who should use this serum?"
            ],
            "Usage": [
                "How do I apply GlowBoost?",
                "When should it be used?"
            ],
            "Safety": [
                "Does it cause irritation?",
                "Is it safe for sensitive skin?"
            ],
            "Purchase": [
                "What is the price of GlowBoost?",
                "Is it worth the price?"
            ],
            "Comparison": [
                "How is GlowBoost different from other serums?"
            ]
        }

        state["pending_tasks"].remove("questions")
        state["completed_tasks"].add("questions")
        return state
