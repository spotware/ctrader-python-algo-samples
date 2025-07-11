using cAlgo.API;

namespace cAlgo.Robots;

[Robot(AccessRights = AccessRights.None, AddIndicators = true)]
public partial class AlligatorSample : Robot
{
    [Parameter("Volume (Lots)", DefaultValue = 0.01)]
    public double VolumeInLots { get; set; }

    [Parameter("Stop Loss (Pips)", DefaultValue = 10, MaxValue = 100, MinValue = 1, Step = 1)]
    public double StopLossInPips { get; set; }

    [Parameter("Take Profit (Pips)", DefaultValue = 10, MaxValue = 100, MinValue = 1, Step = 1)]
    public double TakeProfitInPips { get; set; }

    [Parameter("Label", DefaultValue = "AlligatorSample")]
    public string Label { get; set; }

    [Parameter("Jaws Periods", DefaultValue = 13, Group = "Alligator", MinValue = 1)]
    public int JawsPeriods { get; set; }

    [Parameter("Jaws Shift", DefaultValue = 18, Group = "Alligator", MinValue = 0, MaxValue = 1000)]
    public int JawsShift { get; set; }

    [Parameter("Teeth Periods", DefaultValue = 8, Group = "Alligator", MinValue = 1)]
    public int TeethPeriods { get; set; }

    [Parameter("Teeth Shift", DefaultValue = 5, Group = "Alligator", MinValue = 0, MaxValue = 1000)]
    public int TeethShift { get; set; }

    [Parameter("Lips Periods", DefaultValue = 5, Group = "Alligator", MinValue = 1)]
    public int LipsPeriods { get; set; }

    [Parameter("Lips Shift", DefaultValue = 3, Group = "Alligator", MinValue = 0, MaxValue = 1000)]
    public int LipsShift { get; set; }
}