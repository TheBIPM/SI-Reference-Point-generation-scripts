_Vocabulary: [http://si-digital-framework.org/SI#](index.md)_

---








## Property si:hasStatus


#### Tree

* rdf:Property
    * si:hasStatus





*NOTE* this is a leaf node.


#### URI
http://si-digital-framework.org/SI#hasStatus

#### Description
<p>Linking a SI definition to its status.</p>


#### Inherits from:
owl:Thing



#### Usage


[si:Definition](class-sidefinition.md)
=&gt;&nbsp;_si:hasStatus_&nbsp;=&gt;&nbsp;[rdfs:Literal](class-rdfsliteral.md)

#### Implementation
```rdf
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix si: <http://si-digital-framework.org/SI#> .

si:hasStatus a owl:DatatypeProperty ;
    rdfs:label "has status"@en,
        "a l'état"@fr ;
    rdfs:comment "Linking a SI definition to its status."@en,
        "Associer une définition SI à son état."@fr ;
    rdfs:domain si:Definition ;
    rdfs:range rdfs:Literal .


```









---

_Documentation automatically generated on Fri, 26 Jan 2024 15:50:19 with [Ontospy](http://lambdamusic.github.io/Ontospy/ "Open") (v2.1.1)_