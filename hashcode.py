class ride:

    def __init__(self, i, sc, ec, es, lf):
        self.id = i
        self.start_coordinate = sc
        self.end_coordinate = ec
        self.earliest_start = es
        self.latest_finish = lf


class car:

    def __init__(self, id):
        self.id = id
        self.available = True
        self.current_position = [0,0]
        self.step_busy = 0
        self.current_ride = -1
        self.rides_done = []

    # def ridesDone:
    #     return(self.rides_done)
    # def getCarID:
    #     return(self.)

    # def updateAvailableCars(self):

if __name__ == "__main__":
    timestamp = 0
    available_cars = []
    not_available_cars = []

#Retrieve sentences
    filer = open('d_metropolis.in', 'r')
    filew = open('d_metropolis.out', 'w')


    inp = filer.read().split('\n')
    first = inp[0].split(' ')
    rows= int(first[0])
    columns=  int(first[1])
    vehicles= int(first[2])
    num_rides = int(first[3])
    bonus = int(first[4])
    steps = int(first[5])

    #Car Objects
    for i in range(vehicles):
        carObj = car(i)
        available_cars.append(carObj)
    #Ride Objects
    rides=[]
    for i in range(num_rides):
        # print(filer.readlines(i))
        input = inp[i+1].split(' ')


        start_coordinates = [int(input[0]), int(input[1])]
        end_coordinates = [int(input[2]), int(input[3])]
        earliest_start = int(input[4])
        latest_finish = int(input[5])
        rideObject = ride(i, start_coordinates, end_coordinates,earliest_start, latest_finish)
        rides.append(rideObject)

    #Sort Rides according to start time
    sorted_rides = sorted(rides, key= lambda x: x.earliest_start)

    while(timestamp<=steps):
        for carq in not_available_cars:
            if carq.step_busy == timestamp:
                carq.available = True
                # carq.current_position = sorted_rides[max_prof].end_coordinate
                carq.step_busy = 0
                # carq.rides_done.append(sorted_rides[max_prof].id)
                carq.current_ride = -1
                # available_cars.append(carq)
            available_cars.append(carq)
            not_available_cars.remove(carq)
        for carq in available_cars:
            profit=[]
            for i,rideq in enumerate(sorted_rides):
                # rider ka disrtnce
                curr_distance = abs(rideq.start_coordinate[0]-rideq.end_coordinate[0])+abs(rideq.start_coordinate[1]-rideq.end_coordinate[1])
                # rider tak pohochne ka dist
                curr_time_to_reach = timestamp+(abs(carq.current_position[0]-rideq.start_coordinate[0])+abs(carq.current_position[1]-rideq.start_coordinate[1]))
                # time pe pohoch
                curr_bonus = bonus if curr_time_to_reach <= rideq.earliest_start else 0
                # ride dropped before latest finish
                curr_onTime = curr_distance if curr_time_to_reach+curr_distance <= rideq.latest_finish else 0
                profit.append(curr_bonus + curr_onTime)
            max_prof = profit.index(max(profit)) if len(profit)>0 else -1
            if max_prof !=-1:
                carq.available = False
                carq.current_position = sorted_rides[max_prof].end_coordinate
                carq.step_busy = curr_time_to_reach+curr_distance
                carq.rides_done.append(str(sorted_rides[max_prof].id))
                carq.current_ride=sorted_rides[max_prof].id
                available_cars.remove(carq)
                not_available_cars.append(carq)
                sorted_rides.remove(sorted_rides[max_prof])
        timestamp+=1

    answer = []
    if (len(available_cars)>0):
        if (len(not_available_cars)>0):
            # print(available_cars)
            temp = available_cars+ not_available_cars
            answer = sorted(temp, key=lambda x:x.id)
        else:
            answer = sorted(available_cars, key=lambda x:x.id)
    else:
        answer = sorted(not_available_cars, key=lambda x:x.id)
    for i in range(vehicles):
        text=str(len(answer[i].rides_done))+' '+(' ').join(answer[i].rides_done)+'\n'
        filew.write(text)