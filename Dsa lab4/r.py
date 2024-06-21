if((len(self.vehicles)==0) or (vehicle not in self.vehicles)):
          vehicle = Vehicle(vehicle_number,seating_capacity)
          self.vehicles.append(vehicle)

        #if the vehicle already exists in the self.vehicles list it will retrieve the vehicle object from there  

        else:
            temp=self.vehicles[0]
            i=0
            while(temp.get_vehicle_number()!=vehicle_number):
                i+=1
                temp=self.vehicles[i]
            vehicle=temp   
                  

        new_trip=Trip(vehicle,pick_up_location,drop_location,departure_time)#creates a new trip object
        vehicle.add_trip(new_trip)#adds that trip object to vehicle