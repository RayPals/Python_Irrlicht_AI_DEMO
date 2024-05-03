from ctypes import c_int, c_uint, c_bool, c_void_p, byref, POINTER, Structure, cdll
import ctypes.util

# Define the dimension2d_u32 structure
class dimension2d_u32(Structure):
    _fields_ = [("Width", c_uint), ("Height", c_uint)]

# Load the Irrlicht library
irrlicht = cdll.LoadLibrary(r'C:\<PATH_TO_IRRLICHT>\Irrlicht.dll')

# Define the EID_D3D9 constant
EID_D3D9 = 1

# Create the device
print("Creating device...")
windowSize = dimension2d_u32(800, 600)
device = irrlicht.createDevice(
    EID_D3D9,  # deviceType
    byref(windowSize),  # windowSize
    32,  # bits
    False,  # fullscreen
    False,  # stencilbuffer
    True,  # vsync
    None  # receiver
)
print("Device creation result:", device)

# Check if the device was created successfully
if device:
    print("Device created successfully!")
else:
    print("Failed to create device.")

while True:
    pass