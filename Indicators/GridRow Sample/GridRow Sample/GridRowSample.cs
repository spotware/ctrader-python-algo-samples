using System;
using cAlgo.API;

namespace cAlgo.Indicators;

[Indicator(AccessRights = AccessRights.None, IsOverlay = true)]
public partial class GridRowSample : Indicator
{
    [Parameter("Grid Rows #", DefaultValue = 10)]
    public int GridRowsNumber { get; set; }

    [Parameter("Grid Row Length", DefaultValue = 2)]
    public int GridRowLength { get; set; }

    [Parameter("Grid Row Length Unit Type", DefaultValue = GridUnitType.Auto)]
    public GridUnitType GridRowLengthUnitType { get; set; }
}
