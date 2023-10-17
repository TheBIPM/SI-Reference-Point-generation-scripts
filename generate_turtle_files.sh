#!/bin/bash

# Please activate your dedicated Python-environment before executing this script
export PYTHONPATH=$(pwd)

# currently all files are generated into "./Testing/API/"
echo "generating si.ttl"
python ./CUQ/Python/CUQ_TBox.py
echo -e "Done.\n"

echo "generating quantities.ttl"
python ./CUQ/Python/Quantities_ABox.py
echo -e "Done.\n"

echo "generating units.ttl"
python ./CUQ/Python/Units_Abox.py
echo -e "Done.\n"

echo "generating constants.ttl"
python ./CUQ/Python/Constants_ABox.py
echo -e "Done.\n"

echo "generating prefixes.ttl"
python ./CUQ/Python/Prefixes_ABox.py
echo -e "Done.\n"

echo "generating decisions.ttl"
python ./CUQ/Python/generate_decisions_turtle.py
echo -e "Done.\n"

echo "generating bodies.ttl"
python ./ResBod/Python/ResBod_TBox.py
echo -e "Done.\n"

echo "generating cgpm.ttl"
python ./ResBod/Python/ResBod_ABox_CGPM.py
echo -e "Done.\n"

echo "generating cipm.ttl"
python ./ResBod/Python/ResBod_ABox_CIPM.py
echo -e "Done.\n"

echo "generating cctf.ttl"
python ./ResBod/Python/ResBod_ABox_CCTF.py
echo -e "Done.\n"

# compress into archive
export git_hash=$(git log --pretty=format:'%h' -n 1)
zip -j si-app-turtle-$git_hash.zip Testing/API/*.ttl