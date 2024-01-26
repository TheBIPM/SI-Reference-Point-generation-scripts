_Vocabulary: [http://si-digital-framework.org/SI#](index.md)_

---








## Property si:isTargetOf


#### Tree

* rdf:Property
    * si:isTargetOf





*NOTE* this is a leaf node.


#### URI
http://si-digital-framework.org/SI#isTargetOf

#### Description



#### Inherits from:
owl:Thing



#### Usage


[si:DecisionTarget](class-sidecisiontarget.md)
=&gt;&nbsp;_si:isTargetOf_&nbsp;=&gt;&nbsp;[si:SIDecisionScope](class-sisidecisionscope.md)

#### Implementation
```rdf
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix si: <http://si-digital-framework.org/SI#> .

si:isTargetOf a owl:DatatypeProperty ;
    rdfs:label "is target of"@en,
        "est la cible de"@fr ;
    rdfs:domain si:DecisionTarget ;
    rdfs:range si:SIDecisionScope .


```









---

_Documentation automatically generated on Fri, 26 Jan 2024 15:50:19 with [Ontospy](http://lambdamusic.github.io/Ontospy/ "Open") (v2.1.1)_