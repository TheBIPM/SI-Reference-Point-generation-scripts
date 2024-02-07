_Vocabulary: [http://si-digital-framework.org/SI#](index.md)_

---





    


## Class si:SIDecisionTarget


#### Tree

* owl:Thing
    * si:SIDecisionTarget





*NOTE* this is a leaf node.


#### URI
http://si-digital-framework.org/SI#SIDecisionTarget

#### Description
<p>The class for SI decisions target.</p>



#### Inherits from:
owl:Thing






#### Implementation
```rdf
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix si: <http://si-digital-framework.org/SI#> .

si:SIDecisionTarget a owl:Class ;
    rdfs:label "SI Decision target"@en,
        "Cible d'une décision SI"@fr ;
    rdfs:comment "The class for SI decisions target."@en,
        "La classe pour les cibles de décisions SI."@fr .


```




#### Instances of si:SIDecisionTarget can have the following properties:

##### From [si:SIDecisionTarget](class-sisidecisiontarget.md):

| Property | Description | Expected Type |
|----------|-------------|---------------|
| [si:hasDecision](prop-sihasdecision.md) |  |[si:SIDecision](class-sisidecision.md)|


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