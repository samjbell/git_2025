import gspread

gc = gspread.service_account()

sh = gc.open("Ebay-Sales")

sh.sheet1.update_acell('A1', 'Titles')
sh.sheet1.update_acell('B1', 'Type')
sh.sheet1.update_acell('C1', 'Year')
sh.sheet1.update_acell('D1', 'Price')

worksheet = sh.sheet1

worksheet.format('A1:D1', {'textFormat': {'bold': True}})

worksheet.format("A1:D1", {
	"backgroundColor": {
	"red": 0.0,
	"green": 0.0,
	"blue": 0.0	
	},
	"horizontalAlignment": "CENTER",
	"textFormat": {
	"foregroundColor": {
	"red": 1.0,
	"green": 1.0,
	"blue": 1.0
	},
	"fontSize": 12,
	"bold":  True
	}
	})

worksheet.update_title("Ebay Listings")

titles_list = ["Monsters, Inc.", "Despicable Me 2","Ride 3"]

type_list = ["Blue-ray", "3D"]

title_values = [[title] for title in titles_list]

type_values = [[type] for type in type_list]





worksheet.update(range_name1='A2:A', values1=title_values, range_name2='B2:B', values2=type_values)


#A basic version of this would be to write out all of them but wouldn't be more prudent to write them all to a text file and then draw on them via an API call so that they are held within a database. So say I had a database of DVD's to sell and then I want to write them to a spreadsheet to then manipulate the data within their using the functions of Google Sheets. I could also make a steady start with BigQuery too.