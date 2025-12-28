from agents.data_parser_agent import DataParserAgent
from agents.question_agent import QuestionAgent
from agents.faq_agent import FAQAgent
from agents.product_page_agent import ProductPageAgent
from agents.comparison_agent import ComparisonAgent
from logic_blocks.benefit_block import generate_benefits
from logic_blocks.usage_block import generate_usage
import json, os

class Orchestrator:
    def run(self):
        product = DataParserAgent().parse()
        questions = QuestionAgent().generate(product)

        faq = FAQAgent().generate(questions, product)
        product_page = ProductPageAgent().generate(
            product,
            generate_benefits(product),
            generate_usage(product)
        )
        comparison = ComparisonAgent().generate(product)

        os.makedirs("output", exist_ok=True)
        with open("output/faq.json", "w", encoding="utf-8") as f:
            json.dump(faq, f, indent=2, ensure_ascii=False)
        with open("output/product_page.json", "w", encoding="utf-8") as f:
            json.dump(product_page, f, indent=2, ensure_ascii=False)
        with open("output/comparison_page.json", "w", encoding="utf-8") as f:
            json.dump(comparison, f, indent=2, ensure_ascii=False)
