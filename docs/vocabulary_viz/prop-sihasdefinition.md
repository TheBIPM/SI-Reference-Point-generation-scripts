_Vocabulary: [http://si-digital-framework.org/SI#](index.md)_

---








## Property si:hasDefinition


#### Tree

* rdf:Property
    * si:hasDefinition





*NOTE* this is a leaf node.


#### URI
http://si-digital-framework.org/SI#hasDefinition

#### Description
<p>Linking an SI base unit to its definition.</p>


#### Inherits from:
owl:Thing



#### Usage


[si:SIBaseUnit](class-sisibaseunit.md)
=&gt;&nbsp;_si:hasDefinition_&nbsp;=&gt;&nbsp;[si:Definition](class-sidefinition.md)

#### Implementation
```rdf
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix si: <http://si-digital-framework.org/SI#> .

si:hasDefinition a owl:ObjectProperty ;
    rdfs:label "has definition"@en,
        "a une définition"@fr ;
    rdfs:comment "Linking an SI base unit to its definition."@en,
        "Associer une unité de base SI à sa définition."@fr ;
    rdfs:domain si:SIBaseUnit ;
    rdfs:range si:Definition .


```









---

_Documentation automatically generated on Wed, 24 Jan 2024 16:24:45 with [Ontospy](http://lambdamusic.github.io/Ontospy/ "Open") (v2.1.1)_