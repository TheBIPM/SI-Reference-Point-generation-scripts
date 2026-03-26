## si:CompoundQuantityKind

compound quantitykind

|  Predicate | Domain | Range | Comment |
|------------|--------|-------|---------|

## si:CompoundUnit

compound unit

|  Predicate | Domain | Range | Comment |
|------------|--------|-------|---------|

## si:Constant

defining constant

|  Predicate | Domain | Range | Comment |
|------------|--------|-------|---------|
| rdf:type |   |  |  |
| skos:hiddenLabel |   |  |  |
| skos:prefLabel |   |  |  |
| si:hasDatatype | si:Constant, si:SIPrefix |  |  |
| si:hasDatatype | si:Constant, si:SIPrefix |  |  |
| si:hasDefiningResolution | si:Definition, si:Constant | rb:Resolution | Linking an SI definition to the resolution by which it was adopted. |
| si:hasDefiningResolution | si:Definition, si:Constant | rb:Resolution | Linking an SI definition to the resolution by which it was adopted. |
| si:hasSymbol |   | xsd:string | Linking a measurement unit or prefix to a symbol. |
| si:hasUnit | si:Constant, si:QuantityKind | si:MeasurementUnit | Linking a measurement unit to an object. |
| si:hasUnit | si:Constant, si:QuantityKind | si:MeasurementUnit | Linking a measurement unit to an object. |
| si:hasUpdatedDate | si:Constant | xsd:date |  |
| si:hasValue | si:Constant | rdfs:Literal |  |
| si:hasValueAsString | si:Constant | xsd:string |  |

## si:Definition

definition of a base unit

|  Predicate | Domain | Range | Comment |
|------------|--------|-------|---------|
| rdf:type |   |  |  |
| skos:prefLabel |   |  |  |
| si:hasDefiningConstant | si:Definition | si:Constant | Linking a definition to its defining constant. |
| si:hasDefiningEquation | si:Definition, si:Constant | rdfs:Literal | Linking a SI definition to its defining equation. |
| si:hasDefiningEquation | si:Definition, si:Constant | rdfs:Literal | Linking a SI definition to its defining equation. |
| si:hasDefiningResolution | si:Definition, si:Constant | rb:Resolution | Linking an SI definition to the resolution by which it was adopted. |
| si:hasDefiningResolution | si:Definition, si:Constant | rb:Resolution | Linking an SI definition to the resolution by which it was adopted. |
| si:hasDefiningText | si:Definition | rdfs:Literal | Linking an SI definition to the defining text. |
| si:hasDefinitionNote | si:Definition | si:DefinitionNote | Linking an SI definition to a definition note. |
| si:hasEndValidity | si:Definition | xsd:date | Linking an SI definition to its ending validity date. |
| si:hasNextDefinition | si:Definition | si:Definition | Linking an SI definition version to the next version. |
| si:hasPreviousDefinition | si:Definition | si:Definition | Linking an SI definition version to the previous version. |
| si:hasStartValidity | si:Definition | xsd:date | Linking an SI definition to its starting validity date. |
| si:hasStatus | si:Definition | rdfs:Literal | Linking a SI definition to its status. |
| si:prefixRestriction | si:SIBaseUnit, si:SISpecialNamedUnit, si:nonSIUnit, si:MeasurementUnit | xsd:boolean |  |
| si:prefixRestriction | si:SIBaseUnit, si:SISpecialNamedUnit, si:nonSIUnit, si:MeasurementUnit | xsd:boolean |  |

## si:Definition

definition of a base unit

