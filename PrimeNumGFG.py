

import time


from decimal import Decimal
#Euclid's algorithm for determining the greatest common divisor
def rsa(no):
	start_time = time.time()
	def gcd(a,b):
		if b==0:
			return a
		else:
			return gcd(b,a%b)

	from PrimeNumGenerator import gen
	num = 10
	prime1 = gen(num)
	prime2 = gen(num)
	print(prime1)
	print(prime2)

	p = prime1
	q = prime2
	#p = int(input('Enter the value of p = '))
	#q = int(input('Enter the value of q = '))
	#from main import message

	#no = int(input('Enter the value of text = '))
	n = p*q
	t = (p-1)*(q-1)

	for e in range(2,t):
		if gcd(e,t)== 1:
			break

	#chooses d (d = (1 + (k*phi))/e)    k = i
	for i in range(1,10):
		x = 1 + i*t
		if x % e == 0:
			d = int(x/e)
			break
	ctt = Decimal(0)
	ctt =pow(no,e)
	ct = ctt % n

	dtt = Decimal(0)
	dtt = pow(ct,d)
	dt = dtt % n

	print('n = '+str(n)+' e = '+str(e)+' t = '+str(t)+' d = '+str(d)+' cipher text = '+str(ct)+' decrypted text = '+str(dt))
	timing = (time.time() - start_time)
	message = 'first prime number = '+str(p)+' second prime number = '+str(q)+' n = '+str(n)+' public key = '+str(e)+' private key = '+str(t)+' d = '+str(d)+' cipher text = '+str(ct)+' decrypted text = '+str(dt) + " time_took [beta] " + str(timing) + " seconds"

	#print(i)

	return message


	#print("--- %s seconds ---" % (time.time() - start_time))
