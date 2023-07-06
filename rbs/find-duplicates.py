from openpyxl import load_workbook
from difflib import SequenceMatcher
workbook = load_workbook(filename='test-data.xlsx', read_only=True)
sheet = workbook.active

account_names = []
row, col = 3, 5
val = sheet.cell(row=row, column=col).value
while val != None:
    #print(val)
    account_names.append(val)
    row += 1
    val = sheet.cell(row=row, column=col).value

def compare_strings(a: str, b: str):
    return SequenceMatcher(None, a.lower(), b.lower()).ratio()

def find_duplicates(acc_names):
    potential_duplicates = []
    while len(acc_names) > 0:
        base = acc_names[0]
        base_in_list = False
        for i in range(1, len(acc_names)):
            similar = False
            print(base, acc_names[i])
            if acc_names[i] == base:
                similar = True
            elif compare_strings(base, acc_names[i]) > 0.85:
                similar = True

            if similar:
                if not base_in_list:
                    potential_duplicates.extend([base, acc_names[i]])
                    base_in_list = True
                else:
                    potential_duplicates.append(acc_names[i])
        acc_names.remove(acc_names[0])

    return potential_duplicates

print(account_names)
print(find_duplicates(account_names))



    

# Test, test1, the test, tests, your mom, test


