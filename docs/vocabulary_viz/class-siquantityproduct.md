_Vocabulary: [http://si-digital-framework.org/SI#](index.md)_

---





    


## Class si:QuantityProduct


#### Tree

* owl:Thing
    * si:QuantityProduct





*NOTE* this is a leaf node.


#### URI
http://si-digital-framework.org/SI#QuantityProduct

#### Description




#### Inherits from:
owl:Thing






#### Implementation
```rdf
None
```




#### Instances of si:QuantityProduct can have the following properties:

##### From [si:QuantityProduct](class-siquantityproduct.md):

| Property | Description | Expected Type |
|----------|-------------|---------------|
| [si:hasLeftQuantityTerm](prop-sihasleftquantityterm.md) | preserve order of multiplication |[si:QuantityKind](class-siquantitykind.md)|
| [si:hasRightQuantityTerm](prop-sihasrightquantityterm.md) | preserve order of multiplication |[si:QuantityKind](class-siquantitykind.md)|


##### From [owl:Thing](class-owlthing.md):

| Property | Description | Expected Type |
|----------|-------------|---------------|
| [si:hasBase](prop-sihasbase.md) | Base ^ NumericExponent |*owl:Thing*|
| [si:hasQuantityTerm](prop-sihasquantityterm.md) |  |*owl:Thing*|
| [si:hasSymbol](prop-sihassymbol.md) | Linking a measurement unit or prefix to a symbol. |[xsd:string](class-xsdstring.md)|
| [si:hasTerm](prop-sihasterm.md) |  |*owl:Thing*|
| [si:hasUnitTerm](prop-sihasunitterm.md) |  |*owl:Thing*|
| [si:inBaseSIUnits](prop-siinbasesiunits.md) |  |[si:MeasurementUnit](class-simeasurementunit.md)|
| [si:inOtherSIUnits](prop-siinothersiunits.md) |  |[si:MeasurementUnit](class-simeasurementunit.md)|











---

_Documentation automatically generated on Wed, 07 Feb 2024 16:02:36 with [Ontospy](http://lambdamusic.github.io/Ontospy/ "Open") (v2.1.1)_