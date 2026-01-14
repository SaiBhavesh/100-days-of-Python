import time 
#Get input from the user
start = int(input("Enter a number: ")) 
print("Countdown begins!") 
#Start countdown using while loop
while start > 0: 
  print(start) 
  time.sleep(1) 
  start-=1 
  # Printing the final nessage
print("Stay Consistent!! Happy New Year")
