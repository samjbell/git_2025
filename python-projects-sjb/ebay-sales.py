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

titles_list = ["Skate 2", "Terminator","Ride 3"]

values = [[title] for title in titles_list]

worksheet.update(range_name='A2:A4', values=values)


