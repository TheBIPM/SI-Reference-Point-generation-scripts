_Vocabulary: [http://si-digital-framework.org/SI#](index.md)_

---





    


## Class si:SIPrefix


#### Tree

* owl:Thing
    * si:SIPrefix





*NOTE* this is a leaf node.


#### URI
http://si-digital-framework.org/SI#SIPrefix

#### Description
<p>The class for SI Prefixes.</p>



#### Inherits from:
owl:Thing






#### Implementation
```rdf
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix si: <http://si-digital-framework.org/SI#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

si:SIPrefix a owl:Class ;
    rdfs:label "SI prefix"@en,
        "préfixe SI"@fr ;
    rdfs:comment "The class for SI Prefixes."@en,
        "La classe pour les préfixes SI."@fr ;
    rdfs:subClassOf [ a owl:Restriction ;
            owl:minCardinality "1"^^xsd:int ;
            owl:onProperty si:hasScalingFactor ] .


```




#### Instances of si:SIPrefix can have the following properties:

##### From [si:SIPrefix](class-sisiprefix.md):

| Property | Description | Expected Type |
|----------|-------------|---------------|
| [si:hasScalingFactor](prop-sihasscalingfactor.md) | Linking an SI prefix to its scaling factor. |[rdfs:Literal](class-rdfsliteral.md)|


##### From [owl:Thing](class-owlthing.md):

| Property | Description | Expected Type |
|----------|-------------|---------------|
| [si:hasBase](prop-sihasbase.md) | Base ^ NumericExponent |*owl:Thing*|
| [si:hasQuantityTerm](prop-sihasquantityterm.md) |  |*owl:Thing*|
| [si:hasSymbol](prop-sihassymbol.md) | Linking a measurement unit or prefix to a symbol. |[xsd:string](class-xsdstring.md)|
| [si:hasTerm](prop-sihasterm.md) |  |*owl:Thing*|
| [si:hasUnit](prop-sihasunit.md) | Linking a measurement unit to an object. |[si:MeasurementUnit](class-simeasurementunit.md)|
| [si:hasUnitTerm](prop-sihasunitterm.md) |  |*owl:Thing*|
| [si:inBaseSIUnits](prop-siinbasesiunits.md) |  |[si:MeasurementUnit](class-simeasurementunit.md)|
| [si:inOtherSIUnits](prop-siinothersiunits.md) |  |[si:MeasurementUnit](class-simeasurementunit.md)|











---

_Documentation automatically generated on Fri, 26 Jan 2024 15:50:19 with [Ontospy](http://lambdamusic.github.io/Ontospy/ "Open") (v2.1.1)_