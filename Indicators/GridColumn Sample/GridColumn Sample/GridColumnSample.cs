using System;
using cAlgo.API;

namespace cAlgo.Indicators;

[Indicator(AccessRights = AccessRights.None, IsOverlay = true)]
public partial class GridColumnSample : Indicator
{
    [Parameter("Grid Columns #", DefaultValue = 2)]
    public int GridColumnsNumber { get; set; }

    [Parameter("Grid Column Length", DefaultValue = 2)]
    public int GridColumnLength { get; set; }

    [Parameter("Grid Column Length Unit Type", DefaultValue = GridUnitType.Auto)]
    public GridUnitType GridColumnLengthUnitType { get; set; }
}
