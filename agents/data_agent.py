from agents.base_agent import BaseAgent

class DataAgent(BaseAgent):
    def can_handle(self, state):
        return state["product"] is None

    def act(self, state):
        state["product"] = {
            "name": "GlowBoost Vitamin C Serum",
            "concentration": "10% Vitamin C",
            "skin_type": ["Oily", "Combination"],
            "ingredients": ["Vitamin C", "Hyaluronic Acid"],
            "benefits": ["Brightening", "Fades dark spots"],
            "usage": "Apply 2–3 drops in the morning before sunscreen",
            "side_effects": "Mild tingling for sensitive skin",
            "price": 699
        }

        state["pending_tasks"].update({
            "questions",
            "faq",
            "product_page",
            "comparison"
        })

        state["completed_tasks"].add("data_loaded")
        return state
