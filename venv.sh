#!/bin/bash

# Set python and pip to be the python 3 command for the system
python=python3
pip=pip3

$pip install virtualenv

virtualenv venv

venv_dir=$(pwd)/venv

if [ -d "$venv_dir/bin" ]; then
  source venv/bin/activate
else
  source venv/Scripts/activate
fi

$python -m $pip install --upgrade pip
$python -m pip install -r requirements.txt

# Set the matlab_root_dir to the root directory of the system's Matlab installation
matlab_root_dir=/usr/local/MATLAB/R2018b
matlab_python_dir=$matlab_root_dir/extern/engines/python

# Set the absolute_path_to_venv to the absolute path to the (to be) venv directory
absolute_path_to_venv="/home/max/temp/AVVS/venv"

cd "$matlab_python_dir"
$python setup.py install --prefix="$absolute_path_to_venv"
cd -

deactivate
