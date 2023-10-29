def info_kwargs(**kwargs):

    for item in sorted(kwargs.items()):
        print(f"{item[0]}: {item[1]}")


info_kwargs(first_name='Timur', last_name='Guev', age=28, job='teacher') 

print(input)