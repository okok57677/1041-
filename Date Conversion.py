def main():
	dateStr = input("Enter a date(yyyy.mm.dd):")
	yearStr,monthStr,dayStr = dateStr.split(".")
	months = ["一","二","三","四","五","六","七","八","九","十","十一","十二"]
	monthStr = months[int(monthStr)-1]
	yearStr = int(yearStr) - 1911
	print("民國",yearStr,"年",monthStr,"月",dayStr,"日")
main()
