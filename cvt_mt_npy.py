import h5py
import numpy as np

# Load MATLAB v7.3 file
mat_path = "tc165.mat"
with h5py.File(mat_path, 'r') as f:
    tc = np.array(f['tc'])  # load dataset

# Check original shape
print("Original shape:", tc.shape)

# Transpose to match (ROIs, timepoints)
tc_npy = tc.T

print("Converted shape:", tc_npy.shape)

# Save as .npy
np.save("tc165.npy", tc_npy)

print("Saved as tc154.npy")