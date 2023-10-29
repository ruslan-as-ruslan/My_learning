def greet(name, *args):
    
    for i in args:
        name += ' and ' + i 
    
    return f"Hello, {name}!"

print(greet('Timur'))
print(greet('Timur', 'Roman'))
print(greet('Timur', 'Roman', 'Ruslan'))