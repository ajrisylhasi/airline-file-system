from operator import attrgetter
from collections import defaultdict

flights = []

class Flight:
  def __init__(self, airline, destination, passengers):
    self.airline = airline
    self.destination = destination
    self.passengers = passengers

  def getFlight(self):
    return f"{self.airline} {self.destination} {self.passengers}"

def getFlightIf(self):
    if not isinstance(self, str):
      return self.getFlight()
    else:
      return self

with open('input.txt') as f:
  for flight in f:
    flightAttributes = flight.split()
    airline = flightAttributes[0]
    destination = flightAttributes[1] 
    passengers = int(flightAttributes[2])
    flights.append(Flight(airline, destination, passengers))

countFrankfurtFlights = sum(f.destination == "Frankfurt" for f in flights)
maxPassengers = "The file is empty!"
firstSmallFlight = getFlightIf(next((f for f in flights if f.passengers < 100), "There is no flight with passengers less than 100."))
busiestAirline = "The file is empty!"

if len(flights) > 0:
  maxPassengers = max(flights, key=attrgetter('passengers')).getFlight()
  groupedAirlines = defaultdict(list)

  for obj in flights:
      groupedAirlines[obj.airline].append(obj)

  busiestAirline = []

  for k in groupedAirlines.values():
    busiestAirline.append([k[0].airline, sum(f.passengers for f in k)])

  busiestAirline = " ".join(map(str, max(busiestAirline, key=lambda x: x[1])))

print(countFrankfurtFlights)
print(maxPassengers)
print(firstSmallFlight)
print(busiestAirline)
