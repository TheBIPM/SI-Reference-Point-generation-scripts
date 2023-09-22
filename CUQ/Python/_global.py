from CUQ_TBox import SiElements

PDF = SiElements()

print("Run all A boxes")
print("===============")
print()
print()
print("Start Quantities")
exec(open(str(PDF.BASE_PATH) + "/Python/Quantities_ABox.py").read())
print("End Quantities")
print()
print("Start Units")
exec(open(str(PDF.BASE_PATH) + "/Python/Units_ABox.py").read())
print("End Units")
print()
### needs to be executed AFTER Units_ABox because it uses information of it
print("Start Constants")
exec(open(str(PDF.BASE_PATH) + "/Python/Constants_ABox.py").read())
print("End Constants")