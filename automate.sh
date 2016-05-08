#!/bin/bash 
#SBATCH --job-name=7system.sel_rmsd
#SBATCH --output=7system.sel_rmsd.output 
#SBATCH --time=96:00:00 
#SBATCH --nodes=1
#SBATCH --exclusive 

export LD_LIBRARY_PATH="$LD_LIBRARY_PATH:/software/usr/gcc-4.9.2/lib64"
export LD_LIBRARY_PATH="$LD_LIBRARY_PATH:/software/usr/hpcx-v1.2.0-292-gcc-MLNX_OFED_LINUX-2.4-1.0.0-redhat6.6/ompi-mellanox-v1.8/lib"

export PYTHON_EGG_CACHE="./"

time ./RMSD_analysis.py ../../../../../ ../../../../../ 0 &

time ./RMSD_analysis.py ../../../../../ ../../../../../ 1 &

time ./RMSD_analysis.py ../../../../../ ../../../../../ 2 &

time ./RMSD_analysis.py ../../../../../ ../../../../../ 3 &

time ./RMSD_analysis.py ../../../../../ ../../../../../ 4 &

time ./RMSD_analysis.py ../../../../../ ../../../../../ 5 &

time ./RMSD_analysis.py ../../../../../ ../../../../../ 6 &

wait

