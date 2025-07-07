def execute_market_order(trade_side, symbol_name, volume, label=None, stop_loss_pips=None, take_profit_pips=None, comment=None, has_trailing_stop=False, stop_loss_trigger_method=None):
    """
    Execute a Market Order
    
    Args:
        trade_side: Direction of trade
        symbol_name: Symbol name of trade
        volume: Volume (in units) of trade
        label: Representing label (optional)
        stop_loss_pips: Stop loss in pips (optional)
        take_profit_pips: Take profit in pips (optional)
        comment: Order comment (optional)
        has_trailing_stop: Enable/disable TrailingStop for position (default: False)
        stop_loss_trigger_method: Trigger method for position's StopLoss (optional)
        
    Returns:
        Trade Result
        
    Examples:
        execute_market_order(TradeType.Buy, symbol.Name, 10000)
        execute_market_order(TradeType.Sell, symbol.Name, 10000, "myLabel")
        execute_market_order(TradeType.Buy, symbol.Name, 10000, "myLabel", 10, 20)
        execute_market_order(TradeType.Buy, symbol.Name, 5000, "myLabel", 10, 20, "my comment")
    """
    if stop_loss_trigger_method is not None:
        return api.ExecuteMarketOrder(trade_side, symbol_name, volume, label, stop_loss_pips, take_profit_pips, comment, has_trailing_stop, stop_loss_trigger_method)
    elif has_trailing_stop:
        return api.ExecuteMarketOrder(trade_side, symbol_name, volume, label, stop_loss_pips, take_profit_pips, comment, has_trailing_stop)
    elif comment is not None:
        return api.ExecuteMarketOrder(trade_side, symbol_name, volume, label, stop_loss_pips, take_profit_pips, comment)
    elif stop_loss_pips is not None or take_profit_pips is not None:
        return api.ExecuteMarketOrder(trade_side, symbol_name, volume, label, stop_loss_pips, take_profit_pips)
    elif label is not None:
        return api.ExecuteMarketOrder(trade_side, symbol_name, volume, label)
    else:
        return api.ExecuteMarketOrder(trade_side, symbol_name, volume)


def close_position(position, volume=None):
    """
    Close a position
    
    Args:
        position: Position to close
        volume: Volume which is closed (optional, closes full position if not specified)
        
    Returns:
        Trade Result
        
    Examples:
        close_position(position)
        close_position(position, 10000)
    """
    if volume is None:
        return api.ClosePosition(position)
    else:
        return api.ClosePosition(position, volume)


def modify_position(position, volume=None, stop_loss=None, take_profit=None, has_trailing_stop=None, stop_loss_trigger_method=None):
    """
    Modify a position's volume or protection parameters
    
    Args:
        position: Position which is affected
        volume: New volume (in units) for the position (optional)
        stop_loss: New stop loss price (optional)
        take_profit: New take profit price (optional)
        has_trailing_stop: Enable/disable TrailingStop for position (optional)
        stop_loss_trigger_method: Trigger method for position's StopLoss (optional)
        
    Returns:
        Trade Result
        
    Examples:
        # Change position volume
        modify_position(position, volume=20000)
        
        # Update stop loss and take profit
        modify_position(position, stop_loss=1.2340, take_profit=1.2560)
        
        # Enable trailing stop
        modify_position(position, stop_loss=1.2340, take_profit=1.2560, has_trailing_stop=True)
    """
    # Case 1: Modify volume only
    if volume is not None and stop_loss is None and take_profit is None:
        return api.ModifyPosition(position, volume)
    
    # Case 2: Modify stop loss and/or take profit with optional trailing stop and trigger
    if stop_loss_trigger_method is not None:
        return api.ModifyPosition(position, stop_loss, take_profit, has_trailing_stop, stop_loss_trigger_method)
    elif has_trailing_stop is not None:
        return api.ModifyPosition(position, stop_loss, take_profit, has_trailing_stop)
    elif stop_loss is not None or take_profit is not None:
        return api.ModifyPosition(position, stop_loss, take_profit)
    
    # Default case if no parameters were provided
    return None


