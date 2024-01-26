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


[si:UnitPower](class-siunitpower.md)
=&gt;&nbsp;_si:hasNumericExponent_&nbsp;=&gt;&nbsp;[xsd:int](class-xsdint.md)

#### Implementation
```rdf
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix si: <http://si-digital-framework.org/SI#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

si:hasNumericExponent a owl:DatatypeProperty ;
    rdfs:label "has numeric exponent"@en,
        "a pour exposant ce nombre"@fr ;
    rdfs:comment "UnitBase ^ NumericExponent" ;
    rdfs:domain si:UnitPower ;
    rdfs:range xsd:int .


```









---

_Documentation automatically generated on Fri, 26 Jan 2024 15:50:19 with [Ontospy](http://lambdamusic.github.io/Ontospy/ "Open") (v2.1.1)_