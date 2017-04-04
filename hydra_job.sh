#!/bin/bash -l
# number of nodes and cores (change this when using more workers) 
#PBS -l nodes=1:ppn=4
# memory requirements
#PBS -l mem=2gb
# max run time
#PBS -l walltime=00:05:00
# output and error files
#PBS -o a3c.out
#PBS -e a3c.err
#PBS -N a3c
#PBS -V

module add openblas
cd $HOME
source .bashrc
source activate a3c
cd universe-starter-agent
python train.py --num-workers 2 --env-id PongDeterministic-v3 --mode child --log-dir $WORKDIR/pong

#wait for child processes
wait
