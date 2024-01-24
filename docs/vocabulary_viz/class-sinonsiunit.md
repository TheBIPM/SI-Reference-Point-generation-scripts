_Vocabulary: [http://si-digital-framework.org/SI#](index.md)_

---





    


## Class si:nonSIUnit


#### Tree


* [si:MeasurementUnit](class-simeasurementunit.md)

    * si:nonSIUnit





*NOTE* this is a leaf node.


#### URI
http://si-digital-framework.org/SI#nonSIUnit

#### Description
<p>Non-SI units that are accepted for use with the SI</p>



#### Inherits from (1)

- [si:MeasurementUnit](class-simeasurementunit.md)







#### Implementation
```rdf
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix si: <http://si-digital-framework.org/SI#> .

si:nonSIUnit a owl:Class ;
    rdfs:label "non SI unit"@en,
        "unité en dehors du SI"@fr ;
    rdfs:comment "Non-SI units that are accepted for use with the SI"@en,
        "Unités en dehors du SI dont l’usage est accepté avec le SI"@fr ;
    rdfs:subClassOf si:MeasurementUnit .


```




#### Instances of si:nonSIUnit can have the following properties:

<table border="1" cellspacing="3" cellpadding="5" class="classproperties table-hover ">

    <tr>
        <th height="40">Property</th><th>Description</th><th>Expected Type</th>
    </tr>

          

        
            
        
        <tr style="background: lightcyan;text-align: left;">
            <th colspan="3" height="10" class="treeinfo"><span style="font-size: 80%;">
            From <a title="si:nonSIUnit" href="class-sinonsiunit.md" class="rdfclass">si:nonSIUnit</a></span>
            </th>
        </tr>       

            
            <tr>
                <td class="firsttd">
                    <a class="propcolor" title="si:hasConversionFactor" href="prop-sihasconversionfactor.md">si:hasConversionFactor</a>         
                </td>
                <td class="thirdtd">
                    <span><bound method RdfEntity.bestDescription of <Property *http://si-digital-framework.org/SI#hasConversionFactor*>></span>
                </td>
                <td class="secondtd">
                    
                    

                        <a title="rdfs:Literal" href="class-rdfsliteral.md" class="rdfclass">rdfs:Literal</a>

                    
                    
                </td>
            </tr>

            
            <tr>
                <td class="firsttd">
                    <a class="propcolor" title="si:hasConversionUnit" href="prop-sihasconversionunit.md">si:hasConversionUnit</a>         
                </td>
                <td class="thirdtd">
                    <span><bound method RdfEntity.bestDescription of <Property *http://si-digital-framework.org/SI#hasConversionUnit*>></span>
                </td>
                <td class="secondtd">
                    
                    

                        <a title="si:MeasurementUnit" href="class-simeasurementunit.md" class="rdfclass">si:MeasurementUnit</a>

                    
                    
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