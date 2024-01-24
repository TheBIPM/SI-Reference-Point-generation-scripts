_Vocabulary: [http://si-digital-framework.org/SI#](index.md)_

---








## Property si:hasBase


#### Tree

* rdf:Property
    * si:hasBase


        * [si:hasQuantityBase](prop-sihasquantitybase.md)

        * [si:hasUnitBase](prop-sihasunitbase.md)
        






#### URI
http://si-digital-framework.org/SI#hasBase

#### Description
<p>Base ^ NumericExponent</p>


#### Inherits from:
owl:Thing



#### Usage
owl:Thing=&gt;&nbsp;_si:hasBase_&nbsp;=&gt;&nbsp;owl:Thing

#### Implementation
```rdf
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix si: <http://si-digital-framework.org/SI#> .

si:hasBase a owl:ObjectProperty ;
    rdfs:label "has base" ;
    rdfs:comment "Base ^ NumericExponent" .


```









---

_Documentation automatically generated on Wed, 24 Jan 2024 16:24:45 with [Ontospy](http://lambdamusic.github.io/Ontospy/ "Open") (v2.1.1)_