dict_1 ={}
dict_2 = dict()

print(type(dict_1))
print (type(dict_2))
age_dict = {


    'key' : 'value',
    'karim': 20,
    'abul': 34,
    'kasem': 12
}
#print (age_dict)
#print(age_dict.keys())
#print(age_dict.items())
#print(age_dict.values())
print(age_dict['abul'])
print(age_dict.get('Abul'))
age_dict['python']= 100
print(age_dict)
del age_dict['abul']
print(age_dict)