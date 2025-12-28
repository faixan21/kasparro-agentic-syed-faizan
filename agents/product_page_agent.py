class ProductPageAgent:
    def generate(self, product, benefits, usage):
        return {
            "product_name": product["name"],
            "concentration": product["concentration"],
            "benefits": benefits,
            "usage": usage,
            "price": product["price"]
        }
