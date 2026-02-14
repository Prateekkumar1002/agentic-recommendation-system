import random

class OptimizerAgent:
    def suggest(self):
        return {
            "learning_rate": random.choice([0.01, 0.05, 0.1]),
            "n_estimators": random.choice([100, 200, 300])
        }
