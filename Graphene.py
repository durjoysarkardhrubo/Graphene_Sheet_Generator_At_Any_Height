import numpy as np

def generate_graphene_unit_cell(a, b, c, alpha, beta, gamma):
    # Convert angles from degrees to radians
    alpha = np.radians(alpha)
    beta = np.radians(beta)
    gamma = np.radians(gamma)

    v1 = [a, 0, 0]
    v2 = [b * np.cos(gamma), b * np.sin(gamma), 0]
    v3 = [c * np.cos(beta), c * (np.cos(alpha) - np.cos(beta) * np.cos(gamma)) / np.sin(gamma), c * np.sqrt(1 - np.cos(beta)**2 - ((np.cos(alpha) - np.cos(beta) * np.cos(gamma)) / np.sin(gamma))**2)]
    
    basis_atoms = np.array([
        [0, 0, 0],
        [1/3, 2/3, 0]
    ])
    
    return np.array([v1, v2, v3]), basis_atoms

def generate_graphene_supercell(a, b, c, alpha, beta, gamma, nx, ny, z_height):
    lattice_vectors, basis_atoms = generate_graphene_unit_cell(a, b, c, alpha, beta, gamma)
    
    atom_positions = []
    for i in range(nx):
        for j in range(ny):
            for atom in basis_atoms:
                position = i * lattice_vectors[0] + j * lattice_vectors[1] + [0, 0, z_height] + atom
                atom_positions.append(position)
    
    return np.array(atom_positions)

def save_atom_positions(atom_positions, filename):
    with open(filename, 'w') as f:
        for pos in atom_positions:
            f.write(f'{pos[0]:.6f} {pos[1]:.6f} {pos[2]:.6f}\n')

a = 2.46
b = 2.46
c = 10.0
alpha = 90
beta = 90
gamma = 120

nx = int(input("Enter the size of the supercell in the x direction: "))
ny = int(input("Enter the size of the supercell in the y direction: "))
z_height = float(input("Enter the z-height for the graphene sheet: "))

atom_positions = generate_graphene_supercell(a, b, c, alpha, beta, gamma, nx, ny, z_height)

# Save
save_atom_positions(atom_positions, 'graphene_supercell.txt')

print(f"Graphene supercell with size {nx}x{ny}x1 at z-height {z_height} has been generated and saved to 'graphene_supercell.txt'.")