|  Predicate | Domain | Range | Comment |
|------------|--------|-------|---------|
| rdf:type |   |  |  |
| skos:prefLabel |   |  |  |
| si:hasDefiningConstant | si:Definition | si:Constant | Linking a definition to its defining constant. |
| si:hasDefiningEquation | si:Definition, si:Constant | rdfs:Literal | Linking a SI definition to its defining equation. |
| si:hasDefiningEquation | si:Definition, si:Constant | rdfs:Literal | Linking a SI definition to its defining equation. |
| si:hasDefiningResolution | si:Definition, si:Constant | rb:Resolution | Linking an SI definition to the resolution by which it was adopted. |
| si:hasDefiningResolution | si:Definition, si:Constant | rb:Resolution | Linking an SI definition to the resolution by which it was adopted. |
| si:hasDefiningText | si:Definition | rdfs:Literal | Linking an SI definition to the defining text. |
| si:hasDefinitionNote | si:Definition | si:DefinitionNote | Linking an SI definition to a definition note. |
| si:hasEndValidity | si:Definition | xsd:date | Linking an SI definition to its ending validity date. |
| si:hasNextDefinition | si:Definition | si:Definition | Linking an SI definition version to the next version. |
| si:hasPreviousDefinition | si:Definition | si:Definition | Linking an SI definition version to the previous version. |
| si:hasStartValidity | si:Definition | xsd:date | Linking an SI definition to its starting validity date. |
| si:hasStatus | si:Definition | rdfs:Literal | Linking a SI definition to its status. |
| si:prefixRestriction | si:SIBaseUnit, si:SISpecialNamedUnit, si:nonSIUnit, si:MeasurementUnit | xsd:boolean |  |
| si:prefixRestriction | si:SIBaseUnit, si:SISpecialNamedUnit, si:nonSIUnit, si:MeasurementUnit | xsd:boolean |  |

## si:DefinitionNote

unit definition note

|  Predicate | Domain | Range | Comment |
|------------|--------|-------|---------|
| rdf:type |   |  |  |
| si:hasNoteIndex | si:DefinitionNote | rdfs:Literal | The text of a definition note. |
| si:hasNoteText | si:DefinitionNote | rdfs:Literal | The order index of a definition note. |

## si:MeasurementUnit

measurement unit

|  Predicate | Domain | Range | Comment |
|------------|--------|-------|---------|
| rdf:type |   |  |  |
| skos:prefLabel |   |  |  |
| si:hasSymbol |   | xsd:string | Linking a measurement unit or prefix to a symbol. |
| si:isUnitOfQtyKind | si:MeasurementUnit | si:QuantityKind | Linking a measurement unit to its quantity kind. |
| si:prefixRestriction | si:SIBaseUnit, si:SISpecialNamedUnit, si:nonSIUnit, si:MeasurementUnit | xsd:boolean |  |
| si:prefixRestriction | si:SIBaseUnit, si:SISpecialNamedUnit, si:nonSIUnit, si:MeasurementUnit | xsd:boolean |  |

## si:PrefixedUnit

prefixed unit

|  Predicate | Domain | Range | Comment |
|------------|--------|-------|---------|
| rdf:type |   |  |  |
| skos:prefLabel |   |  |  |
| si:hasDefinition | si:SIBaseUnit | si:Definition | Linking an SI base unit to its definition. |
| si:hasNonPrefixedUnit | si:PrefixedUnit | si:MeasurementUnit |  |
| si:hasPrefix | si:PrefixedUnit | si:SIPrefix |  |
| si:hasSymbol |   | xsd:string | Linking a measurement unit or prefix to a symbol. |
| si:hasUnitTypeAsString | si:SIBaseUnit, si:SISpecialNamedUnit, si:nonSIUnit, si:MeasurementUnit | rdfs:Literal |  |
| si:hasUnitTypeAsString | si:SIBaseUnit, si:SISpecialNamedUnit, si:nonSIUnit, si:MeasurementUnit | rdfs:Literal |  |
| si:isUnitOfQtyKind | si:MeasurementUnit | si:QuantityKind | Linking a measurement unit to its quantity kind. |

## si:QuantityKind

kind of quantity

|  Predicate | Domain | Range | Comment |
|------------|--------|-------|---------|
| rdf:type |   |  |  |
| skos:altLabel |   |  |  |
| skos:prefLabel |   |  |  |
| si:hasUnit | si:Constant, si:QuantityKind | si:MeasurementUnit | Linking a measurement unit to an object. |
| si:hasUnit | si:Constant, si:QuantityKind | si:MeasurementUnit | Linking a measurement unit to an object. |

