_Vocabulary: [http://si-digital-framework.org/SI#](index.md)_

---








## Property si:hasFactor


#### Tree

* rdf:Property
    * si:hasFactor


        * [si:hasNumericFactor](prop-sihasnumericfactor.md)

        * [si:hasQuantityFactor](prop-sihasquantityfactor.md)

        * [si:hasUnitFactor](prop-sihasunitfactor.md)
        






#### URI
http://si-digital-framework.org/SI#hasFactor

#### Description



#### Inherits from:
owl:Thing



#### Usage
owl:Thing=&gt;&nbsp;_si:hasFactor_&nbsp;=&gt;&nbsp;owl:Thing

#### Implementation
```rdf
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix si: <http://si-digital-framework.org/SI#> .

si:hasFactor a owl:ObjectProperty ;
    rdfs:label "has factor" .


```









---

_Documentation automatically generated on Wed, 24 Jan 2024 16:24:45 with [Ontospy](http://lambdamusic.github.io/Ontospy/ "Open") (v2.1.1)_