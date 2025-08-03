import csv

input_file = "ButterDict.csv"
output_file = "ButterDict.txt"

with open(input_file, "r", encoding="utf-8") as csvfile:
    reader = csv.DictReader(csvfile)
    passwords = [row["password"] for row in reader if row["password"].strip()]

with open(output_file, "w", encoding="utf-8") as txtfile:
    for pwd in passwords:
        txtfile.write(pwd + "\n")

print(f"成功将 {len(passwords)} 个密码写入 {output_file}")
