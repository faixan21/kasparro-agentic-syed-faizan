class FAQAgent:
    def generate(self, questions, product):
        faqs = []

        for category in questions:
            q = questions[category][0]
            q_lower = q.lower()

            if "apply" in q_lower or "use" in q_lower:
                answer = product["usage"]

            elif "price" in q_lower:
                answer = f"The product is priced at ₹{product['price']}."

            elif "irritation" in q_lower or "side effect" in q_lower or "safe" in q_lower:
                answer = product["side_effects"]

            else:
                answer = f"{product['name']} is suitable for {', '.join(product['skin_type'])} skin types."

            faqs.append({
                "question": q,
                "answer": answer
            })

        return faqs[:5]
