# driving test client

from drivetest_simple import Car
import os

def test(car:Car,message="", distance=20):
    results={
        "fuel":False,
        "engine":False,
        "gear":False
    }
    menu_items="""
        "[A]dd Fuel"
        "[E]ngine On"
        "[G]ear Shift"
        "[R]eady"
        "[Q]uit"
    """
    os.system("clear")
    car.print_status(message)
    while True:
        print(menu_items)
        choice=input("Command: ")
        if choice.upper()=='A':
            results["fuel"]=car.add_fuel()
        if choice.upper()=='E':
            results["engine"]=car.turn_on()
        if choice.upper()=='G':
            results["gear"]=car.switch_gear()
        if choice.upper()=='R':
            results["fuel"]=car.enough_fuel(distance)
            grades={True:"PASSED", False:"FAILED"}
            report=f"""
            result: {grades[all(results.values())]}
            """
            car.print_status(report)
            [print(f"{k}={grades[v]}") for k,v in zip(["fuel","engine","gear"],results.values())]
            break
        if choice=='Q':
            exit()

car1=Car(fuel_amount=1)
distance=2000
test(car1,f"Begin Test {distance} Km",distance)
