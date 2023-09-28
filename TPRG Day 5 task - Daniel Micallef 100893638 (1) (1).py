# circalc.py -- LCR calculator as well as parallel/series resistors and RC time constant for TPRG 2131 Week 3 Day 5
# Assignment 5 for Tprg 2131 intro week 1-2
# Daniel Micallef, 100893638, TPRG 2131-01.
# Note: I did not need to change my code for this challenge as it had already met the requirements for the last challenge as well as this challenge.
# September 20, 2023
# This program is strictly my own work. Any material 
# beyond course learning materials that is taken from 
# the Web or other sources is properly cited, giving
# credit to the original author(s).
# Citations:
# where I learned about the calculations I used then modified them
# for my uses: "https://www.toppr.com/guides/physics/waves/what-is-resonant-frequency-and-how-to-calculate-it/"
# I used python libraries "https://docs.python.org/3/search.html?q=function"
# as well as powerpoints from previous classes to learn about functions and output statments
# I asked chat gpt "How to use functions in a print statment" on september 14.
# I asked chat gpt "How to use range on python?" as well as "How to have python choose a input to do calculations on?". September 15
# I asked chat gpt "How to have your python program ask if the user would like to make another calculation?". September 15
# I asked chat gpt "What is the formula to find the rc time constant of a circuit?"
# as well as "How to put a rc time constant into a python program" September 18

# Function to calculate total resistance in series
def total_resistance_series(resistors):
    total_resistance = sum(resistors)
    return total_resistance

# Function to calculate total resistance in parallel
def total_resistance_parallel(resistors):
    total_resistance = 1 / sum(1 / r for r in resistors)
    return total_resistance

# Function to calculate resonant frequency, bandwidth, and Q factor
def resonance_calculation_units(inductance, capacitance, resistance):
    
    # Calculation for finding the resonant frequency
    # Converting from miliHenries to Heneries and from microFarads to Farards
    resonant_frequency_equation = 1 / (2 * 3.14159265359 * (inductance / 1000) * (capacitance / 10000))
  
    # Calculation for finding the bandwidth
    # Converting from microFarads to Farads
    bandwidth = 1 / (resistance * (capacitance / 10000))
    
    # Calculation for finding the Q factor to find the ratio
    qfactor = resonant_frequency_equation / bandwidth
    return resonant_frequency_equation, bandwidth, qfactor

# Function to calculate RC time constant
def rc_time_constant_calculation(resistance, capacitance):
    rc_time_constant = resistance * capacitance / 1000000  # Convert capacitance from uF to F
    return rc_time_constant


while True:
    user_input = input("Press 'q' or 'Q' to quit. Do you want to calculate resistance in series, parallel, resonance, or RC time constant? (Enter 'series', 'parallel', 'resonance' or 'rc'): ").lower()

    # Check if the user wants to quit
    if user_input == 'q':
        break
    
    # Checking if the user's choice is valid
    if user_input not in ['series', 'parallel', 'resonance', 'rc']:
        print("Invalid choice. Please enter 'series', 'parallel', 'resonance' or 'rc'")
        continue
    

    # If the choice is not 'resonance' or 'rc', perform resistance calculations
    if user_input != 'resonance' and user_input != 'rc':
        num_resistors = int(input("How many resistors are there? "))
        resistors = []

        # Loop to input resistance values for each resistor
        for i in range(num_resistors):
            resistance = float(input(f"Enter resistance value for resistor {i + 1} in ohms: "))
            resistors.append(resistance)

        # Calculating and displaying total resistance based on the user's choice
        if user_input == 'series':
            total_resistance = total_resistance_series(resistors)
            print(f"Total Resistance in Series: {total_resistance:.3f} ohms")
        else:
            total_resistance = total_resistance_parallel(resistors)
            print(f"Total Resistance in Parallel: {total_resistance:.3f} ohms")
    
    elif user_input == 'rc':
        resistance = float(input("What is the resistance in ohms? "))
        while resistance <= 0.0:
            resistance = float(input("The value must be greater than zero\nWhat is the resistance in ohms? "))
            
        capacitance = float(input("What is the capacitance in uF? "))
        while capacitance <= 0.0:
            capacitance = float(input("The value must be greater than zero\nWhat is the capacitance in uF? "))
        
        rc_time_constant = rc_time_constant_calculation(resistance, capacitance)
        print(f"RC Time Constant: {rc_time_constant:.3f} seconds")

    else:
        # If the choice is 'resonance', ask for inductance, capacitance, and resistance values
        inductance = float(input("What is the inductance in mH? "))
        while inductance <= 0.0:
            inductance = float(input("The value must be greater than zero\nWhat is the inductance in mH? "))

        capacitance = float(input("What is the capacitance in uF? "))
        while capacitance <= 0.0:
            capacitance = float(input("The value must be greater than zero\nWhat is the capacitance in uF? "))

        resistance = float(input("What is the resistance in ohms? "))
        while resistance <= 0.0:
            resistance = float(input("The value must be greater than zero\nWhat is the resistance in ohms? "))

        resonant_frequency_equation, bandwidth, qfactor = resonance_calculation_units(inductance, capacitance, resistance)
        
        # Calculations for resonant frequency, bandwidth and q factor and printing the answers for the user
        print(f"Resonant Frequency (f_r): {resonant_frequency_equation:.3f} Hz")
        print(f"Bandwidth (BW): {qfactor:.3f} Hz")
        print(f"Q Factor (Q): {bandwidth:.3f}\n")

    # Asking the user if they want to perform another calculation or quit the program
    another_calculation = input("Do you want to perform another calculation? (yes/no): ").lower()
    if another_calculation != 'yes':
        break