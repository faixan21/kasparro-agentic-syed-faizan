import json
from core.state import initial_state
from core.orchestrator import Orchestrator

from agents.data_agent import DataAgent
from agents.question_agent import QuestionAgent
from agents.faq_agent import FAQAgent
from agents.product_page_agent import ProductPageAgent
from agents.comparison_agent import ComparisonAgent

state = initial_state()

agents = [
    DataAgent(),
    QuestionAgent(),
    FAQAgent(),
    ProductPageAgent(),
    ComparisonAgent()
]

orchestrator = Orchestrator(agents)
final_state = orchestrator.run(state)

with open("output/faq.json", "w", encoding="utf-8") as f:
    json.dump(final_state["outputs"].get("faq", []), f, indent=2, ensure_ascii=False)

with open("output/product_page.json", "w", encoding="utf-8") as f:
    json.dump(final_state["outputs"].get("product_page", {}), f, indent=2, ensure_ascii=False)

with open("output/comparison_page.json", "w", encoding="utf-8") as f:
    json.dump(final_state["outputs"].get("comparison_page", {}), f, indent=2, ensure_ascii=False)

print("Dynamic multi-agent system executed successfully.")
