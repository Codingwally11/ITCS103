import openpyxl as op

workbook = op.Workbook()

sheet = workbook.active

sheet ['A1'] = "Order Id"
sheet ['B1'] = "Customer Name"
sheet ['C1'] = "Contact"
sheet ['D1'] = "Service"
sheet ['E1'] = "Day"
sheet ['F1'] = "Time"

sheet ['A2'] = "1"



sheet ['B2'] = "Oswald Pastorfide"



sheet ['C2'] = "09918422225"



sheet ['D2'] = "Haircut"



sheet ['E2'] = "Saturday"


sheet ['F2'] = "7:00am - 9:00am"


workbook.save("Pastorfide_Database.xlsx")