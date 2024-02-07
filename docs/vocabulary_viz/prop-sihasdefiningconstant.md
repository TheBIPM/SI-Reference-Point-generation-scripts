_Vocabulary: [http://si-digital-framework.org/SI#](index.md)_

---








## Property si:hasDefiningConstant


#### Tree

* rdf:Property
    * si:hasDefiningConstant





*NOTE* this is a leaf node.


#### URI
http://si-digital-framework.org/SI#hasDefiningConstant

#### Description
<p>Linking a definition to its defining constant.</p>


#### Inherits from:
owl:Thing



#### Usage


[si:Definition](class-sidefinition.md)
=&gt;&nbsp;_si:hasDefiningConstant_&nbsp;=&gt;&nbsp;[si:Constant](class-siconstant.md)

#### Implementation
```rdf
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix si: <http://si-digital-framework.org/SI#> .

si:hasDefiningConstant a owl:ObjectProperty ;
    rdfs:label "has defining constant"@en,
        "a une constante de définition"@fr ;
    rdfs:comment "Linking a definition to its defining constant."@en,
        "Associer une définition à sa constante de définition."@fr ;
    rdfs:domain si:Definition ;
    rdfs:range si:Constant .


```









---

_Documentation automatically generated on Wed, 07 Feb 2024 16:02:36 with [Ontospy](http://lambdamusic.github.io/Ontospy/ "Open") (v2.1.1)_