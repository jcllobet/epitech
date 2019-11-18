class LinearRegression:
    def fit(self, X, y):
        self.b = ((X - X.mean())*(y - y.mean())).sum() / ((X - X.mean())**2).sum()
        self.a = y.mean() - (self.b * X.mean())
        return self

    def predict(self, X):
        return self.a + self.b * X
