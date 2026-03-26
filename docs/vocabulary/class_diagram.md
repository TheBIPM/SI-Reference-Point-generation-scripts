classDiagram
	`si:QuantityKind`<|--`si:CompoundQuantityKind`
	`si:MeasurementUnit`<|--`si:CompoundUnit`
	`si:CompoundUnit`<|--`si:PrefixedUnit`
	`si:CompoundQuantityKind`<|--`si:QuantityKindPower`
	`si:CompoundQuantityKind`<|--`si:QuantityKindProduct`
	`si:MeasurementUnit`<|--`si:SIBaseUnit`
	`si:MeasurementUnit`<|--`si:SISpecialNamedUnit`
	`si:CompoundUnit`<|--`si:UnitMultiple`
	`si:CompoundUnit`<|--`si:UnitPower`
	`si:CompoundUnit`<|--`si:UnitProduct`
	`si:MeasurementUnit`<|--`si:nonSIUnit`
	class `si:CompoundQuantityKind`{
	}
	class `si:CompoundUnit`{
	}
	class `si:Constant`{
		+si:hasDatatype
		+si:hasDefiningResolution
		+si:hasUnit
		+si:hasUpdatedDate
		+si:hasValue
		+si:hasValueAsString
		+si:hasDefiningEquation
	}
	class `si:Definition`{
		+si:hasDefiningResolution
		+si:hasDefiningConstant
		+si:hasDefiningEquation
		+si:hasDefiningText
		+si:hasDefinitionNote
		+si:hasEndValidity
		+si:hasNextDefinition
		+si:hasPreviousDefinition
		+si:hasStartValidity
		+si:hasStatus
	}
	class `si:DefinitionNote`{
		+si:hasNoteIndex
		+si:hasNoteText
	}
	class `si:MeasurementUnit`{
		+si:prefixRestriction
		+si:isUnitOfQtyKind
		+si:hasUnitTypeAsString
	}
	class `si:PrefixedUnit`{
		+si:hasNonPrefixedUnit
		+si:hasPrefix
	}
	class `si:QuantityKind`{
		+si:hasUnit
	}
	class `si:QuantityKindPower`{
	}
	class `si:QuantityKindProduct`{
	}
	class `si:SIBaseUnit`{
		+si:prefixRestriction
		+si:hasDefinition
		+si:hasUnitTypeAsString
	}
	class `si:SIDecision`{
		+si:correspondingResolution
		+si:isDecisionOf
	}
	class `si:SIDecisionTarget`{
		+si:hasDecision
		+si:isTargetOf
	}
	class `si:SIPrefix`{
		+si:hasDatatype
		+si:hasScalingFactor
	}
	class `si:SISpecialNamedUnit`{
		+si:prefixRestriction
		+si:hasUnitTypeAsString
	}
	class `si:UnitMultiple`{
		+si:hasNumericFactor
		+si:hasNumericFactorAsString
		+si:hasUnitTerm
	}
	class `si:UnitPower`{
		+si:hasNumericExponent
		+si:hasUnitBase
	}
	class `si:UnitProduct`{
		+si:hasUnitTerm
		+si:hasLeftUnitTerm
		+si:hasRightUnitTerm
	}
	class `si:nonSIUnit`{
		+si:prefixRestriction
		+si:hasUnitTypeAsString
	}
	`si:Constant` --o `rb:Resolution`
	`si:Constant` --o `si:MeasurementUnit`
	`si:Constant` --o `xsd:date`
	`si:Constant` --o `rdfs:Literal`
	`si:Constant` --o `xsd:string`
	`si:Definition` --o `rb:Resolution`
	`si:Definition` --o `si:Constant`
	`si:Definition` --o `rdfs:Literal`
	`si:Definition` --o `si:DefinitionNote`
	`si:Definition` --o `xsd:date`
	`si:Definition` --o `si:Definition`
	`si:DefinitionNote` --o `rdfs:Literal`
	`si:MeasurementUnit` --o `xsd:boolean`
	`si:MeasurementUnit` --o `si:QuantityKind`
	`si:MeasurementUnit` --o `rdfs:Literal`
	`si:PrefixedUnit` --o `si:MeasurementUnit`
	`si:PrefixedUnit` --o `si:SIPrefix`
	`si:QuantityKind` --o `si:MeasurementUnit`
	`si:SIBaseUnit` --o `xsd:boolean`
	`si:SIBaseUnit` --o `si:Definition`
	`si:SIBaseUnit` --o `rdfs:Literal`
	`si:SIDecision` --o `rb:Resolution`
	`si:SIDecision` --o `si:SIDecisionTarget`
	`si:SIDecisionTarget` --o `si:SIDecision`
	`si:SIDecisionTarget` --o `si:SIDecisionScope`
	`si:SIPrefix` --o `rdfs:Literal`
	`si:SISpecialNamedUnit` --o `xsd:boolean`
	`si:SISpecialNamedUnit` --o `rdfs:Literal`
	`si:UnitMultiple` --o `xsd:string`
	`si:UnitMultiple` --o `si:MeasurementUnit`
	`si:UnitPower` --o `xsd:short`
	`si:UnitPower` --o `si:MeasurementUnit`
	`si:UnitProduct` --o `si:MeasurementUnit`
	`si:nonSIUnit` --o `xsd:boolean`
	`si:nonSIUnit` --o `rdfs:Literal`
