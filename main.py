# Create a function that will calculate the number of steps that you
# make for a certain distance.


def calculate_steps(distance_m, step_length_m):
    steps = int(distance_m/step_length_m)
    print("Number of steps: {0}".format(steps))


distance_m = int(input("Enter a distance in meters: "))
step_length_m = int(input("Enter a length of you step: "))

calculate_steps(distance_m, step_length_m)