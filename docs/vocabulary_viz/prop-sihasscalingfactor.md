_Vocabulary: [http://si-digital-framework.org/SI#](index.md)_

---








## Property si:hasScalingFactor


#### Tree

* rdf:Property
    * si:hasScalingFactor





*NOTE* this is a leaf node.


#### URI
http://si-digital-framework.org/SI#hasScalingFactor

#### Description
<p>Linking an SI prefix to its scaling factor.</p>


#### Inherits from:
owl:Thing



#### Usage


[si:SIPrefix](class-sisiprefix.md)
=&gt;&nbsp;_si:hasScalingFactor_&nbsp;=&gt;&nbsp;[rdfs:Literal](class-rdfsliteral.md)

#### Implementation
```rdf
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix si: <http://si-digital-framework.org/SI#> .

si:hasScalingFactor a owl:DatatypeProperty ;
    rdfs:label "has scaling factor"@en,
        "a un facteur d'échelle"@fr ;
    rdfs:comment "Linking an SI prefix to its scaling factor."@en,
        "Associer un préfixe SI à son facteur d'échelle."@fr ;
    rdfs:domain si:SIPrefix ;
    rdfs:range rdfs:Literal .


```









---

_Documentation automatically generated on Wed, 24 Jan 2024 14:19:56 with [Ontospy](http://lambdamusic.github.io/Ontospy/ "Open") (v2.1.1)_