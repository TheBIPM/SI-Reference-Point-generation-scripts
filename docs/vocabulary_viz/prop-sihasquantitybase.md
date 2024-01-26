_Vocabulary: [http://si-digital-framework.org/SI#](index.md)_

---








## Property si:hasQuantityBase


#### Tree


* [si:hasBase](prop-sihasbase.md)

    * si:hasQuantityBase





*NOTE* this is a leaf node.


#### URI
http://si-digital-framework.org/SI#hasQuantityBase

#### Description
<p>QuantityBase ^ NumericExponent</p>


#### Inherits from (1)

- [si:hasBase](prop-sihasbase.md)




#### Usage


[si:QuantityPower](class-siquantitypower.md)
=&gt;&nbsp;_si:hasQuantityBase_&nbsp;=&gt;&nbsp;[si:MeasurementUnit](class-simeasurementunit.md)

#### Implementation
```rdf
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix si: <http://si-digital-framework.org/SI#> .

si:hasQuantityBase a owl:ObjectProperty ;
    rdfs:label "has quantity base"@en,
        "a pour base cette quantité"@fr ;
    rdfs:comment "QuantityBase ^ NumericExponent" ;
    rdfs:domain si:QuantityPower ;
    rdfs:range si:MeasurementUnit ;
    rdfs:subPropertyOf si:hasBase .


```









---

_Documentation automatically generated on Fri, 26 Jan 2024 15:50:19 with [Ontospy](http://lambdamusic.github.io/Ontospy/ "Open") (v2.1.1)_