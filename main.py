import re

import csv
with open("phonebook_raw.csv") as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)


pattern = r"(\+7|8).*?(\d{3}).*?(\d{3}).*?(\d{2}).*?(\d{2})(\s\доб.\s\d+)?(\s\((доб.\s\d+)\))?"
pattern_1 =r"\S+"
substitution = r"+7 (\2) \3-\4-\5 \6 \8"


rows = []
for contacts_list_1 in contacts_list:
  row = []
  i=0
  names_count = 0
  for contacts_list_2 in contacts_list_1:
    if i>2:
      number_fones = re.findall(pattern, contacts_list_2)
      text_phones_res = re.sub(pattern, substitution, contacts_list_2)
      row.append(text_phones_res)
    else:
      names = re.findall(pattern_1, contacts_list_2)
      names_count += len(names)
      if i == 2:
        x = 3 - names_count
        for j in range(x):
          row.append('')
      for name in names:
          row.append(name)
    i+=1
  rows.append(row)


rows_new = []
for i in range(len(rows)):
  for j in range(len(rows)):
    if rows[i][:2] == rows[j][:2]:
      rows[i] = [x or y for x, y in zip(rows[i], rows[j])]
  if rows[i] not in rows_new:
    rows_new.append(rows[i])
rows_new.sort()
rows = rows_new
print(rows)


with open("phonebook.csv", "w", encoding='utf8') as f:
  datawriter = csv.writer(f, delimiter=',')
  datawriter.writerows(rows)