import openpyxl
from datetime import datetime
import time

def favorite_people_recorder():
    cyear = datetime.now().year
    
    records = []
    
    print("\n=== 𝑭𝒂𝒗𝒐𝒓𝒊𝒕𝒆 𝑷𝒆𝒐𝒑𝒍𝒆 𝑹𝒆𝒄𝒐𝒓𝒅𝒆𝒓 ===")

    for i in range(1, 4):
        print(f"Person {i}:")
        fname = input("Enter First Name: ").strip()
        lname = input("Enter Last Name: ").strip()

        while True:
            try:
                byear_str = input("Enter Birth Year: ").strip()
                birthyear = int(byear_str)
                if birthyear <1900 or birthyear > cyear:
                    print(f"Input a valid birth year between 1900 and {cyear}.")
                else:
                    break
            except ValueError:
                print("Invalid input. Please enter a numeric year.")
        age = cyear - birthyear

        person_id = i
        
        record = {
        "ID": person_id,
        "First Name": fname,
        "Last Name": lname,
        "Birth Year": birthyear,
        "Age": age
        }
        records.append(record)
        print() 

    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Favorite People"

    headers = ["ID", "First Name", "Last Name", "Birth Year", "Age"]
    ws.append(headers)

    for record in records:
        ws.append([
            record["ID"],
            record["First Name"],
            record["Last Name"],
            record["Birth Year"],
            record["Age"]
        ])

    excel_favperson = "favorite_people.xlsx"
    wb.save(excel_favperson)
    print("=𝑭𝒂𝒗𝒐𝒓𝒊𝒕𝒆 𝒑𝒆𝒐𝒑𝒍𝒆 𝒔𝒂𝒗𝒆𝒅 𝒔𝒖𝒄𝒄𝒆𝒔𝒔𝒇𝒖𝒍𝒍𝒚!=\n")

    print("\t\t=== 𝑭𝑨𝑽𝑶𝑹𝑰𝑻𝑬 𝑷𝑬𝑶𝑷𝑳𝑬 𝑳𝑰𝑺𝑻 ===")
    print(f"{"('ID',":<5} {"'First Name',":<15} {"'Last Name',":<15} {"'Birth Year',":<12} {"'Age')":<5}")
    
    print("=" * 60) #Table seperator
    
    for record in records:
        time.sleep(0.2)
        print(f"({record['ID']},    '{record['First Name']}',        '{record['Last Name']}',          {record['Birth Year']},        {record['Age']})")
        
favorite_people_recorder()
input("\nPress enter to exit...")