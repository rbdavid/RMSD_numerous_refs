#!/bin/bash 
#SBATCH --job-name=7system.rmsd_pca
#SBATCH --output=7system.traj_rmsd_pca.output 
#SBATCH --time=96:00:00 
#SBATCH --nodes=1
#SBATCH --exclusive 

export LD_LIBRARY_PATH="$LD_LIBRARY_PATH:/software/usr/gcc-4.9.2/lib64"
export LD_LIBRARY_PATH="$LD_LIBRARY_PATH:/software/usr/hpcx-v1.2.0-292-gcc-MLNX_OFED_LINUX-2.4-1.0.0-redhat6.6/ompi-mellanox-v1.8/lib"

export PYTHON_EGG_CACHE="./"

#time ./Traj_writing.py ../../../../../AMBER_ssrna_adp_pi/truncated.pdb ../../../../../ 7system_backbone.dcd > traj_writing.output

#time ./RMSD.avg_structures.py ../../../../Avg_structure/ reference_structure.pdb 7system_backbone.dcd > rmsd_calc.output

#time ./PCA.avg_structures.py > pca_calc.output

time ... 1 &

time ... 2 &

time ... 3 &

time ... 4 &

wait



