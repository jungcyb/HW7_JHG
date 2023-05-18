import numpy as np

def main() :
	docs = np.array([
		[1, 1, 0, 1, 0, 1],
		[1, 1, 1, 0, 1, 0],
		[1, 1, 0, 1, 0, 0]
	]);

	query = np.array([1, 1, 0, 0, 1, 0])
	
	res = []

	for i in range(0, 3) :
		print("doc{0}={1:.2f}".format(i, np.dot(docs[i], query) / (np.linalg.norm(docs[i]) * np.linalg.norm(query))))


if __name__ == "__main__" :
	main()