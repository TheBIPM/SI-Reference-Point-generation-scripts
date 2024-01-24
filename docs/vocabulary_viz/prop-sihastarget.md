_Vocabulary: [http://si-digital-framework.org/SI#](index.md)_

---








## Property si:hasTarget


#### Tree

* rdf:Property
    * si:hasTarget





*NOTE* this is a leaf node.


#### URI
http://si-digital-framework.org/SI#hasTarget

#### Description



#### Inherits from:
owl:Thing



#### Usage


[si:SIDecisionScope](class-sisidecisionscope.md)
=&gt;&nbsp;_si:hasTarget_&nbsp;=&gt;&nbsp;[si:SIDecisionTarget](class-sisidecisiontarget.md)

#### Implementation
```rdf
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix si: <http://si-digital-framework.org/SI#> .

si:hasTarget a owl:DatatypeProperty ;
    rdfs:label "has target"@en,
        "a pour cible"@fr ;
    rdfs:domain si:SIDecisionScope ;
    rdfs:range si:SIDecisionTarget ;
    owl:inverseOf si:isTargetOf .


```









---

_Documentation automatically generated on Wed, 24 Jan 2024 14:19:56 with [Ontospy](http://lambdamusic.github.io/Ontospy/ "Open") (v2.1.1)_