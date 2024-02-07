_Vocabulary: [http://si-digital-framework.org/SI#](index.md)_

---








## Property si:hasDefiningResolution


#### Tree

* rdf:Property
    * si:hasDefiningResolution





*NOTE* this is a leaf node.


#### URI
http://si-digital-framework.org/SI#hasDefiningResolution

#### Description
<p>Linking an SI definition to the resolution by which it was adopted.</p>


#### Inherits from:
owl:Thing



#### Usage


[na38f2c0b404d4008bcfb1c25887fbc6bb23](entity-na38f2c0b404d4008bcfb1c25887fbc6bb23.md)
=&gt;&nbsp;_si:hasDefiningResolution_&nbsp;=&gt;&nbsp;[rb:Resolution](class-rbresolution.md)

#### Implementation
```rdf
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rb: <http://si-digital-framework.org/bodies#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix si: <http://si-digital-framework.org/SI#> .

si:hasDefiningResolution a owl:ObjectProperty ;
    rdfs:label "has defining resolution"@en,
        "a une résolution déterminante"@fr ;
    rdfs:comment "Linking an SI definition to the resolution by which it was adopted."@en,
        "Associer une définition SI à la résolution par laquelle elle a été adoptée."@fr ;
    rdfs:domain [ owl:oneOf ( si:Definition si:Constant ) ] ;
    rdfs:range rb:Resolution .


```









---

_Documentation automatically generated on Wed, 07 Feb 2024 16:02:36 with [Ontospy](http://lambdamusic.github.io/Ontospy/ "Open") (v2.1.1)_