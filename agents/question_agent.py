class QuestionAgent:
    def generate(self, product):
        return {
            "Informational": [
                "What is GlowBoost Vitamin C Serum?",
                "What does Vitamin C do for skin?",
                "Who should use this serum?"
            ],
            "Usage": [
                "How do I apply GlowBoost?",
                "Can I use it daily?",
                "When should I apply it?"
            ],
            "Safety": [
                "Does it cause irritation?",
                "Is it safe for sensitive skin?",
                "Are there side effects?"
            ],
            "Purchase": [
                "What is the price of GlowBoost?",
                "Is it worth the price?",
                "How long does one bottle last?"
            ],
            "Comparison": [
                "How is GlowBoost different from other serums?",
                "Is GlowBoost better than Product B?",
                "Which serum is more affordable?"
            ]
        }
