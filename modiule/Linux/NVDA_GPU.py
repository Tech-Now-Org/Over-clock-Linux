import subprocess

def set_nvidia_gpu_overclock(core_offset_percent, memory_offset_percent):
    try:
        # Command to set core clock and memory clock offsets
        command = f"nvidia-settings -a '[gpu:0]/GPUGraphicsClockOffset[3]={core_offset_percent}%' " \
                  f"-a '[gpu:0]/GPUMemoryTransferRateOffset[3]={memory_offset_percent}%'"

        # Execute command 
        subprocess.run(command, shell=True, check=True)

        print("NVIDIA GPU overclocking successful!")
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")



# Example : Set core clock offset : +10% , memory clock offset : +20% 
nvidia_core_offset_percent = 10
nvidia_memory_offset_percent = 20
set_nvidia_gpu_overclock(nvidia_core_offset_percent, nvidia_memory_offset_percent)

