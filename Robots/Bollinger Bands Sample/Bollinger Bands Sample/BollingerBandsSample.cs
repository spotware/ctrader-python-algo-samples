using cAlgo.API;

namespace cAlgo.Robots;

[Robot(AccessRights = AccessRights.None, AddIndicators = true)]
public partial class BollingerBandsSample : Robot
{
    [Parameter("Volume (Lots)", DefaultValue = 0.01)]
    public double VolumeInLots { get; set; }

    [Parameter("Label", DefaultValue = "BollingerBandsSample")]
    public string Label { get; set; }

    [Parameter("Source", Group = "Bollinger Bands")]
    public DataSeries Source { get; set; }

    [Parameter(DefaultValue = 20, Group = "Bollinger Bands", MinValue = 1)]
    public int Periods { get; set; }

    [Parameter("Standard Dev", DefaultValue = 2.0, Group = "Bollinger Bands", MinValue = 0.0001, MaxValue = 10)]
    public double StandardDeviations { get; set; }

    [Parameter("MA Type", DefaultValue = MovingAverageType.Simple, Group = "Bollinger Bands")]
    public MovingAverageType MaType { get; set; }

    [Parameter("Shift", DefaultValue = 0, Group = "Bollinger Bands", MinValue = -1000, MaxValue = 1000)]
    public int Shift { get; set; }
}