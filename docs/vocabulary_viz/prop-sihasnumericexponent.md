_Vocabulary: [http://si-digital-framework.org/SI#](index.md)_

---








## Property si:hasNumericExponent


#### Tree

* rdf:Property
    * si:hasNumericExponent





*NOTE* this is a leaf node.


#### URI
http://si-digital-framework.org/SI#hasNumericExponent

#### Description
<p>UnitBase ^ NumericExponent</p>


#### Inherits from:
owl:Thing



#### Usage
owl:Thing=&gt;&nbsp;_si:hasNumericExponent_&nbsp;=&gt;&nbsp;owl:Thing

#### Implementation
```rdf
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix si: <http://si-digital-framework.org/SI#> .

si:hasNumericExponent a owl:DatatypeProperty ;
    rdfs:label "has numeric exponent" ;
    rdfs:comment "UnitBase ^ NumericExponent" .


```









---

_Documentation automatically generated on Wed, 24 Jan 2024 16:24:45 with [Ontospy](http://lambdamusic.github.io/Ontospy/ "Open") (v2.1.1)_