## si:QuantityKindPower

quantitykind power

|  Predicate | Domain | Range | Comment |
|------------|--------|-------|---------|

## si:QuantityKindProduct

quantitykind product

|  Predicate | Domain | Range | Comment |
|------------|--------|-------|---------|

## si:SIBaseUnit

base unit

|  Predicate | Domain | Range | Comment |
|------------|--------|-------|---------|
| rdf:type |   |  |  |
| skos:prefLabel |   |  |  |
| si:hasDefinition | si:SIBaseUnit | si:Definition | Linking an SI base unit to its definition. |
| si:hasNonPrefixedUnit | si:PrefixedUnit | si:MeasurementUnit |  |
| si:hasPrefix | si:PrefixedUnit | si:SIPrefix |  |
| si:hasSymbol |   | xsd:string | Linking a measurement unit or prefix to a symbol. |
| si:hasUnitTypeAsString | si:SIBaseUnit, si:SISpecialNamedUnit, si:nonSIUnit, si:MeasurementUnit | rdfs:Literal |  |
| si:hasUnitTypeAsString | si:SIBaseUnit, si:SISpecialNamedUnit, si:nonSIUnit, si:MeasurementUnit | rdfs:Literal |  |
| si:isUnitOfQtyKind | si:MeasurementUnit | si:QuantityKind | Linking a measurement unit to its quantity kind. |

## si:SIDecision

SI Decision

|  Predicate | Domain | Range | Comment |
|------------|--------|-------|---------|
| rdf:type |   |  |  |
| rdfs:label |   |  |  |
| skos:related |   |  |  |
| si:correspondingResolution | si:SIDecision | rb:Resolution |  |
| si:isDecisionOf | si:SIDecision | si:SIDecisionTarget |  |

## si:SIDecisionTarget

SI Decision target

|  Predicate | Domain | Range | Comment |
|------------|--------|-------|---------|
| rdf:type |   |  |  |
| rdfs:label |   |  |  |
| si:hasDecision | si:SIDecisionTarget | si:SIDecision |  |
| si:isTargetOf | si:SIDecisionTarget | si:SIDecisionScope |  |

## si:SIPrefix

SI prefix

|  Predicate | Domain | Range | Comment |
|------------|--------|-------|---------|
| rdf:type |   |  |  |
| skos:prefLabel |   |  |  |
| si:hasDatatype | si:Constant, si:SIPrefix |  |  |
| si:hasDatatype | si:Constant, si:SIPrefix |  |  |
| si:hasDefiningResolution | si:Definition, si:Constant | rb:Resolution | Linking an SI definition to the resolution by which it was adopted. |
| si:hasDefiningResolution | si:Definition, si:Constant | rb:Resolution | Linking an SI definition to the resolution by which it was adopted. |
| si:hasNumericExponent | si:UnitPower | xsd:short |  |
| si:hasScalingFactor | si:SIPrefix | rdfs:Literal | Linking an SI prefix to its scaling factor. |
| si:hasSymbol |   | xsd:string | Linking a measurement unit or prefix to a symbol. |

## si:SIPrefix

SI prefix

|  Predicate | Domain | Range | Comment |
|------------|--------|-------|---------|
| rdf:type |   |  |  |
| skos:prefLabel |   |  |  |
| si:hasDatatype | si:Constant, si:SIPrefix |  |  |
| si:hasDatatype | si:Constant, si:SIPrefix |  |  |
| si:hasDefiningResolution | si:Definition, si:Constant | rb:Resolution | Linking an SI definition to the resolution by which it was adopted. |
| si:hasDefiningResolution | si:Definition, si:Constant | rb:Resolution | Linking an SI definition to the resolution by which it was adopted. |
| si:hasNumericExponent | si:UnitPower | xsd:short |  |
| si:hasScalingFactor | si:SIPrefix | rdfs:Literal | Linking an SI prefix to its scaling factor. |
| si:hasSymbol |   | xsd:string | Linking a measurement unit or prefix to a symbol. |

## si:SISpecialNamedUnit

SI unit with special name

