_Vocabulary: [http://si-digital-framework.org/SI#](index.md)_

---








## Property si:hasUnitTerm


#### Tree


* [si:hasTerm](prop-sihasterm.md)

    * si:hasUnitTerm


        * [si:hasLeftUnitTerm](prop-sihasleftunitterm.md)

        * [si:hasRightUnitTerm](prop-sihasrightunitterm.md)
        






#### URI
http://si-digital-framework.org/SI#hasUnitTerm

#### Description



#### Inherits from (1)

- [si:hasTerm](prop-sihasterm.md)




#### Usage
owl:Thing=&gt;&nbsp;_si:hasUnitTerm_&nbsp;=&gt;&nbsp;owl:Thing

#### Implementation
```rdf
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix si: <http://si-digital-framework.org/SI#> .

si:hasUnitTerm a owl:ObjectProperty ;
    rdfs:label "has unit term"@en,
        "a cette unité pour terme"@fr ;
    rdfs:subPropertyOf si:hasTerm .


```









---

_Documentation automatically generated on Fri, 26 Jan 2024 15:50:19 with [Ontospy](http://lambdamusic.github.io/Ontospy/ "Open") (v2.1.1)_