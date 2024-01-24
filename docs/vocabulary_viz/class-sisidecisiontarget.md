_Vocabulary: [http://si-digital-framework.org/SI#](index.md)_

---





    


## Class si:SIDecisionTarget


#### Tree

* owl:Thing
    * si:SIDecisionTarget





*NOTE* this is a leaf node.


#### URI
http://si-digital-framework.org/SI#SIDecisionTarget

#### Description
<p>The class for SI decisions target.</p>



#### Inherits from:
owl:Thing






#### Implementation
```rdf
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix si: <http://si-digital-framework.org/SI#> .

si:SIDecisionTarget a owl:Class ;
    rdfs:label "SI Decision target"@en,
        "Cible d'une décision SI"@fr ;
    rdfs:comment "The class for SI decisions target."@en,
        "La classe pour les cibles de décisions SI."@fr .


```




#### Instances of si:SIDecisionTarget can have the following properties:

<table border="1" cellspacing="3" cellpadding="5" class="classproperties table-hover ">

    <tr>
        <th height="40">Property</th><th>Description</th><th>Expected Type</th>
    </tr>

          

        
            
        
        <tr style="background: lightcyan;text-align: left;">
            <th colspan="3" height="10" class="treeinfo"><span style="font-size: 80%;">
            From <a title="si:SIDecisionTarget" href="class-sisidecisiontarget.md" class="rdfclass">si:SIDecisionTarget</a></span>
            </th>
        </tr>       

            
            <tr>
                <td class="firsttd">
                    <a class="propcolor" title="si:hasDecision" href="prop-sihasdecision.md">si:hasDecision</a>         
                </td>
                <td class="thirdtd">
                    <span><bound method RdfEntity.bestDescription of <Property *http://si-digital-framework.org/SI#hasDecision*>></span>
                </td>
                <td class="secondtd">
                    
                    

                        <a title="si:SIDecision" href="class-sisidecision.md" class="rdfclass">si:SIDecision</a>

                    
                    
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