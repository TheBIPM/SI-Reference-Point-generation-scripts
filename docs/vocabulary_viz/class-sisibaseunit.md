_Vocabulary: [http://si-digital-framework.org/SI#](index.md)_

---





    


## Class si:SIBaseUnit


#### Tree


* [si:MeasurementUnit](class-simeasurementunit.md)

    * si:SIBaseUnit





*NOTE* this is a leaf node.


#### URI
http://si-digital-framework.org/SI#SIBaseUnit

#### Description
<p>Class of SI base units. Several definitions can be attached to this class to represent definitions of the BaseUnit throughout time.</p>



#### Inherits from (1)

- [si:MeasurementUnit](class-simeasurementunit.md)







#### Implementation
```rdf
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix si: <http://si-digital-framework.org/SI#> .

si:SIBaseUnit a owl:Class ;
    rdfs:label "base unit"@en,
        "unité de base"@fr ;
    rdfs:comment "Class of SI base units. Several definitions can be attached to this class to represent definitions of the BaseUnit throughout time."@en,
        "La classe des unités de base SI. Plusieurs définitions peuvent être attachées à cette classe pour représenter les définitions de l'unité de base en question à travers les temps."@fr ;
    rdfs:isDefinedBy "VIM3 1.10" ;
    rdfs:subClassOf si:MeasurementUnit ;
    owl:disjointWith si:SISpecialNamedUnit,
        si:nonSIUnit .


```




#### Instances of si:SIBaseUnit can have the following properties:

<table border="1" cellspacing="3" cellpadding="5" class="classproperties table-hover ">

    <tr>
        <th height="40">Property</th><th>Description</th><th>Expected Type</th>
    </tr>

          

        
            
        
        <tr style="background: lightcyan;text-align: left;">
            <th colspan="3" height="10" class="treeinfo"><span style="font-size: 80%;">
            From <a title="si:SIBaseUnit" href="class-sisibaseunit.md" class="rdfclass">si:SIBaseUnit</a></span>
            </th>
        </tr>       

            
            <tr>
                <td class="firsttd">
                    <a class="propcolor" title="si:hasDefinition" href="prop-sihasdefinition.md">si:hasDefinition</a>         
                </td>
                <td class="thirdtd">
                    <span><bound method RdfEntity.bestDescription of <Property *http://si-digital-framework.org/SI#hasDefinition*>></span>
                </td>
                <td class="secondtd">
                    
                    

                        <a title="si:Definition" href="class-sidefinition.md" class="rdfclass">si:Definition</a>

                    
                    
                </td>
            </tr>

            

        

          

        
            
        
        <tr style="background: lightcyan;text-align: left;">
            <th colspan="3" height="10" class="treeinfo"><span style="font-size: 80%;">
            From <a title="si:MeasurementUnit" href="class-simeasurementunit.md" class="rdfclass">si:MeasurementUnit</a></span>
            </th>
        </tr>       

            
            <tr>
                <td class="firsttd">
                    <a class="propcolor" title="si:isUnitOfQtyKind" href="prop-siisunitofqtykind.md">si:isUnitOfQtyKind</a>         
                </td>
                <td class="thirdtd">
                    <span><bound method RdfEntity.bestDescription of <Property *http://si-digital-framework.org/SI#isUnitOfQtyKind*>></span>
                </td>
                <td class="secondtd">
                    
                    

                        <a title="si:QuantityKind" href="class-siquantitykind.md" class="rdfclass">si:QuantityKind</a>

                    
                    
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