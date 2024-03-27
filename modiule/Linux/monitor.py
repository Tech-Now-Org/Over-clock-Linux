import subprocess

def set_refresh_rate(refresh_rate):
    try:
        # Command to set refresh rate using xrandr
        command = f"xrandr --output <your_monitor_name> --mode 1920x1080 --rate {refresh_rate}"

        # Execute command
        subprocess.run(command, shell=True, check=True)

        print(f"Refresh rate set to {refresh_rate} Hz successfully!")
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")

# Example : Set refresh rate to 144 Hz
refresh_rate = 144
set_refresh_rate(refresh_rate)
