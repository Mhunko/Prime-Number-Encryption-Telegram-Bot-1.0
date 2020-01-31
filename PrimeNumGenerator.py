import random




prime = False
num = 1000
def gen(num):
    prime = False
    while prime is False:
        num = random.randrange(3, 1000)#change to control which range of numbers you want to generate

        if num > 1:

            # Iterate from 2 to n / 2
            for i in range(2, num // 2):

                # If num is divisible by any number between
                # 2 and n / 2, it is not prime
                if (num % i) == 0:
                    print(num, "is not a prime number")
                    break
                    prime = False

            else:
                print(num, "is a prime number")
                prime = True
                return num
    return num
#prime1 = gen(num)
#prime2 = gen(num)

#print(prime1)
#print(prime2)
