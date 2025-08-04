using System;
using cAlgo.API;

namespace cAlgo.Indicators;

[Indicator(AccessRights = AccessRights.None, IsOverlay = true)]
public partial class ParameterAttributeSample : Indicator
{
    [Parameter("Double Parameter", DefaultValue = 0.0, MinValue = 0, MaxValue = 10, Step = 1, Group = "Numeric Group")]
    public double DoubleParameter { get; set; }

    [Parameter("Int Parameter", DefaultValue = 0.0, MinValue = 0, MaxValue = 100, Step = 1, Group = "Numeric Group")]
    public int IntParameter { get; set; }

    [Parameter("Bool Parameter", DefaultValue = true, Group = "Bool Group")]
    public bool BoolParameter { get; set; }
    
    [Parameter("String Parameter", DefaultValue = "Default value", Group = "String Group")]
    public string StringParameter { get; set; }

    [Parameter("TradeType Parameter", DefaultValue = TradeType.Buy, Group = "Enum Group")]
    public TradeType TradeTypeParameter { get; set; }

    [Parameter("Second Parameter", DefaultValue = CustomEnum.Second, Group = "Enum Group")]
    public CustomEnum CustomEnumParameter { get; set; }
    
    [Parameter("Color Parameter", DefaultValue = "#3798c4", Group = "Color Group")]
    public Color ColorParameter { get; set; }
    
    [Parameter("DataSeries Parameter", Group = "DataSeries Group")]
    public DataSeries DataSeriesParameter { get; set; }
    
    [Parameter("TimeFrame Parameter", DefaultValue = "Daily", Group = "TimeFrame Group")]
    public TimeFrame TimeFrameParameter { get; set; }
}

public enum CustomEnum
{
    First,
    Second
}
