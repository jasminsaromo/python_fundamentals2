def racer(id):
    print(f"How far did person {id} run (in metres)?")
    distance = float(input())
    print(f"How long (in minutes) did person {id} run take to run {distance} metres?")
    mins = float(input())

    return distance/(mins*60)

speed1 = racer(1)
speed2 = racer(2)
speed3 = racer(3)

if speed3 > speed2 and speed3 > speed1:
  print("Person 3 was the fastest at {} m/s".format(speed3))
elif speed2 > speed3 and speed2 > speed1:
  print("Person 2 was the fastest at {} m/s".format(speed2))
elif speed1 > speed3 and speed1 > speed2:
  print("Person 1 was the fastest at {} m/s".format(speed1))
elif speed1 == speed2 and speed2 == speed3:
  print("Everyone tied at {} m/s".format(speed1))
else:
  print("Well done everyone!")