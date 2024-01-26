_Vocabulary: [http://si-digital-framework.org/SI#](index.md)_

---








## Property si:hasSymbol


#### Tree

* rdf:Property
    * si:hasSymbol





*NOTE* this is a leaf node.


#### URI
http://si-digital-framework.org/SI#hasSymbol

#### Description
<p>Linking a measurement unit or prefix to a symbol.</p>


#### Inherits from:
owl:Thing



#### Usage
owl:Thing=&gt;&nbsp;_si:hasSymbol_&nbsp;=&gt;&nbsp;[xsd:string](class-xsdstring.md)

#### Implementation
```rdf
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix si: <http://si-digital-framework.org/SI#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

si:hasSymbol a owl:DatatypeProperty ;
    rdfs:label "has symbol"@en,
        "a un symbole"@fr ;
    rdfs:comment "Linking a measurement unit or prefix to a symbol."@en,
        "Associer une unité de mesure ou un préfixe à un symbole."@fr ;
    rdfs:range xsd:string .


```









---

_Documentation automatically generated on Fri, 26 Jan 2024 15:50:19 with [Ontospy](http://lambdamusic.github.io/Ontospy/ "Open") (v2.1.1)_