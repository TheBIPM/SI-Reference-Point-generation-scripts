_Vocabulary: [http://si-digital-framework.org/SI#](index.md)_

---








## Property si:hasPrefix


#### Tree

* rdf:Property
    * si:hasPrefix





*NOTE* this is a leaf node.


#### URI
http://si-digital-framework.org/SI#hasPrefix

#### Description
<p>&lt;Prefix&gt; and &lt;NonPrefixedUnit&gt; form a &lt;PrefixedUnit&gt;</p>


#### Inherits from:
owl:Thing



#### Usage


[si:PrefixedUnit](class-siprefixedunit.md)
=&gt;&nbsp;_si:hasPrefix_&nbsp;=&gt;&nbsp;[si:SIPrefix](class-sisiprefix.md)

#### Implementation
```rdf
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix si: <http://si-digital-framework.org/SI#> .

si:hasPrefix a owl:ObjectProperty ;
    rdfs:label "has prefix" ;
    rdfs:comment "<Prefix> and <NonPrefixedUnit> form a <PrefixedUnit>" ;
    rdfs:domain si:PrefixedUnit ;
    rdfs:range si:SIPrefix .


```









---

_Documentation automatically generated on Wed, 24 Jan 2024 16:24:45 with [Ontospy](http://lambdamusic.github.io/Ontospy/ "Open") (v2.1.1)_