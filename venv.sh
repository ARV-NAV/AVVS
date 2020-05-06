#!/bin/bash

virtualenv venv

venv_dir=$(pwd)/venv

if [ -d "$venv_dir/bin" ]; then
  source venv/bin/activate
else
  source venv/Scripts/activate
fi

pip3 install --upgrade pip
pip install -r requirments.txt

matlab_root_dir=/c/Program\ Files/MATLAB/R2019b
matlab_python_dir=$matlab_root_dir/extern/engines/python
absolute_path_to_venv="C:\Users\Legol\google_drive\CS\CS46X\AVVS\venv"

cd "$matlab_python_dir"
python setup.py install --prefix="$absolute_path_to_venv"
cd -

deactivate
