#!/bin/bash

#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1
#SBATCH --mem=16G
module load conda/latest
conda activate HeRM
./analyzing_big_sweep.py