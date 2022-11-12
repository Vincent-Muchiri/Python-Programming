kenyan_counties = ["Mombasa", "Kwale", "Kilifi", "Tana River", "Lamu", "Taita Taveta", "Garissa", "Wajir", "Mandera", "Marsabit", "Isiolo", "Meru",
"Tharaka Nithi", "Embu", "Kitui", "Machakos", "Makueni", "Nyandarua", "Nyeri", "Kirinyaga", "Muranga", "Kiambu", "Turkana", "West Pokot", "Samburu",
"Trans Nzoia", "Uasin Gishu", "Elgeyo Marakwet", "Nandi", "Baringo", "Laikipia", "Nakuru", "Narok", "Kajiado", "Kericho", "Bomet", "Kakamega",
"Vihiga", "Bungoma", "Busia", "Siaya", "Kisumu", "Homa Bay", "Migori", "Kisii", "Nyamira", "Nairobi City"]

county_no6 = kenyan_counties[7]
print(county_no6)

last_county = kenyan_counties[-1] #Cannot have -0
print(last_county)

#Adding an extra county
kenyan_counties.append("Thika")
kenyan_counties.extend(["Ruiru", "Juja"])
kenyan_counties.remove(kenyan_counties[-10])
print(kenyan_counties)
last_county = kenyan_counties[-1]
print(last_county)

num = ["1", "9"]
int_num = [1, 9]

total = 0
for elem in int_num:
    total += elem
print(f"The total is {total}")

total = 0
for elem in num:
    total += int(elem)
print(f"The total is {total}")

new_list = [1, 2, 3]
new_list.insert(0, 0)
print(new_list)

for index in range(0,len(kenyan_counties), 2):
    print(index)
