import numpy as np;

def main() :
	arr = np.matrix([[1, 2], [3, 4]])
	#  eigenvalues, eigenvectors, and the determinant of a given square array
	eigens = np.linalg.eig(arr)
	eigenvalues = eigens[0]
	eigenvectors = eigens[1]

	det = np.linalg.det(arr)

	vec1 = np.array([1, 2, 3])
	vec2 = np.array([4, 5, 6])

	res = np.cross(vec1, vec2)

	A = np.array([[1, 2, -2], [2, 1, -5], [1, -4, 1]])
	b = np.array([-15, -21, 18])

	x = np.linalg.solve(A, b)

	print("Eigenvalues:", eigenvalues)
	print("Eigenvectors:", eigenvectors)
	print("Determinant:", det)
	print("Cross product:", res)
	print("Solution:", x)

if __name__ == "__main__" :
	main()