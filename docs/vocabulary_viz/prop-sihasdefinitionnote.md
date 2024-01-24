_Vocabulary: [http://si-digital-framework.org/SI#](index.md)_

---








## Property si:hasDefinitionNote


#### Tree

* rdf:Property
    * si:hasDefinitionNote





*NOTE* this is a leaf node.


#### URI
http://si-digital-framework.org/SI#hasDefinitionNote

#### Description
<p>Linking an SI definition to a definition note.</p>


#### Inherits from:
owl:Thing



#### Usage


[si:Definition](class-sidefinition.md)
=&gt;&nbsp;_si:hasDefinitionNote_&nbsp;=&gt;&nbsp;[si:DefinitionNote](class-sidefinitionnote.md)

#### Implementation
```rdf
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix si: <http://si-digital-framework.org/SI#> .

si:hasDefinitionNote a owl:ObjectProperty ;
    rdfs:label "has definition note"@en,
        "a une note de définition"@fr ;
    rdfs:comment "Linking an SI definition to a definition note."@en,
        "Associer une définition SI à une note de définition."@fr ;
    rdfs:domain si:Definition ;
    rdfs:range si:DefinitionNote .


```









---

_Documentation automatically generated on Wed, 24 Jan 2024 16:24:45 with [Ontospy](http://lambdamusic.github.io/Ontospy/ "Open") (v2.1.1)_