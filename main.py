import sounddevice as sd
import numpy as np

device_name = "NVIDIA" #"C24FG70"
sample_rate = 44100
devices = sd.query_devices()

output_device = None
device_id = None

for d_id,device in enumerate(devices):
    if device_name in device['name'] and device['max_output_channels'] > 0 and device['default_samplerate'] == sample_rate:
        output_device = device
        device_id = d_id        
        break

if output_device:
    sd.default.samplerate = sample_rate #44100
    sd.default.device = device_id
    data = np.array([i for i in range(256)]*10,dtype='uint8')
    with sd.OutputStream(samplerate=10000,dtype="uint8") as stream:
        while True:
            stream.write(data)
else:
    print("No device was selected")
