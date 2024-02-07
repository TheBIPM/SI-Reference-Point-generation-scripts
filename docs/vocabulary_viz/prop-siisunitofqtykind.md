_Vocabulary: [http://si-digital-framework.org/SI#](index.md)_

---








## Property si:isUnitOfQtyKind


#### Tree

* rdf:Property
    * si:isUnitOfQtyKind





*NOTE* this is a leaf node.


#### URI
http://si-digital-framework.org/SI#isUnitOfQtyKind

#### Description
<p>Linking a measurement unit to its quantity kind.</p>


#### Inherits from:
owl:Thing



#### Usage


[si:MeasurementUnit](class-simeasurementunit.md)
=&gt;&nbsp;_si:isUnitOfQtyKind_&nbsp;=&gt;&nbsp;[si:QuantityKind](class-siquantitykind.md)

#### Implementation
```rdf
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix si: <http://si-digital-framework.org/SI#> .

si:isUnitOfQtyKind a owl:ObjectProperty ;
    rdfs:label "is unit of quantity kind"@en,
        "est une unité de quantité"@fr ;
    rdfs:comment "Linking a measurement unit to its quantity kind."@en,
        "Associer une unité de mesure à son type de quantité."@fr ;
    rdfs:domain si:MeasurementUnit ;
    rdfs:range si:QuantityKind .


```









---

_Documentation automatically generated on Wed, 07 Feb 2024 16:02:36 with [Ontospy](http://lambdamusic.github.io/Ontospy/ "Open") (v2.1.1)_