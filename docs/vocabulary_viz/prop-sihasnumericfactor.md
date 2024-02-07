_Vocabulary: [http://si-digital-framework.org/SI#](index.md)_

---








## Property si:hasNumericFactor


#### Tree


* [si:hasTerm](prop-sihasterm.md)

    * si:hasNumericFactor





*NOTE* this is a leaf node.


#### URI
http://si-digital-framework.org/SI#hasNumericFactor

#### Description



#### Inherits from (1)

- [si:hasTerm](prop-sihasterm.md)




#### Usage


[si:MeasurementUnit](class-simeasurementunit.md)
=&gt;&nbsp;_si:hasNumericFactor_&nbsp;=&gt;&nbsp;owl:Thing

#### Implementation
```rdf
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix si: <http://si-digital-framework.org/SI#> .

si:hasNumericFactor a owl:DatatypeProperty ;
    rdfs:label "has numeric factor"@en,
        "a pour facteur ce nombre"@fr ;
    rdfs:domain si:MeasurementUnit ;
    rdfs:subPropertyOf si:hasTerm .


```









---

_Documentation automatically generated on Wed, 07 Feb 2024 16:02:36 with [Ontospy](http://lambdamusic.github.io/Ontospy/ "Open") (v2.1.1)_