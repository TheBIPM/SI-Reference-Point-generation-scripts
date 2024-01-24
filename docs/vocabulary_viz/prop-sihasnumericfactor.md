_Vocabulary: [http://si-digital-framework.org/SI#](index.md)_

---








## Property si:hasNumericFactor


#### Tree


* [si:hasFactor](prop-sihasfactor.md)

    * si:hasNumericFactor





*NOTE* this is a leaf node.


#### URI
http://si-digital-framework.org/SI#hasNumericFactor

#### Description



#### Inherits from (1)

- [si:hasFactor](prop-sihasfactor.md)




#### Usage
owl:Thing=&gt;&nbsp;_si:hasNumericFactor_&nbsp;=&gt;&nbsp;owl:Thing

#### Implementation
```rdf
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix schema: <https://schema.org/> .
@prefix si: <http://si-digital-framework.org/SI#> .

si:hasNumericFactor a owl:DatatypeProperty ;
    rdfs:label "has numeric factor" ;
    rdfs:subPropertyOf si:hasFactor ;
    schema:domainIncludes si:MeasurementUnit .


```









---

_Documentation automatically generated on Wed, 24 Jan 2024 14:19:56 with [Ontospy](http://lambdamusic.github.io/Ontospy/ "Open") (v2.1.1)_