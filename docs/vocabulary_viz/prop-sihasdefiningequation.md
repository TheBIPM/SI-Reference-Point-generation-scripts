_Vocabulary: [http://si-digital-framework.org/SI#](index.md)_

---








## Property si:hasDefiningEquation


#### Tree

* rdf:Property
    * si:hasDefiningEquation





*NOTE* this is a leaf node.


#### URI
http://si-digital-framework.org/SI#hasDefiningEquation

#### Description
<p>Linking a SI definition to its defining equation.</p>


#### Inherits from:
owl:Thing



#### Usage


[n0fe14176d0b84ad0ae63b0a583714332b4](entity-n0fe14176d0b84ad0ae63b0a583714332b4.md)
=&gt;&nbsp;_si:hasDefiningEquation_&nbsp;=&gt;&nbsp;[rdfs:Literal](class-rdfsliteral.md)

#### Implementation
```rdf
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix si: <http://si-digital-framework.org/SI#> .

si:hasDefiningEquation a owl:DatatypeProperty ;
    rdfs:label "has defining equation"@en,
        "a une équation de définition"@fr ;
    rdfs:comment "Linking a SI definition to its defining equation."@en,
        "Associer une définition SI à son équation de définition."@fr ;
    rdfs:domain [ owl:oneOf ( si:Definition si:Constant ) ] ;
    rdfs:range rdfs:Literal .


```









---

_Documentation automatically generated on Fri, 26 Jan 2024 15:50:19 with [Ontospy](http://lambdamusic.github.io/Ontospy/ "Open") (v2.1.1)_