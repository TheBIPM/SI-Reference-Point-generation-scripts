# Please activate your dedicated Python-environment before executing this script

Set-Variable -Name "PYTHONPATH" -Value "."

# currently all files are generated into "./Testing/API/"
echo "generating si.ttl"
python ./CUQ/Python/CUQ_TBox.py
echo "Done.`n"

echo "generating quantities.ttl"
python ./CUQ/Python/Quantities_ABox.py
echo "Done.`n"

echo "generating units.ttl"
python ./CUQ/Python/Units_Abox.py
echo "Done.`n"

echo "generating constants.ttl"
python ./CUQ/Python/Constants_ABox.py
echo "Done.`n"

echo "generating prefixes.ttl"
python ./CUQ/Python/Prefixes_ABox.py
echo "Done.`n"

echo "generating decisions.ttl"
python ./CUQ/Python/generate_decisions_turtle.py
echo "Done.`n"

echo "generating bodies.ttl"
python ./ResBod/Python/ResBod_TBox.py
echo "Done.`n"

echo "generating cgpm.ttl"
python ./ResBod/Python/ResBod_ABox_CGPM.py
echo "Done.`n"

echo "generating cipm.ttl"
python ./ResBod/Python/ResBod_ABox_CIPM.py
echo "Done.`n"

echo "generating cctf.ttl"
python ./ResBod/Python/ResBod_ABox_CCTF.py
echo "Done.`n"

# compress into archive
$git_hash = git log --pretty=format:'%h' -n 1
Compress-Archive -Path Testing\API\*.ttl -DestinationPath si-app-turtle-$git_hash.zip