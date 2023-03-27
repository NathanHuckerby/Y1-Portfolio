from datetime import date

diary_entries = []

def save():
    with open("entries.txt", "w") as f:
        f.write("\n".join(diary_entries))
    

print("---------------------------------------------------------")
print("|                  Welcome to My Diary!                 |")
print("|      Please choose one of the options available:      |")
print("|                                                       |")
print("|      1. Add to My Diary                               |")
print("|      2. Display current My Diary entries              |")
print("|      3. Exit My Diary                                 |")
print("---------------------------------------------------------")

choice = int(input(""))

if choice == 1:
    print("\n")

    print("|   Please enter your diary entry:    |")
    entry = input("| ")
    today = date.today()
    date_time = today.strftime("%d/%m/%y")
    final_entry = (date_time, entry)
    print(final_entry)
    diary_entries.append(final_entry)
    save()