_Vocabulary: [http://si-digital-framework.org/SI#](index.md)_

---








## Property si:hasNonPrefixedUnit


#### Tree

* rdf:Property
    * si:hasNonPrefixedUnit





*NOTE* this is a leaf node.


#### URI
http://si-digital-framework.org/SI#hasNonPrefixedUnit

#### Description
<p>&lt;Prefix&gt; and &lt;NonPrefixedUnit&gt; form a &lt;PrefixedUnit&gt;</p>


#### Inherits from:
owl:Thing



#### Usage


[si:PrefixedUnit](class-siprefixedunit.md)
=&gt;&nbsp;_si:hasNonPrefixedUnit_&nbsp;=&gt;&nbsp;[si:MeasurementUnit](class-simeasurementunit.md)

#### Implementation
```rdf
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix si: <http://si-digital-framework.org/SI#> .

si:hasNonPrefixedUnit a owl:ObjectProperty ;
    rdfs:label "has non prefixed unit"@en,
        "a pour unité sans préfixe"@fr ;
    rdfs:comment "<Prefix> and <NonPrefixedUnit> form a <PrefixedUnit>" ;
    rdfs:domain si:PrefixedUnit ;
    rdfs:range si:MeasurementUnit .


```









---

_Documentation automatically generated on Wed, 07 Feb 2024 16:02:36 with [Ontospy](http://lambdamusic.github.io/Ontospy/ "Open") (v2.1.1)_