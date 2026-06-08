"""
run_mattersim.py — run in mlip-mattersim environment
conda activate mlip-mattersim
"""

import sys
from ase.io import read
from ase.optimize import BFGS
from mattersim.forcefield import MatterSimCalculator

# print("hello from mattersim!")  # check connection

# argv[1]: path to dft run POSCAR
# argv[2]: path to write mlip run to

ads_slab = read(sys.argv[1], format="vasp")

calc = MatterSimCalculator()

ads_slab.calc = calc  # no mps option, runs on cpu

opt = BFGS(ads_slab, trajectory=sys.argv[2])
opt.run(fmax=0.05)  # converge forces to 0.05 eV/Å
