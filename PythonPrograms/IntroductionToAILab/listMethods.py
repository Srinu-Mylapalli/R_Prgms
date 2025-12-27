num=[1,2,3,4,5]
prime=[2,3,5,7,11]
print(f"numbers: {num}\n prime numbets: {prime}")
prime.append(13)
print(f"after appending 13 into prime numbers: {prime}")
num.extend(prime)
print(f"after add prime numbers into numbers: {num}")
print(num.pop())
del num
try:
    print(num)
except Exception as e:
    print(e)
prime.clear()
print(prime)
