import faiss
import numpy as np

class VectorIndex:
    def __init__(self, dim):
        self.index = faiss.IndexFlatL2(dim)

    def build(self, vectors):
        self.index.add(vectors)

    def search(self, query, k=10):
        return self.index.search(query, k)
