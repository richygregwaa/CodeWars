def capital(capitals):
    capital_ans = [];
    for i_dict in capitals:
        first_key = list(i_dict.keys())[0];
        answer = 'The capital of ' + i_dict[first_key] + ' is ' + i_dict['capital'];
        capital_ans.append (answer)
    return capital_ans


def capital2(capitals):
    return [f"The capital of {c.get('state') or c['country']} is {c['capital']}" for c in capitals]
    # Read about f strings (formatting) - https://realpython.com/python-f-strings/



# creating a new dictionary
res_data = [{'state': 'Maine', 'capital': 'Augusta'}];
res1 = [{'state': 'Maine', 'capital': 'Augusta'}];
res2 = [{'country' : 'Spain', 'capital' : 'Madrid'}]
res3 = [{"state" : 'Maine', 'capital': 'Augusta'}, {'country': 'Spain', "capital" : "Madrid"}]

# My Solution
print (capital(res1));
print (capital(res2));
print (capital(res3));

print("\n")
# Alternative Solution
print (capital2(res1));
print (capital2(res2));
print (capital2(res3));
