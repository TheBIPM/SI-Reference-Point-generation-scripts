_Vocabulary: [http://si-digital-framework.org/SI#](index.md)_

---








## Property si:hasEndValidity


#### Tree

* rdf:Property
    * si:hasEndValidity





*NOTE* this is a leaf node.


#### URI
http://si-digital-framework.org/SI#hasEndValidity

#### Description
<p>Linking an SI definition to its ending validity date.</p>


#### Inherits from:
owl:Thing



#### Usage


[si:Definition](class-sidefinition.md)
=&gt;&nbsp;_si:hasEndValidity_&nbsp;=&gt;&nbsp;[xsd:date](class-xsddate.md)

#### Implementation
```rdf
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix si: <http://si-digital-framework.org/SI#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

si:hasEndValidity a owl:DatatypeProperty ;
    rdfs:label "has end validity"@en,
        "a fin de validité"@fr ;
    rdfs:comment "Linking an SI definition to its ending validity date."@en,
        "Associer une définition SI à sa date de fin de validité."@fr ;
    rdfs:domain si:Definition ;
    rdfs:range xsd:date .


```









---

_Documentation automatically generated on Wed, 24 Jan 2024 16:24:45 with [Ontospy](http://lambdamusic.github.io/Ontospy/ "Open") (v2.1.1)_