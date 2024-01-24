_Vocabulary: [http://si-digital-framework.org/SI#](index.md)_

---








## Property si:hasConversionFactor


#### Tree

* rdf:Property
    * si:hasConversionFactor





*NOTE* this is a leaf node.


#### URI
http://si-digital-framework.org/SI#hasConversionFactor

#### Description
<p>The conversion factor between non-SI unit and an SI Unit (number SI unit contained in 1 non SI unit)</p>


#### Inherits from:
owl:Thing



#### Usage


[si:nonSIUnit](class-sinonsiunit.md)
=&gt;&nbsp;_si:hasConversionFactor_&nbsp;=&gt;&nbsp;[rdfs:Literal](class-rdfsliteral.md)

#### Implementation
```rdf
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix si: <http://si-digital-framework.org/SI#> .

si:hasConversionFactor a owl:DatatypeProperty ;
    rdfs:label "has a conversion factor"@en,
        "a un facteur de conversion"@fr ;
    rdfs:comment "The conversion factor between non-SI unit and an SI Unit (number SI unit contained in 1 non SI unit)"@en,
        "Le facteur de conversion entre l'unité non SI et l'unité dans le SI (nombre d'unité de contenu dans l'unité non-SI)"@fr ;
    rdfs:domain si:nonSIUnit ;
    rdfs:range rdfs:Literal .


```









---

_Documentation automatically generated on Wed, 24 Jan 2024 14:19:56 with [Ontospy](http://lambdamusic.github.io/Ontospy/ "Open") (v2.1.1)_