import pandas as pd

def main() :
	pd.set_option('mode.chained_assignment', None)
	data = pd.read_csv("gender2.csv", encoding='cp949', index_col=0)
	new_data = data[["2022년_계_총인구수", "2022년_남_총인구수", "2022년_여_총인구수"]]
	new_data.rename(columns={
		"2022년_계_총인구수": "Total", 
		"2022년_남_총인구수": "Male", 
		"2022년_여_총인구수": "Female"
	}, inplace=True)
	
	print(new_data)

if __name__ == "__main__" :
	main()