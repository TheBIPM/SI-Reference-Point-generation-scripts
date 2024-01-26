_Vocabulary: [http://si-digital-framework.org/SI#](index.md)_

---








## Property si:hasPreviousDefinition


#### Tree

* rdf:Property
    * si:hasPreviousDefinition





*NOTE* this is a leaf node.


#### URI
http://si-digital-framework.org/SI#hasPreviousDefinition

#### Description
<p>Linking an SI definition version to the previous version.</p>


#### Inherits from:
owl:Thing



#### Usage


[si:Definition](class-sidefinition.md)
=&gt;&nbsp;_si:hasPreviousDefinition_&nbsp;=&gt;&nbsp;[si:Definition](class-sidefinition.md)

#### Implementation
```rdf
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix si: <http://si-digital-framework.org/SI#> .

si:hasPreviousDefinition a owl:ObjectProperty ;
    rdfs:label "has previous definition"@en,
        "a la définition précédente"@fr ;
    rdfs:comment "Linking an SI definition version to the previous version."@en,
        "Associer une version de définition SI à la version précédente."@fr ;
    rdfs:domain si:Definition ;
    rdfs:range si:Definition ;
    owl:inverseOf si:hasNextDefinition .


```









---

_Documentation automatically generated on Fri, 26 Jan 2024 15:50:19 with [Ontospy](http://lambdamusic.github.io/Ontospy/ "Open") (v2.1.1)_