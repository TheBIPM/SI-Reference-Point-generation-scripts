_Vocabulary: [http://si-digital-framework.org/SI#](index.md)_

---








## Property si:hasRightUnitFactor


#### Tree


* [si:hasUnitFactor](prop-sihasunitfactor.md)

    * si:hasRightUnitFactor





*NOTE* this is a leaf node.


#### URI
http://si-digital-framework.org/SI#hasRightUnitFactor

#### Description
<p>preserve order of multiplication</p>


#### Inherits from (2)

- [si:hasUnitFactor](prop-sihasunitfactor.md)

- [si:hasFactor](prop-sihasfactor.md)




#### Usage
owl:Thing=&gt;&nbsp;_si:hasRightUnitFactor_&nbsp;=&gt;&nbsp;owl:Thing

#### Implementation
```rdf
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix si: <http://si-digital-framework.org/SI#> .

si:hasRightUnitFactor a owl:ObjectProperty ;
    rdfs:label "has right unit factor" ;
    rdfs:comment "preserve order of multiplication" ;
    rdfs:subPropertyOf si:hasUnitFactor .


```









---

_Documentation automatically generated on Wed, 24 Jan 2024 14:19:56 with [Ontospy](http://lambdamusic.github.io/Ontospy/ "Open") (v2.1.1)_