import pycpufreq

def overclock_cpu(overclock_percentage):
    cpu_freq = pycpufreq.CPUFreq()
    available_freqs = cpu_freq.get_available_frequencies()
    
    if available_freqs:
        max_freq = max(available_freqs)
        print("Current available frequencies:", available_freqs)
        print("Max frequency before overclocking:", max_freq)
        
        overclocked_freq = max_freq * (1 + overclock_percentage / 100)  # Increase frequency by specified percentage
        cpu_freq.set_frequency(int(overclocked_freq))
        
        print("CPU overclocked to:", overclocked_freq)
    else:
        print("No available frequencies found.")

if __name__ == "__main__":
    overclock_percentage = 10  # Change this to the desired overclock percentage
    overclock_cpu(overclock_percentage)
