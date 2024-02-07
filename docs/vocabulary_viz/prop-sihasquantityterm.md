_Vocabulary: [http://si-digital-framework.org/SI#](index.md)_

---








## Property si:hasQuantityTerm


#### Tree


* [si:hasTerm](prop-sihasterm.md)

    * si:hasQuantityTerm


        * [si:hasLeftQuantityTerm](prop-sihasleftquantityterm.md)

        * [si:hasRightQuantityTerm](prop-sihasrightquantityterm.md)
        






#### URI
http://si-digital-framework.org/SI#hasQuantityTerm

#### Description



#### Inherits from (1)

- [si:hasTerm](prop-sihasterm.md)




#### Usage
owl:Thing=&gt;&nbsp;_si:hasQuantityTerm_&nbsp;=&gt;&nbsp;owl:Thing

#### Implementation
```rdf
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix si: <http://si-digital-framework.org/SI#> .

si:hasQuantityTerm a owl:ObjectProperty ;
    rdfs:label "has quantity term"@en,
        "a pour terme cette quantité"@fr ;
    rdfs:subPropertyOf si:hasTerm .


```









---

_Documentation automatically generated on Wed, 07 Feb 2024 16:02:36 with [Ontospy](http://lambdamusic.github.io/Ontospy/ "Open") (v2.1.1)_