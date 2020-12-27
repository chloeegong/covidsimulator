import Covid

def main():
    option = ""
    while option != '0':
        print("""
        1 COVID-19 Simulation (No Lockdown) 
        2 COVID-19 Simulation (Lockdown) 
        """)
        option = input()
        if option == "1":
            covid = Covid.Covid(60)
            day = int(input("Enter the range of days for the simulation: "))
            covid.simulation(day)
        elif option == "2":
            covid = Covid.Covid(5)
            day = int(input("Enter the range of days for the simulation: "))
            covid.simulation(day)

if __name__ == "__main__":
    main()