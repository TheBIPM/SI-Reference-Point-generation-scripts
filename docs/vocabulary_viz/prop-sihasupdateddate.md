_Vocabulary: [http://si-digital-framework.org/SI#](index.md)_

---








## Property si:hasUpdatedDate


#### Tree

* rdf:Property
    * si:hasUpdatedDate





*NOTE* this is a leaf node.


#### URI
http://si-digital-framework.org/SI#hasUpdatedDate

#### Description



#### Inherits from:
owl:Thing



#### Usage


[si:Constant](class-siconstant.md)
=&gt;&nbsp;_si:hasUpdatedDate_&nbsp;=&gt;&nbsp;[xsd:date](class-xsddate.md)

#### Implementation
```rdf
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix si: <http://si-digital-framework.org/SI#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

si:hasUpdatedDate a owl:DatatypeProperty ;
    rdfs:label "has updated date"@en,
        "a mis à jour la date"@fr ;
    rdfs:domain si:Constant ;
    rdfs:range xsd:date .


```









---

_Documentation automatically generated on Wed, 24 Jan 2024 14:19:56 with [Ontospy](http://lambdamusic.github.io/Ontospy/ "Open") (v2.1.1)_