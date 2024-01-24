_Vocabulary: [http://si-digital-framework.org/SI#](index.md)_

---








## Property si:hasNextDefinition


#### Tree

* rdf:Property
    * si:hasNextDefinition





*NOTE* this is a leaf node.


#### URI
http://si-digital-framework.org/SI#hasNextDefinition

#### Description
<p>Linking an SI definition version to the next version.</p>


#### Inherits from:
owl:Thing



#### Usage


[si:Definition](class-sidefinition.md)
=&gt;&nbsp;_si:hasNextDefinition_&nbsp;=&gt;&nbsp;[si:Definition](class-sidefinition.md)

#### Implementation
```rdf
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix si: <http://si-digital-framework.org/SI#> .

si:hasNextDefinition a owl:ObjectProperty ;
    rdfs:label "has next definition"@en,
        "a la prochaine définition"@fr ;
    rdfs:comment "Linking an SI definition version to the next version."@en,
        "Associer une version de définition SI à la version suivante."@fr ;
    rdfs:domain si:Definition ;
    rdfs:range si:Definition ;
    owl:inverseOf si:hasPreviousDefinition .


```









---

_Documentation automatically generated on Wed, 24 Jan 2024 14:19:56 with [Ontospy](http://lambdamusic.github.io/Ontospy/ "Open") (v2.1.1)_