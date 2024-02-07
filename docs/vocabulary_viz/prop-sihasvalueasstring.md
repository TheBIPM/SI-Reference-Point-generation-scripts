_Vocabulary: [http://si-digital-framework.org/SI#](index.md)_

---








## Property si:hasValueAsString


#### Tree

* rdf:Property
    * si:hasValueAsString





*NOTE* this is a leaf node.


#### URI
http://si-digital-framework.org/SI#hasValueAsString

#### Description



#### Inherits from:
owl:Thing



#### Usage


[si:Constant](class-siconstant.md)
=&gt;&nbsp;_si:hasValueAsString_&nbsp;=&gt;&nbsp;[xsd:string](class-xsdstring.md)

#### Implementation
```rdf
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix si: <http://si-digital-framework.org/SI#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

si:hasValueAsString a owl:DatatypeProperty ;
    rdfs:label "has value as a string"@en,
        "a une valeur sous forme de chaîne"@fr ;
    rdfs:domain si:Constant ;
    rdfs:range xsd:string .


```









---

_Documentation automatically generated on Wed, 07 Feb 2024 16:02:36 with [Ontospy](http://lambdamusic.github.io/Ontospy/ "Open") (v2.1.1)_