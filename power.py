import sys

def power():
	base = int(sys.argv[1])
	power = int(sys.argv[2])
	result = 1
	for i in range(power):
	   result = result*base
	return result


if __name__ == "__main__":
   print(power())
