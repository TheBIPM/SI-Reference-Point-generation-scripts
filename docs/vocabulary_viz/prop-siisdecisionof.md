_Vocabulary: [http://si-digital-framework.org/SI#](index.md)_

---








## Property si:isDecisionOf


#### Tree

* rdf:Property
    * si:isDecisionOf





*NOTE* this is a leaf node.


#### URI
http://si-digital-framework.org/SI#isDecisionOf

#### Description



#### Inherits from:
owl:Thing



#### Usage


[si:SIDecision](class-sisidecision.md)
=&gt;&nbsp;_si:isDecisionOf_&nbsp;=&gt;&nbsp;[si:SIDecisionTarget](class-sisidecisiontarget.md)

#### Implementation
```rdf
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix si: <http://si-digital-framework.org/SI#> .

si:isDecisionOf a owl:DatatypeProperty ;
    rdfs:label "is decision of"@en,
        "est la décision de"@fr ;
    rdfs:domain si:SIDecision ;
    rdfs:range si:SIDecisionTarget .


```









---

_Documentation automatically generated on Wed, 24 Jan 2024 14:19:56 with [Ontospy](http://lambdamusic.github.io/Ontospy/ "Open") (v2.1.1)_