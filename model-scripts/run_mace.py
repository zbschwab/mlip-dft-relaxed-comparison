"""
run_mace.py — run in mlip-mace environment
conda activate mlip-mace
"""

import sys
from ase.io import read
from ase.optimize import BFGS
from mace.calculators import mace_mp

# print("hello from mace!")  # check connection

# argv[1]: path to dft run POSCAR
# argv[2]: path to write mlip run to

ads_slab = read(sys.argv[1], format="vasp")

# set MACE to run on mps instead of cpu 
# (change depending on your particular gpu predicament)
calc = mace_mp(model="medium", dispersion=False, default_dtype="float32")
calc.models = [m.float().to("mps") for m in calc.models]
calc.device = "mps"

ads_slab.calc = calc

opt = BFGS(ads_slab, trajectory=sys.argv[2])
opt.run(fmax=0.05)  # converge forces to 0.05 eV/Å
