from openai import OpenAI
from sklearn.cluster import KMeans

def cluster( terms, num_clusters ):
    # Vectorize our terms
    client = OpenAI()
    vectors = []
    for term in terms:
        response = client.embeddings.create(
                input = term,
                model="text-embedding-3-small"
                )
        vectors.append(response.data[0].embedding)

    kmeans = KMeans(n_clusters=num_clusters, random_state=0)
    labels = kmeans.fit_predict(vectors)
    return kmeans, labels

    vectors = vectorize(terms)
    kmeans, labels = cluster_vectors(vectors, 2)


test = ["apple", "orange", "pine tree"]

print(cluster(test, 2))
