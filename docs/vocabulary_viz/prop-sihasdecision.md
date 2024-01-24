_Vocabulary: [http://si-digital-framework.org/SI#](index.md)_

---








## Property si:hasDecision


#### Tree

* rdf:Property
    * si:hasDecision





*NOTE* this is a leaf node.


#### URI
http://si-digital-framework.org/SI#hasDecision

#### Description



#### Inherits from:
owl:Thing



#### Usage


[si:SIDecisionTarget](class-sisidecisiontarget.md)
=&gt;&nbsp;_si:hasDecision_&nbsp;=&gt;&nbsp;[si:SIDecision](class-sisidecision.md)

#### Implementation
```rdf
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix si: <http://si-digital-framework.org/SI#> .

si:hasDecision a owl:DatatypeProperty ;
    rdfs:label "has decision"@en,
        "a pour décision"@fr ;
    rdfs:domain si:SIDecisionTarget ;
    rdfs:range si:SIDecision ;
    owl:inverseOf si:isDecisionOf .


```









---

_Documentation automatically generated on Wed, 24 Jan 2024 16:24:45 with [Ontospy](http://lambdamusic.github.io/Ontospy/ "Open") (v2.1.1)_