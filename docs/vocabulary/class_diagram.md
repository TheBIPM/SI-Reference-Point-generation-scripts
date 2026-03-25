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
	}
	class `si:Definition`{
	}
	class `si:DefinitionNote`{
	}
	class `si:MeasurementUnit`{
	}
	class `si:PrefixedUnit`{
	}
	class `si:QuantityKind`{
	}
	class `si:QuantityKindPower`{
	}
	class `si:QuantityKindProduct`{
	}
	class `si:SIBaseUnit`{
	}
	class `si:SIDecision`{
	}
	class `si:SIDecisionTarget`{
	}
	class `si:SIPrefix`{
	}
	class `si:SISpecialNamedUnit`{
	}
	class `si:UnitMultiple`{
	}
	class `si:UnitPower`{
	}
	class `si:UnitProduct`{
	}
	class `si:nonSIUnit`{
	}