|  Predicate | Domain | Range | Comment |
|------------|--------|-------|---------|
| rdf:type |   |  |  |
| skos:prefLabel |   |  |  |
| si:hasDefiningResolution | si:Definition, si:Constant | rb:Resolution | Linking an SI definition to the resolution by which it was adopted. |
| si:hasDefiningResolution | si:Definition, si:Constant | rb:Resolution | Linking an SI definition to the resolution by which it was adopted. |
| si:hasSymbol |   | xsd:string | Linking a measurement unit or prefix to a symbol. |
| si:hasUnitTypeAsString | si:SIBaseUnit, si:SISpecialNamedUnit, si:nonSIUnit, si:MeasurementUnit | rdfs:Literal |  |
| si:hasUnitTypeAsString | si:SIBaseUnit, si:SISpecialNamedUnit, si:nonSIUnit, si:MeasurementUnit | rdfs:Literal |  |
| si:inBaseSIUnits |   | si:MeasurementUnit |  |
| si:inOtherSIUnits |   | si:MeasurementUnit |  |
| si:isUnitOfQtyKind | si:MeasurementUnit | si:QuantityKind | Linking a measurement unit to its quantity kind. |
| si:prefixRestriction | si:SIBaseUnit, si:SISpecialNamedUnit, si:nonSIUnit, si:MeasurementUnit | xsd:boolean |  |
| si:prefixRestriction | si:SIBaseUnit, si:SISpecialNamedUnit, si:nonSIUnit, si:MeasurementUnit | xsd:boolean |  |

## si:UnitMultiple

unit multiple

|  Predicate | Domain | Range | Comment |
|------------|--------|-------|---------|
| rdf:type |   |  |  |
| si:hasNumericFactor | si:UnitMultiple |  |  |
| si:hasNumericFactorAsString | si:UnitMultiple | xsd:string |  |
| si:hasUnitTerm | si:UnitProduct, si:UnitMultiple | si:MeasurementUnit |  |
| si:hasUnitTerm | si:UnitProduct, si:UnitMultiple | si:MeasurementUnit |  |

## si:UnitPower

unit power

|  Predicate | Domain | Range | Comment |
|------------|--------|-------|---------|
| rdf:type |   |  |  |
| si:hasNumericExponent | si:UnitPower | xsd:short |  |
| si:hasUnitBase | si:UnitPower | si:MeasurementUnit |  |

## si:UnitProduct

unit product

|  Predicate | Domain | Range | Comment |
|------------|--------|-------|---------|
| rdf:type |   |  |  |
| si:hasLeftUnitTerm | si:UnitProduct | si:MeasurementUnit |  |
| si:hasRightUnitTerm | si:UnitProduct | si:MeasurementUnit |  |

## si:nonSIUnit

non SI unit

|  Predicate | Domain | Range | Comment |
|------------|--------|-------|---------|
| rdf:type |   |  |  |
| skos:prefLabel |   |  |  |
| si:hasAltSymbol |   | xsd:string | Linking a measurement unit or prefix to an alternate symbol. |
| si:hasSymbol |   | xsd:string | Linking a measurement unit or prefix to a symbol. |
| si:hasUnitTypeAsString | si:SIBaseUnit, si:SISpecialNamedUnit, si:nonSIUnit, si:MeasurementUnit | rdfs:Literal |  |
| si:hasUnitTypeAsString | si:SIBaseUnit, si:SISpecialNamedUnit, si:nonSIUnit, si:MeasurementUnit | rdfs:Literal |  |
| si:inOtherSIUnits |   | si:MeasurementUnit |  |
| si:isUnitOfQtyKind | si:MeasurementUnit | si:QuantityKind | Linking a measurement unit to its quantity kind. |
| si:prefixRestriction | si:SIBaseUnit, si:SISpecialNamedUnit, si:nonSIUnit, si:MeasurementUnit | xsd:boolean |  |
| si:prefixRestriction | si:SIBaseUnit, si:SISpecialNamedUnit, si:nonSIUnit, si:MeasurementUnit | xsd:boolean |  |

