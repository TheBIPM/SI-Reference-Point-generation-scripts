_Vocabulary: [http://si-digital-framework.org/SI#](index.md)_

---








## Property si:hasRightQuantityTerm


#### Tree


* [si:hasQuantityTerm](prop-sihasquantityterm.md)

    * si:hasRightQuantityTerm





*NOTE* this is a leaf node.


#### URI
http://si-digital-framework.org/SI#hasRightQuantityTerm

#### Description
<p>preserve order of multiplication</p>


#### Inherits from (2)

- [si:hasQuantityTerm](prop-sihasquantityterm.md)

- [si:hasTerm](prop-sihasterm.md)




#### Usage


[si:QuantityProduct](class-siquantityproduct.md)
=&gt;&nbsp;_si:hasRightQuantityTerm_&nbsp;=&gt;&nbsp;[si:QuantityKind](class-siquantitykind.md)

#### Implementation
```rdf
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix si: <http://si-digital-framework.org/SI#> .

si:hasRightQuantityTerm a owl:ObjectProperty ;
    rdfs:label "has right quantity term"@en,
        "a pour terme de droite cette quantité"@fr ;
    rdfs:comment "preserve order of multiplication" ;
    rdfs:domain si:QuantityProduct ;
    rdfs:range si:QuantityKind ;
    rdfs:subPropertyOf si:hasQuantityTerm .


```









---

_Documentation automatically generated on Fri, 26 Jan 2024 15:50:19 with [Ontospy](http://lambdamusic.github.io/Ontospy/ "Open") (v2.1.1)_