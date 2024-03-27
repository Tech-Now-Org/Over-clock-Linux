import subprocess

def set_amd_gpu_overclock(core_offset_percent, memory_offset_percent):
    try:
        # Command set core clock and memory clock offsets
        command = f"sudo amdconfig --odsc={core_offset_percent},{memory_offset_percent}"

        # Execute  Command
        subprocess.run(command, shell=True, check=True)

        print("AMD GPU overclocking successful!")
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")

# Example : Set core clock offset to : +5% , memory clock offset to : +10% 
amd_core_offset_percent = 5
amd_memory_offset_percent = 10
set_amd_gpu_overclock(amd_core_offset_percent, amd_memory_offset_percent)
