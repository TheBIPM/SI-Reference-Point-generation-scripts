_Vocabulary: [http://si-digital-framework.org/SI#](index.md)_

---








## Property si:hasNoteIndex


#### Tree

* rdf:Property
    * si:hasNoteIndex





*NOTE* this is a leaf node.


#### URI
http://si-digital-framework.org/SI#hasNoteIndex

#### Description
<p>The text of a definition note.</p>


#### Inherits from:
owl:Thing



#### Usage


[si:DefinitionNote](class-sidefinitionnote.md)
=&gt;&nbsp;_si:hasNoteIndex_&nbsp;=&gt;&nbsp;[rdfs:Literal](class-rdfsliteral.md)

#### Implementation
```rdf
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix si: <http://si-digital-framework.org/SI#> .

si:hasNoteIndex a owl:DatatypeProperty ;
    rdfs:label "has note index"@en,
        "a un texte de note"@fr ;
    rdfs:comment "The text of a definition note."@en,
        "Le texte d'une note de définition."@fr ;
    rdfs:domain si:DefinitionNote ;
    rdfs:range rdfs:Literal .


```









---

_Documentation automatically generated on Fri, 26 Jan 2024 15:50:19 with [Ontospy](http://lambdamusic.github.io/Ontospy/ "Open") (v2.1.1)_