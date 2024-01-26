_Vocabulary: [http://si-digital-framework.org/SI#](index.md)_

---








## Property si:hasTerm


#### Tree

* rdf:Property
    * si:hasTerm


        * [si:hasNumericFactor](prop-sihasnumericfactor.md)

        * [si:hasQuantityTerm](prop-sihasquantityterm.md)

        * [si:hasUnitTerm](prop-sihasunitterm.md)
        






#### URI
http://si-digital-framework.org/SI#hasTerm

#### Description



#### Inherits from:
owl:Thing



#### Usage
owl:Thing=&gt;&nbsp;_si:hasTerm_&nbsp;=&gt;&nbsp;owl:Thing

#### Implementation
```rdf
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix si: <http://si-digital-framework.org/SI#> .

si:hasTerm a owl:ObjectProperty ;
    rdfs:label "has a term"@en,
        "a pour terme"@fr .


```









---

_Documentation automatically generated on Fri, 26 Jan 2024 15:50:19 with [Ontospy](http://lambdamusic.github.io/Ontospy/ "Open") (v2.1.1)_