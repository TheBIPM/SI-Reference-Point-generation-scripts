_Vocabulary: [http://si-digital-framework.org/SI#](index.md)_

---








## Property si:hasNoteText


#### Tree

* rdf:Property
    * si:hasNoteText





*NOTE* this is a leaf node.


#### URI
http://si-digital-framework.org/SI#hasNoteText

#### Description
<p>The order index of a definition note.</p>


#### Inherits from:
owl:Thing



#### Usage


[si:DefinitionNote](class-sidefinitionnote.md)
=&gt;&nbsp;_si:hasNoteText_&nbsp;=&gt;&nbsp;[rdfs:Literal](class-rdfsliteral.md)

#### Implementation
```rdf
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix si: <http://si-digital-framework.org/SI#> .

si:hasNoteText a owl:DatatypeProperty ;
    rdfs:label "has note text"@en,
        "a un index de notes"@fr ;
    rdfs:comment "The order index of a definition note."@en,
        "Index d'ordre d'une note de définition."@fr ;
    rdfs:domain si:DefinitionNote ;
    rdfs:range rdfs:Literal .


```









---

_Documentation automatically generated on Wed, 24 Jan 2024 14:19:56 with [Ontospy](http://lambdamusic.github.io/Ontospy/ "Open") (v2.1.1)_