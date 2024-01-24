_Vocabulary: [http://si-digital-framework.org/SI#](index.md)_

---








## Property si:correspondingResolution


#### Tree

* rdf:Property
    * si:correspondingResolution





*NOTE* this is a leaf node.


#### URI
http://si-digital-framework.org/SI#correspondingResolution

#### Description



#### Inherits from:
owl:Thing



#### Usage


[si:SIDecision](class-sisidecision.md)
=&gt;&nbsp;_si:correspondingResolution_&nbsp;=&gt;&nbsp;owl:Thing

#### Implementation
```rdf
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix si: <http://si-digital-framework.org/SI#> .

si:correspondingResolution a owl:DatatypeProperty ;
    rdfs:label "has corresponding resolution"@en,
        "a pour résolution correspondante"@fr ;
    rdfs:domain si:SIDecision .


```









---

_Documentation automatically generated on Wed, 24 Jan 2024 14:19:56 with [Ontospy](http://lambdamusic.github.io/Ontospy/ "Open") (v2.1.1)_