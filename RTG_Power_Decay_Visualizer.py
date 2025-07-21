import radioactivedecay as rd
import matplotlib.pyplot as plt

def thermal_power(mass): 
    return round(mass * 0.56, 6)  # W/g

def decay(years):
    nuclide = rd.Inventory({"Pu-238": 4.8}, 'kg')
    decayed = nuclide.decay(years, 'y')
    masses = decayed.masses('g')
    return round(masses['Pu-238'], 6)

def graph_thermalpower():
    years = list(range(0, 87))  # 87 years for Pu-238
    pu_masses = [decay(year) for year in years]
    ypower = [thermal_power(mass) for mass in pu_masses]
    ymin = [power * 0.05 for power in ypower]
    ymax = [power * 0.08 for power in ypower]

    plt.plot(years, ypower, label="Total Thermal Power Generated", color='blue')
    plt.plot(years, ymax, label="Actual Maximum Thermal Power", color='purple')
    plt.plot(years, ymin, label="Actual Minimum Thermal Power", color='red')
    plt.xlabel("Years")
    plt.ylabel("Thermal Power (W)")
    plt.title("Thermal Power of Pu-238 Over Time")
    plt.grid()
    plt.legend()
    plt.show()

def main():
    year_input = int(input("\nEnter the number of years for decay: "))
    pu_left = decay(year_input)
    difference = 4800 - pu_left
    print(f"The amount of remaining Pu-238 after {year_input} years will be {pu_left:.6f}g")
    print(f"The difference in mass is {difference:.6f}g")
    print(f"\nPu-238 emits 0.56W of heat per gram.\nTherefore, the thermal power after {year_input} years will be {thermal_power(pu_left)}W, compared to the initial 2688W at 4800g.")
    print(f"However, thermoelectric materials used in thermocouple arrays have typical efficiencies of 5-8%.\nSo the ACTUAL thermal power output would be {thermal_power(pu_left) * 0.05}W to {thermal_power(pu_left) * 0.08}W.")

    graph_thermalpower()

if __name__ == "__main__":
    main()