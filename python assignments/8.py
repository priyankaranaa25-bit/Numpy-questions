# List of joint angles
angles = [30, -15, 45, 200, 60, 90]

# Function to check valid angles (0° to 180°)
def is_valid(angle):
    return 0 <= angle <= 180

# Function to convert angle to servo command
def servo_command(angle):
    return angle * 10

# Filter valid angles
valid_angles = list(filter(is_valid, angles))

# Convert valid angles to servo commands
servo_commands = list(map(servo_command, valid_angles))

# Display results
print("Valid Angles:", valid_angles)
print("Servo Commands:", servo_commands)