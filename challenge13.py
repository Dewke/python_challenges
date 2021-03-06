
u_in = int(input('How many Fibonnaci numbers should I generate?: '))

def fibonaci_generate(number):
    if number == 0:
        return []
    if number == 1:
        return [1]
    elif number == 2:
        return [1, 1]
    elif number > 2:
        fib = [1, 1]
        i = 2
        while i < number:
            fib.append(fib[i-2]+fib[i-1])
            i = i + 1
        return fib

def fibonaci_generate_rec(number):
  if number == 0:
    return []
  if number == 1:
    return [1]
  elif number == 2:
    return [1, 1]
  else:
    fib = fibonaci_generate_rec(number-1)
    fib.append(fib[-1]+fib[-2])
    return fib

print(fibonaci_generate(u_in))
print(fibonaci_generate_rec(u_in))
