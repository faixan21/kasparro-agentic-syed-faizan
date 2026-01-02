from agents.base_agent import BaseAgent
from templates.faq_template import FAQ_TEMPLATE

class FAQAgent(BaseAgent):
    def can_handle(self, state):
        return "faq" in state["pending_tasks"] and "questions" in state["outputs"]

    def act(self, state):
        product = state["product"]
        questions = state["outputs"]["questions"]

        items = []
        for category, qs in questions.items():
            q = qs[0]
            ql = q.lower()

            if "apply" in ql:
                answer = product["usage"]
            elif "price" in ql:
                answer = f"The product is priced at ₹{product['price']}."
            elif "irritation" in ql or "safe" in ql:
                answer = product["side_effects"]
            else:
                answer = f"Suitable for {', '.join(product['skin_type'])} skin types."

            items.append({
                "question": q,
                "answer": answer
            })

        state["outputs"]["faq"] = {
            "template": FAQ_TEMPLATE["name"],
            "items": items[:FAQ_TEMPLATE["min_items"]]
        }

        state["pending_tasks"].remove("faq")
        state["completed_tasks"].add("faq")
        return state
