import pandas as pd

def analyze_behavior(df):

    results = {}
    # OVERTRADING

    total_trades = len(df)

    if total_trades > 15:
        results["overtrading"] = {
            "status": True,
            "message": f"You took {total_trades} trades. Possible overtrading detected."
        }
    else:
        results["overtrading"] = {
            "status": False,
            "message": "Trading frequency looks healthy."
        }


    # HOLDING LOSERS TOO LONG
    if "Profit" in df.columns and "HoldingHours" in df.columns:

        winning_trades = df[df["Profit"] > 0]
        losing_trades = df[df["Profit"] < 0]

        if len(winning_trades) > 0 and len(losing_trades) > 0:

            avg_win_hold = winning_trades["HoldingHours"].mean()
            avg_loss_hold = losing_trades["HoldingHours"].mean()

            if avg_loss_hold > avg_win_hold:

                results["holding_losers"] = {
                    "status": True,
                    "message": (
                        f"Losing trades held {avg_loss_hold:.1f} hrs "
                        f"vs winners {avg_win_hold:.1f} hrs."
                    )
                }

            else:

                results["holding_losers"] = {
                    "status": False,
                    "message": "Holding behavior looks balanced."
                }

    # CUTTING WINNERS EARLY
    
    if "Profit" in df.columns:

        avg_win = df[df["Profit"] > 0]["Profit"].mean()
        avg_loss = abs(df[df["Profit"] < 0]["Profit"].mean())

        if pd.notna(avg_win) and pd.notna(avg_loss):

            if avg_win < avg_loss:

                results["cutting_winners"] = {
                    "status": True,
                    "message": (
                        "Winning trades are smaller than losing trades."
                    )
                }

            else:

                results["cutting_winners"] = {
                    "status": False,
                    "message": "Profit capture looks healthy."
                }

    return results