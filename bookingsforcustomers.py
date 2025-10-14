

def checkBooking():
    times = [["9:00", "5877RC"],["9:30","9655AS"], ["10:00","-"], ["10:30","8754TT"], 
    ["11:00","-"], ["11:30","87545SD"], ["13:00","9635GH"], ["13:30", "-"],["14:00","9874PL"],
    ["14:30", "9658SV"]]
    customerID = input("whata is your customerID?: ")
    for i, slot in enumerate(times):
        for idx, value in enumerate(slot):
            if value != "-":
                continue
            elif value=="-" :
                return f"time {times[i][0]} is aviable "
    return -1

print(checkBooking())