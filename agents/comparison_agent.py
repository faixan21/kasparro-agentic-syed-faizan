class ComparisonAgent:
    def generate(self, product):
        product_b = {
            "name": "Radiant C Serum",
            "ingredients": ["Vitamin C"],
            "benefits": ["Brightening"],
            "price": 899
        }

        return {
            "GlowBoost": product,
            "ProductB": product_b
        }
