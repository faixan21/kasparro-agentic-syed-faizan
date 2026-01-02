from agents.base_agent import BaseAgent
from templates.comparison_template import COMPARISON_TEMPLATE

class ComparisonAgent(BaseAgent):
    def can_handle(self, state):
        return "comparison" in state["pending_tasks"]

    def act(self, state):
        product_b = {
            "name": "Radiant C Serum",
            "ingredients": ["Vitamin C"],
            "benefits": ["Brightening"],
            "price": 899
        }

        state["outputs"]["comparison_page"] = {
            "template": COMPARISON_TEMPLATE["name"],
            "GlowBoost": state["product"],
            "ProductB": product_b
        }

        state["pending_tasks"].remove("comparison")
        state["completed_tasks"].add("comparison")
        return state
