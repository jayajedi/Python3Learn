from countries import country_list
#print(country_list)
country_count={}
for country in country_list:
    if country not in country_count:
        country_count.update({country:1})
    else:
        country_count[country]+=1
print(country_count)
Hello How are you?