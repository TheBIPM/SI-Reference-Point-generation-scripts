# Please activate your dedicated Python-environment before executing this script

Set-Variable -Name "PYTHONPATH" -Value "."

# currently all files are generated into "./Testing/API/"

echo "generating si.ttl + quantities.ttl"
python ./CUQ/Python/Quantities_ABox.py
echo "Done.`n"

echo "generating units.ttl"
python ./CUQ/Python/Units_ABox.py
echo "Done.`n"

echo "generating constants.ttl"
python ./CUQ/Python/Constants_ABox.py
echo "Done.`n"

#echo "generating bodies.ttl"
python ./ResBod/Python/ResBod_TBox.py
echo "Done.`n"

echo "generating cgpm.ttl"
python ./ResBod/Python/ResBod_ABox_CGPM.py
echo "Done.`n"

echo "generating cipm.ttl"
python ./ResBod/Python/ResBod_ABox_CIPM.py
echo "Done.`n"
