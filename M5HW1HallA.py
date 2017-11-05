# CTI 110
# M5HW1: Distance Traveled
# Hall, A
# 17 Oct 2017

# Calcualte Distance Traveled
# Formula is distance = speed * time

# Ask User To Enter in Speed and Time

def main():
    carSpeed = int(input('What is the speed of the vehicle in mph?:'))

    driveTime = int(input('How many hours has it traveled?:'))


    # Command to Print out display

    print ('Hour','\t','Distance Traveled')
    print ('-----------------------------------')


    # For loop to caluclate the distance traveled
    for hour in range (1, driveTime + 1):
        distanceTraveled = carSpeed * hour
        print (hour,'\t',distanceTraveled)
        
        
main()        
    


    
    

