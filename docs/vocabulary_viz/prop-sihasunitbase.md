_Vocabulary: [http://si-digital-framework.org/SI#](index.md)_

---








## Property si:hasUnitBase


#### Tree


* [si:hasBase](prop-sihasbase.md)

    * si:hasUnitBase





*NOTE* this is a leaf node.


#### URI
http://si-digital-framework.org/SI#hasUnitBase

#### Description
<p>UnitBase ^ NumericExponent</p>


#### Inherits from (1)

- [si:hasBase](prop-sihasbase.md)




#### Usage
owl:Thing=&gt;&nbsp;_si:hasUnitBase_&nbsp;=&gt;&nbsp;owl:Thing

#### Implementation
```rdf
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix si: <http://si-digital-framework.org/SI#> .

si:hasUnitBase a owl:ObjectProperty ;
    rdfs:label "has unit base" ;
    rdfs:comment "UnitBase ^ NumericExponent" ;
    rdfs:subPropertyOf si:hasBase .


```









---

_Documentation automatically generated on Wed, 24 Jan 2024 16:24:45 with [Ontospy](http://lambdamusic.github.io/Ontospy/ "Open") (v2.1.1)_