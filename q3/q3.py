import pandas as pd

def main() :
	data = pd.DataFrame([
		[1000, 25],
		[280, 120],
		[900, 30]
	], 
	index=[f"store{i}" for i in range(1, 4)],
	columns=["unit price", "number"])
	print(data)
	
	data["total price"] = data["unit price"] * data["number"]
	print(data)

	data.sort_values(by="total price", ascending=True)
	print(data[1:3])

if __name__ == "__main__" :
	main()