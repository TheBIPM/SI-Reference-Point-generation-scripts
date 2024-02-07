_Vocabulary: [http://si-digital-framework.org/SI#](index.md)_

---





    


## Class si:DefinitionNote


#### Tree

* owl:Thing
    * si:DefinitionNote





*NOTE* this is a leaf node.


#### URI
http://si-digital-framework.org/SI#DefinitionNote

#### Description
<p>The class for notes related SI unit definitions.</p>



#### Inherits from:
owl:Thing






#### Implementation
```rdf
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix si: <http://si-digital-framework.org/SI#> .

si:DefinitionNote a owl:Class ;
    rdfs:label "unit definition note"@en,
        "note de définition d'unité"@fr ;
    rdfs:comment "The class for notes related SI unit definitions."@en,
        "La classe pour les définitions d'unités SI liées aux notes."@fr .


```




#### Instances of si:DefinitionNote can have the following properties:

##### From [si:DefinitionNote](class-sidefinitionnote.md):

| Property | Description | Expected Type |
|----------|-------------|---------------|
| [si:hasNoteIndex](prop-sihasnoteindex.md) | The text of a definition note. |[rdfs:Literal](class-rdfsliteral.md)|
| [si:hasNoteText](prop-sihasnotetext.md) | The order index of a definition note. |[rdfs:Literal](class-rdfsliteral.md)|


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