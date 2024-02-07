_Vocabulary: [http://si-digital-framework.org/SI#](index.md)_

---








## Property si:isDefiningResolutionOf


#### Tree

* rdf:Property
    * si:isDefiningResolutionOf





*NOTE* this is a leaf node.


#### URI
http://si-digital-framework.org/SI#isDefiningResolutionOf

#### Description
<p>Linking a resolution to the SI definition it defined.</p>


#### Inherits from:
owl:Thing



#### Usage


[rb:Resolution](class-rbresolution.md) &amp;&amp; 

[na38f2c0b404d4008bcfb1c25887fbc6bb15](entity-na38f2c0b404d4008bcfb1c25887fbc6bb15.md)
=&gt;&nbsp;_si:isDefiningResolutionOf_&nbsp;=&gt;&nbsp;owl:Thing

#### Implementation
```rdf
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rb: <http://si-digital-framework.org/bodies#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix si: <http://si-digital-framework.org/SI#> .

si:isDefiningResolutionOf a owl:ObjectProperty ;
    rdfs:label "is defining resolution of"@en,
        "définit la résolution de"@fr ;
    rdfs:comment "Linking a resolution to the SI definition it defined."@en,
        "Associer une résolution à la définition SI qu'elle a définie."@fr ;
    rdfs:domain rb:Resolution ;
    rdfs:range [ owl:oneOf ( si:Definition si:Constant ) ] ;
    owl:inverseOf si:hasDefiningResolution .


```









---

_Documentation automatically generated on Wed, 07 Feb 2024 16:02:36 with [Ontospy](http://lambdamusic.github.io/Ontospy/ "Open") (v2.1.1)_