def main():
    mass = int(input("Mass: "))
    energy = calculate_energy(mass)
    print(f"E: {energy}")

def calculate_energy(mass):
    c = 300000000
    return mass * c ** 2

main()
