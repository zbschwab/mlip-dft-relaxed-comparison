"""
run_uma.py — run in mlip-uma environment
conda activate mlip-uma
"""

import sys
from ase.io import read
from ase.optimize import BFGS
from fairchem.core import pretrained_mlip, FAIRChemCalculator

# print("hello from uma!")  # check connection

# argv[1]: path to dft run POSCAR
# argv[2]: path to write mlip run to

ads_slab = read(sys.argv[1], format="vasp")

# (change depending on your particular gpu predicament)
predictor = pretrained_mlip.get_predict_unit("uma-s-1p2", device="cpu")

calc = FAIRChemCalculator(predictor, task_name="oc20", seed=None)
ads_slab.calc = calc

opt = BFGS(ads_slab, trajectory=sys.argv[2])
opt.run(fmax=0.05)  # converge forces to 0.05 eV/Å
