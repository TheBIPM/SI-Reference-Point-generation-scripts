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

[n0fe14176d0b84ad0ae63b0a583714332b12](entity-n0fe14176d0b84ad0ae63b0a583714332b12.md)
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

_Documentation automatically generated on Fri, 26 Jan 2024 15:50:19 with [Ontospy](http://lambdamusic.github.io/Ontospy/ "Open") (v2.1.1)_