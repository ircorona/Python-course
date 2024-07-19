def fibonacci (limit):
    a,b = 0,1
    while a<limit:
        yield a 
        a,b = b, a+b 

for num in fibonacci(50):
    print(num)

def story():
    yield "Once upon a time, there was a brave knight."
    yield "The knight fought a dragon."
    yield "The knight saved the kingdom."
    yield "Everyone lived happily ever after."
for part in story():
    print(part)
