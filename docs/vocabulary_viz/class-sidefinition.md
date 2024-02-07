_Vocabulary: [http://si-digital-framework.org/SI#](index.md)_

---





    


## Class si:Definition


#### Tree

* owl:Thing
    * si:Definition





*NOTE* this is a leaf node.


#### URI
http://si-digital-framework.org/SI#Definition

#### Description
<p>The class for definitions of an SI base unit.</p>



#### Inherits from:
owl:Thing






#### Implementation
```rdf
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix si: <http://si-digital-framework.org/SI#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

si:Definition a owl:Class ;
    rdfs:label "definition of a base unit"@en,
        "définition d'une unité de base"@fr ;
    rdfs:comment "The class for definitions of an SI base unit."@en,
        "La classe pour les notes sur les définitions des unités SI."@fr ;
    rdfs:subClassOf [ a owl:Restriction ;
            owl:minCardinality "1"^^xsd:int ;
            owl:onProperty si:hasStartValidity ] .


```




#### Instances of si:Definition can have the following properties:

##### From [si:Definition](class-sidefinition.md):

| Property | Description | Expected Type |
|----------|-------------|---------------|
| [si:hasDefiningText](prop-sihasdefiningtext.md) | Linking an SI definition to the defining text. |[rdfs:Literal](class-rdfsliteral.md)|
| [si:hasEndValidity](prop-sihasendvalidity.md) | Linking an SI definition to its ending validity date. |[xsd:date](class-xsddate.md)|
| [si:hasStartValidity](prop-sihasstartvalidity.md) | Linking an SI definition to its starting validity date. |[xsd:date](class-xsddate.md)|
| [si:hasStatus](prop-sihasstatus.md) | Linking a SI definition to its status. |[rdfs:Literal](class-rdfsliteral.md)|
| [si:hasDefiningConstant](prop-sihasdefiningconstant.md) | Linking a definition to its defining constant. |[si:Constant](class-siconstant.md)|
| [si:hasDefinitionNote](prop-sihasdefinitionnote.md) | Linking an SI definition to a definition note. |[si:DefinitionNote](class-sidefinitionnote.md)|
| [si:hasNextDefinition](prop-sihasnextdefinition.md) | Linking an SI definition version to the next version. |[si:Definition](class-sidefinition.md)|
| [si:hasPreviousDefinition](prop-sihaspreviousdefinition.md) | Linking an SI definition version to the previous version. |[si:Definition](class-sidefinition.md)|


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