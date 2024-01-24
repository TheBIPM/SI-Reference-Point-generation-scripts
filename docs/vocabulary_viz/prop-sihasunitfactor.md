_Vocabulary: [http://si-digital-framework.org/SI#](index.md)_

---








## Property si:hasUnitFactor


#### Tree


* [si:hasFactor](prop-sihasfactor.md)

    * si:hasUnitFactor


        * [si:hasLeftUnitFactor](prop-sihasleftunitfactor.md)

        * [si:hasRightUnitFactor](prop-sihasrightunitfactor.md)
        






#### URI
http://si-digital-framework.org/SI#hasUnitFactor

#### Description



#### Inherits from (1)

- [si:hasFactor](prop-sihasfactor.md)




#### Usage
owl:Thing=&gt;&nbsp;_si:hasUnitFactor_&nbsp;=&gt;&nbsp;owl:Thing

#### Implementation
```rdf
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix schema: <https://schema.org/> .
@prefix si: <http://si-digital-framework.org/SI#> .

si:hasUnitFactor a owl:ObjectProperty ;
    rdfs:label "has unit factor" ;
    rdfs:subPropertyOf si:hasFactor ;
    schema:domainIncludes si:MeasurementUnit ;
    schema:rangeIncludes si:MeasurementUnit .


```









---

_Documentation automatically generated on Wed, 24 Jan 2024 16:24:45 with [Ontospy](http://lambdamusic.github.io/Ontospy/ "Open") (v2.1.1)_