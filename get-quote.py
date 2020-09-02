import random
# above line will import the module of random

def go(): # This line tells it what to do
  # print("Keep it logically awesome.")

  f = open("quotes.txt") # f = file
  last = 13
  rnd = random.randint(0, last)
  #  The above 2 lines set the last number or length at 0 and stores teh random number in rnd.  
  quotes = f.readlines()
  f.close()

  print(quotes)
  #  above will print out all the quotes in the file in the form of an array

  print(quotes[0])
# above will print out the 1st index, but not in an array

  print(quotes[13])

  print(quotes[rnd])
  #  above will now call on the random feature and print 1 quote at random.


if __name__== "__main__":
  go()
