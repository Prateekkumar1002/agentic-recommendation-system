#Evaluator Agent 
class EvaluatorAgent:
    def evaluate(self, metrics):
        if metrics["ctr"] < 0.12:
            return "RETRAIN"
        return "OK"