def place_stop_order(trade_side, symbol_name, volume, target_price, label=None, stop_loss=None, take_profit=None, expiration=None, comment=None, has_trailing_stop=False, stop_loss_trigger_method=None, stop_order_trigger_method=None):
    """
    Place a stop order
    
    Args:
        trade_side: Direction of trade
        symbol_name: Symbol name of trade
        volume: Volume (in units) of trade
        target_price: Price at which order becomes a market order
        label: Representing label (optional)
        stop_loss: Stop loss price (optional)
        take_profit: Take profit price (optional)
        expiration: Order expiry time (optional)
        comment: Order comment (optional)
        has_trailing_stop: Enable/disable TrailingStop for position (default: False)
        stop_loss_trigger_method: Trigger method for position's StopLoss (optional)
        stop_order_trigger_method: Trigger method for the stop order (optional)
        
    Returns:
        Trade Result
        
    Examples:
        # Basic stop order
        place_stop_order(TradeType.Buy, symbol.Name, 10000, 1.2450)
        
        # Stop order with label
        place_stop_order(TradeType.Sell, symbol.Name, 20000, symbol.Ask, "myStopOrder")
        
        # Stop order with protection
        place_stop_order(TradeType.Buy, symbol.Name, 10000, 1.2450, "myStopOrder", 1.2400, 1.2500)
    """
    # Handle different combinations of parameters
    if stop_order_trigger_method is not None:
        return api.PlaceStopOrder(trade_side, symbol_name, volume, target_price, label, 
                               stop_loss, take_profit, None, expiration, 
                               comment, has_trailing_stop, stop_loss_trigger_method, stop_order_trigger_method)
    elif stop_loss_trigger_method is not None:
        return api.PlaceStopOrder(trade_side, symbol_name, volume, target_price, label, 
                               stop_loss, take_profit, None, expiration, 
                               comment, has_trailing_stop, stop_loss_trigger_method)
    elif comment is not None or has_trailing_stop:
        return api.PlaceStopOrder(trade_side, symbol_name, volume, target_price, label, 
                               stop_loss, take_profit, None, expiration, comment, has_trailing_stop)
    elif expiration is not None:
        return api.PlaceStopOrder(trade_side, symbol_name, volume, target_price, label, 
                               stop_loss, take_profit, None, expiration)
    elif stop_loss is not None or take_profit is not None:
        return api.PlaceStopOrder(trade_side, symbol_name, volume, target_price, label, 
                               stop_loss, take_profit, None)
    elif label is not None:
        return api.PlaceStopOrder(trade_side, symbol_name, volume, target_price, label)
    else:
        return api.PlaceStopOrder(trade_side, symbol_name, volume, target_price)


def place_limit_order(trade_side, symbol_name, volume, target_price, label=None, stop_loss=None, take_profit=None, expiration=None, comment=None, has_trailing_stop=False, stop_loss_trigger_method=None):
    """
    Place a limit order
    
    Args:
        trade_side: Direction of trade
        symbol_name: Symbol name of trade
        volume: Volume (in units) of trade
        target_price: Price (or better) at which order is filled
        label: Label representing the order (optional)
        stop_loss: Stop loss price (optional)
        take_profit: Take profit price (optional)
        expiration: Order expiry time (optional)
        comment: Order comment (optional)
        has_trailing_stop: Enable/disable TrailingStop for position (default: False)
        stop_loss_trigger_method: Trigger method for position's StopLoss (optional)
        
    Returns:
        Trade Result
        
    Examples:
        # Basic limit order
        place_limit_order(TradeType.Buy, symbol.Name, 10000, symbol.Bid - 10 * symbol.PipSize)
        
        # Limit order with label
        place_limit_order(TradeType.Buy, symbol.Name, 10000, symbol.Bid - 5 * symbol.PipSize, "myLimitOrder")
        
        # Limit order with protection
        place_limit_order(TradeType.Sell, symbol.Name, 20000, symbol.Ask + 10 * symbol.PipSize, 
                       "myLimitOrder", symbol.Ask - 20 * symbol.PipSize, symbol.Ask + 30 * symbol.PipSize)
                       
        # Limit order with expiration
        expiry = DateTime.Now.AddHours(1)
        place_limit_order(TradeType.Buy, symbol.Name, 10000, symbol.Bid - 10 * symbol.PipSize,
                       "myLimitOrder", 10, 10, expiry)
    """
    # Handle different combinations of parameters
    if stop_loss_trigger_method is not None:
        return api.PlaceLimitOrder(trade_side, symbol_name, volume, target_price, label, 
                               stop_loss, take_profit, None, expiration, 
                               comment, has_trailing_stop, stop_loss_trigger_method)
    elif comment is not None or has_trailing_stop:
        return api.PlaceLimitOrder(trade_side, symbol_name, volume, target_price, label, 
                               stop_loss, take_profit, None, expiration, 
                               comment, has_trailing_stop)
    elif expiration is not None:
        return api.PlaceLimitOrder(trade_side, symbol_name, volume, target_price, label, 
                               stop_loss, take_profit, None, expiration)
    elif stop_loss is not None or take_profit is not None:
        return api.PlaceLimitOrder(trade_side, symbol_name, volume, target_price, label, 
                               stop_loss, take_profit, None)
    elif label is not None:
        return api.PlaceLimitOrder(trade_side, symbol_name, volume, target_price, label)
    else:
        return api.PlaceLimitOrder(trade_side, symbol_name, volume, target_price)
