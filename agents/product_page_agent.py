from agents.base_agent import BaseAgent
from templates.product_template import PRODUCT_TEMPLATE

class ProductPageAgent(BaseAgent):
    def can_handle(self, state):
        return "product_page" in state["pending_tasks"]

    def act(self, state):
        p = state["product"]

        state["outputs"]["product_page"] = {
            "template": PRODUCT_TEMPLATE["name"],
            "product_name": p["name"],
            "concentration": p["concentration"],
            "benefits": p["benefits"],
            "usage": p["usage"],
            "price": p["price"]
        }

        state["pending_tasks"].remove("product_page")
        state["completed_tasks"].add("product_page")
        return state
