import faiss
import numpy as np

class VectorIndex:
    def __init__(self, dim):
        self.index = faiss.IndexFlatL2(dim) # Flat Indexing

    def build(self, vectors):
        self.index.add(vectors)

    def search(self, query, k=10): # Top K=10
        return self.index.search(query, k)


