_Vocabulary: [http://si-digital-framework.org/SI#](index.md)_

---





    


## Class si:Definition


#### Tree

* owl:Thing
    * si:Definition





*NOTE* this is a leaf node.


#### URI
http://si-digital-framework.org/SI#Definition

#### Description
<p>The class for definitions of an SI base unit.</p>



#### Inherits from:
owl:Thing






#### Implementation
```rdf
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix si: <http://si-digital-framework.org/SI#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

si:Definition a owl:Class ;
    rdfs:label "definition of a base unit"@en,
        "définition d'une unité de base"@fr ;
    rdfs:comment "The class for definitions of an SI base unit."@en,
        "La classe pour les notes sur les définitions des unités SI."@fr ;
    rdfs:subClassOf [ a owl:Restriction ;
            owl:minCardinality "1"^^xsd:int ;
            owl:onProperty si:hasStartValidity ] .


```




#### Instances of si:Definition can have the following properties:

<table border="1" cellspacing="3" cellpadding="5" class="classproperties table-hover ">

    <tr>
        <th height="40">Property</th><th>Description</th><th>Expected Type</th>
    </tr>

          

        
            
        
        <tr style="background: lightcyan;text-align: left;">
            <th colspan="3" height="10" class="treeinfo"><span style="font-size: 80%;">
            From <a title="si:Definition" href="class-sidefinition.md" class="rdfclass">si:Definition</a></span>
            </th>
        </tr>       

            
            <tr>
                <td class="firsttd">
                    <a class="propcolor" title="si:hasDefiningText" href="prop-sihasdefiningtext.md">si:hasDefiningText</a>         
                </td>
                <td class="thirdtd">
                    <span><bound method RdfEntity.bestDescription of <Property *http://si-digital-framework.org/SI#hasDefiningText*>></span>
                </td>
                <td class="secondtd">
                    
                    

                        <a title="rdfs:Literal" href="class-rdfsliteral.md" class="rdfclass">rdfs:Literal</a>

                    
                    
                </td>
            </tr>

            
            <tr>
                <td class="firsttd">
                    <a class="propcolor" title="si:hasEndValidity" href="prop-sihasendvalidity.md">si:hasEndValidity</a>         
                </td>
                <td class="thirdtd">
                    <span><bound method RdfEntity.bestDescription of <Property *http://si-digital-framework.org/SI#hasEndValidity*>></span>
                </td>
                <td class="secondtd">
                    
                    

                        <a title="xsd:date" href="class-xsddate.md" class="rdfclass">xsd:date</a>

                    
                    
                </td>
            </tr>

            
            <tr>
                <td class="firsttd">
                    <a class="propcolor" title="si:hasStartValidity" href="prop-sihasstartvalidity.md">si:hasStartValidity</a>         
                </td>
                <td class="thirdtd">
                    <span><bound method RdfEntity.bestDescription of <Property *http://si-digital-framework.org/SI#hasStartValidity*>></span>
                </td>
                <td class="secondtd">
                    
                    

                        <a title="xsd:date" href="class-xsddate.md" class="rdfclass">xsd:date</a>

                    
                    
                </td>
            </tr>

            
            <tr>
                <td class="firsttd">
                    <a class="propcolor" title="si:hasStatus" href="prop-sihasstatus.md">si:hasStatus</a>         
                </td>
                <td class="thirdtd">
                    <span><bound method RdfEntity.bestDescription of <Property *http://si-digital-framework.org/SI#hasStatus*>></span>
                </td>
                <td class="secondtd">
                    
                    

                        <a title="rdfs:Literal" href="class-rdfsliteral.md" class="rdfclass">rdfs:Literal</a>

                    
                    
                </td>
            </tr>

            
            <tr>
                <td class="firsttd">
                    <a class="propcolor" title="si:hasDefiningConstant" href="prop-sihasdefiningconstant.md">si:hasDefiningConstant</a>         
                </td>
                <td class="thirdtd">
                    <span><bound method RdfEntity.bestDescription of <Property *http://si-digital-framework.org/SI#hasDefiningConstant*>></span>
                </td>
                <td class="secondtd">
                    
                    

                        <a title="si:Constant" href="class-siconstant.md" class="rdfclass">si:Constant</a>

                    
                    
                </td>
            </tr>

            
            <tr>
                <td class="firsttd">
                    <a class="propcolor" title="si:hasDefinitionNote" href="prop-sihasdefinitionnote.md">si:hasDefinitionNote</a>         
                </td>
                <td class="thirdtd">
                    <span><bound method RdfEntity.bestDescription of <Property *http://si-digital-framework.org/SI#hasDefinitionNote*>></span>
                </td>
                <td class="secondtd">
                    
                    

                        <a title="si:DefinitionNote" href="class-sidefinitionnote.md" class="rdfclass">si:DefinitionNote</a>

                    
                    
                </td>
            </tr>

            
            <tr>
                <td class="firsttd">
                    <a class="propcolor" title="si:hasNextDefinition" href="prop-sihasnextdefinition.md">si:hasNextDefinition</a>         
                </td>
                <td class="thirdtd">
                    <span><bound method RdfEntity.bestDescription of <Property *http://si-digital-framework.org/SI#hasNextDefinition*>></span>
                </td>
                <td class="secondtd">
                    
                    

                        <a title="si:Definition" href="class-sidefinition.md" class="rdfclass">si:Definition</a>

                    
                    
                </td>
            </tr>

            
            <tr>
                <td class="firsttd">
                    <a class="propcolor" title="si:hasPreviousDefinition" href="prop-sihaspreviousdefinition.md">si:hasPreviousDefinition</a>         
                </td>
                <td class="thirdtd">
                    <span><bound method RdfEntity.bestDescription of <Property *http://si-digital-framework.org/SI#hasPreviousDefinition*>></span>
                </td>
                <td class="secondtd">
                    
                    

                        <a title="si:Definition" href="class-sidefinition.md" class="rdfclass">si:Definition</a>

                    
                    
                </td>
            </tr>

            

        

          

        
            
        
        <tr style="background: lightcyan;text-align: left;">
            <th colspan="3" height="10" class="treeinfo"><span style="font-size: 80%;">
            From <a title="owl:Thing" href="class-owlthing.md" class="rdfclass">owl:Thing</a></span>
            </th>
        </tr>       

            
            <tr>
                <td class="firsttd">
                    <a class="propcolor" title="si:hasBase" href="prop-sihasbase.md">si:hasBase</a>         
                </td>
                <td class="thirdtd">
                    <span><bound method RdfEntity.bestDescription of <Property *http://si-digital-framework.org/SI#hasBase*>></span>
                </td>
                <td class="secondtd">
                    
                        <i>owl:Thing</i>
                    
                </td>
            </tr>

            
            <tr>
                <td class="firsttd">
                    <a class="propcolor" title="si:hasFactor" href="prop-sihasfactor.md">si:hasFactor</a>         
                </td>
                <td class="thirdtd">
                    <span><bound method RdfEntity.bestDescription of <Property *http://si-digital-framework.org/SI#hasFactor*>></span>
                </td>
                <td class="secondtd">
                    
                        <i>owl:Thing</i>
                    
                </td>
            </tr>

            
            <tr>
                <td class="firsttd">
                    <a class="propcolor" title="si:hasLeftUnitFactor" href="prop-sihasleftunitfactor.md">si:hasLeftUnitFactor</a>         
                </td>
                <td class="thirdtd">
                    <span><bound method RdfEntity.bestDescription of <Property *http://si-digital-framework.org/SI#hasLeftUnitFactor*>></span>
                </td>
                <td class="secondtd">
                    
                        <i>owl:Thing</i>
                    
                </td>
            </tr>

            
            <tr>
                <td class="firsttd">
                    <a class="propcolor" title="si:hasNumericExponent" href="prop-sihasnumericexponent.md">si:hasNumericExponent</a>         
                </td>
                <td class="thirdtd">
                    <span><bound method RdfEntity.bestDescription of <Property *http://si-digital-framework.org/SI#hasNumericExponent*>></span>
                </td>
                <td class="secondtd">
                    
                        <i>owl:Thing</i>
                    
                </td>
            </tr>

            
            <tr>
                <td class="firsttd">
                    <a class="propcolor" title="si:hasNumericFactor" href="prop-sihasnumericfactor.md">si:hasNumericFactor</a>         
                </td>
                <td class="thirdtd">
                    <span><bound method RdfEntity.bestDescription of <Property *http://si-digital-framework.org/SI#hasNumericFactor*>></span>
                </td>
                <td class="secondtd">
                    
                        <i>owl:Thing</i>
                    
                </td>
            </tr>

            
            <tr>
                <td class="firsttd">
                    <a class="propcolor" title="si:hasQuantityBase" href="prop-sihasquantitybase.md">si:hasQuantityBase</a>         
                </td>
                <td class="thirdtd">
                    <span><bound method RdfEntity.bestDescription of <Property *http://si-digital-framework.org/SI#hasQuantityBase*>></span>
                </td>
                <td class="secondtd">
                    
                        <i>owl:Thing</i>
                    
                </td>
            </tr>

            
            <tr>
                <td class="firsttd">
                    <a class="propcolor" title="si:hasQuantityFactor" href="prop-sihasquantityfactor.md">si:hasQuantityFactor</a>         
                </td>
                <td class="thirdtd">
                    <span><bound method RdfEntity.bestDescription of <Property *http://si-digital-framework.org/SI#hasQuantityFactor*>></span>
                </td>
                <td class="secondtd">
                    
                        <i>owl:Thing</i>
                    
                </td>
            </tr>

            
            <tr>
                <td class="firsttd">
                    <a class="propcolor" title="si:hasRightUnitFactor" href="prop-sihasrightunitfactor.md">si:hasRightUnitFactor</a>         
                </td>
                <td class="thirdtd">
                    <span><bound method RdfEntity.bestDescription of <Property *http://si-digital-framework.org/SI#hasRightUnitFactor*>></span>
                </td>
                <td class="secondtd">
                    
                        <i>owl:Thing</i>
                    
                </td>
            </tr>

            
            <tr>
                <td class="firsttd">
                    <a class="propcolor" title="si:hasSymbol" href="prop-sihassymbol.md">si:hasSymbol</a>         
                </td>
                <td class="thirdtd">
                    <span><bound method RdfEntity.bestDescription of <Property *http://si-digital-framework.org/SI#hasSymbol*>></span>
                </td>
                <td class="secondtd">
                    
                    

                        <a title="xsd:string" href="class-xsdstring.md" class="rdfclass">xsd:string</a>

                    
                    
                </td>
            </tr>

            
            <tr>
                <td class="firsttd">
                    <a class="propcolor" title="si:hasUnit" href="prop-sihasunit.md">si:hasUnit</a>         
                </td>
                <td class="thirdtd">
                    <span><bound method RdfEntity.bestDescription of <Property *http://si-digital-framework.org/SI#hasUnit*>></span>
                </td>
                <td class="secondtd">
                    
                    

                        <a title="si:MeasurementUnit" href="class-simeasurementunit.md" class="rdfclass">si:MeasurementUnit</a>

                    
                    
                </td>
            </tr>

            
            <tr>
                <td class="firsttd">
                    <a class="propcolor" title="si:hasUnitBase" href="prop-sihasunitbase.md">si:hasUnitBase</a>         
                </td>
                <td class="thirdtd">
                    <span><bound method RdfEntity.bestDescription of <Property *http://si-digital-framework.org/SI#hasUnitBase*>></span>
                </td>
                <td class="secondtd">
                    
                        <i>owl:Thing</i>
                    
                </td>
            </tr>

            
            <tr>
                <td class="firsttd">
                    <a class="propcolor" title="si:hasUnitFactor" href="prop-sihasunitfactor.md">si:hasUnitFactor</a>         
                </td>
                <td class="thirdtd">
                    <span><bound method RdfEntity.bestDescription of <Property *http://si-digital-framework.org/SI#hasUnitFactor*>></span>
                </td>
                <td class="secondtd">
                    
                        <i>owl:Thing</i>
                    
                </td>
            </tr>

            
            <tr>
                <td class="firsttd">
                    <a class="propcolor" title="si:inBaseSIUnits" href="prop-siinbasesiunits.md">si:inBaseSIUnits</a>         
                </td>
                <td class="thirdtd">
                    <span><bound method RdfEntity.bestDescription of <Property *http://si-digital-framework.org/SI#inBaseSIUnits*>></span>
                </td>
                <td class="secondtd">
                    
                    

                        <a title="si:MeasurementUnit" href="class-simeasurementunit.md" class="rdfclass">si:MeasurementUnit</a>

                    
                    
                </td>
            </tr>

            
            <tr>
                <td class="firsttd">
                    <a class="propcolor" title="si:inOtherSIUnits" href="prop-siinothersiunits.md">si:inOtherSIUnits</a>         
                </td>
                <td class="thirdtd">
                    <span><bound method RdfEntity.bestDescription of <Property *http://si-digital-framework.org/SI#inOtherSIUnits*>></span>
                </td>
                <td class="secondtd">
                    
                    

                        <a title="si:MeasurementUnit" href="class-simeasurementunit.md" class="rdfclass">si:MeasurementUnit</a>

                    
                    
                </td>
            </tr>

            

        

    

</table>












---

_Documentation automatically generated on Wed, 24 Jan 2024 14:19:56 with [Ontospy](http://lambdamusic.github.io/Ontospy/ "Open") (v2.1.1)_