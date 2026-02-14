import xgboost as xgb

class Ranker:
    def __init__(self):
        self.model = xgb.XGBRanker(
            objective="rank:pairwise",
            n_estimators=200,
            learning_rate=0.05
        )

    def train(self, X, y, groups):
        self.model.fit(X, y, group=groups)

    def predict(self, X):
        return self.model.predict(X)
