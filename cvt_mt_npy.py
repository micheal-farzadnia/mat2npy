import h5py
import numpy as np

# N_subjects = 100

for i in range(1,N_subjects):

    # Load MATLAB v7.3 file
    mat_path = f"tc{i:03d}.mat"
    out_path = f"tc{i:03d}.npy"

    with h5py.File(mat_path, 'r') as f:
        tc = np.array(f['tc'])

    print(f"{mat_path} original shape:", tc.shape)

    tc_npy = tc.T

    print(f"{mat_path} converted shape:", tc_npy.shape)

    np.save(out_path, tc_npy)

    print(f"Saved {out_path}")
