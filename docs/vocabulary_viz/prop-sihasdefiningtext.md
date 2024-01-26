_Vocabulary: [http://si-digital-framework.org/SI#](index.md)_

---








## Property si:hasDefiningText


#### Tree

* rdf:Property
    * si:hasDefiningText





*NOTE* this is a leaf node.


#### URI
http://si-digital-framework.org/SI#hasDefiningText

#### Description
<p>Linking an SI definition to the defining text.</p>


#### Inherits from:
owl:Thing



#### Usage


[si:Definition](class-sidefinition.md)
=&gt;&nbsp;_si:hasDefiningText_&nbsp;=&gt;&nbsp;[rdfs:Literal](class-rdfsliteral.md)

#### Implementation
```rdf
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix si: <http://si-digital-framework.org/SI#> .

si:hasDefiningText a owl:DatatypeProperty ;
    rdfs:label "has defining text"@en,
        "a un texte de définition"@fr ;
    rdfs:comment "Linking an SI definition to the defining text."@en,
        "Associer une définition SI au texte de définition."@fr ;
    rdfs:domain si:Definition ;
    rdfs:range rdfs:Literal .


```









---

_Documentation automatically generated on Fri, 26 Jan 2024 15:50:19 with [Ontospy](http://lambdamusic.github.io/Ontospy/ "Open") (v2.1.1)_