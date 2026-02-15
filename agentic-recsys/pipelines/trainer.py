from data.load_data import load_data
from embeddings.embedder import Embedder
from embeddings.index import VectorIndex
from models.ranker import Ranker

users, items, interactions = load_data()

embedder = Embedder()
item_vecs = embedder.encode(items["description"].tolist())

index = VectorIndex(item_vecs.shape[1])
index.build(item_vecs)

ranker = Ranker()
X = interactions[["user_id", "item_id"]].values
y = interactions["clicked"].values
groups = interactions.groupby("user_id").size().values

ranker.train(X, y, groups)
