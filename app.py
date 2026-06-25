from flask import Flask, render_template, request
from behavior_analyzer import analyze_behavior
from health_score import calculate_health_score
import pandas as pd
import plotly.express as px

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():

    data = None
    total_profit = None
    win_rate = None
    best_stock = None
    worst_stock = None
    avg_holding = None
    coach_message = None
    behaviour_message = None
    sector_analysis = None
    best_sector = None
    worst_sector = None
    chat_response = None
    sector_chart = None
    best_strategy = None
    worst_strategy = None
    profit_factor = None
    strategy_chart = None
    previous_profit = None
    total_trades = None
    risk_rating = None
    improvement = None
    health_score = None
    behavior_results = {}

    if request.method == 'POST':

        file = request.files.get('file')
        question = request.form.get('question')

        if file:

            try:
                df = pd.read_csv(file)
                

            except Exception:

                return render_template(
                    "index.html",
                    chat_response="Invalid CSV uploaded."
            )
            
            
            required_columns = [
                "Stock",
                "Sector",
                "Strategy",
                "BuyPrice",
                "SellPrice",
                "Quantity",
                "HoldingHours"
            ]

            for col in required_columns:

                if col not in df.columns:

                    return render_template(
                        "index.html",
                        chat_response=f"Missing column: {col}"
                    )

            # Calculate profit
            df['Profit'] = (
                (df['SellPrice'] - df['BuyPrice'])
                * df['Quantity']
            )

            behavior_results = analyze_behavior(df)

            print("Behavior Results:", behavior_results)
            total_trades = len(df)
            # Total Profit
            total_profit = df['Profit'].sum()
            winning_profit = df[df['Profit'] > 0]['Profit'].sum()

            losing_profit = abs(
                df[df['Profit'] < 0]['Profit'].sum()
            )

            if losing_profit > 0:
                profit_factor = round(
                    winning_profit / losing_profit,
                    2
                )
            else:
                profit_factor = "Infinity"
            previous_profit = 1800

            improvement = round(
                ((total_profit - previous_profit) / previous_profit) * 100,
                2
            )

            # Win Rate
            win_rate = (
                (df['Profit'] > 0).mean()
            ) * 100
            
            if win_rate >= 70:
                risk_rating = "Low Risk ✅"

            elif win_rate >= 50:
                risk_rating = "Moderate Risk ⚠️"

            else:
                risk_rating = "High Risk 🔴"
            
            avg_holding = round(
                    df['HoldingHours'].mean(),
                    2
            ) 
            health_score = calculate_health_score(
                win_rate,
                avg_holding,
                profit_factor
            )
            print("Health Score:", health_score)
            
            # AI Coach Logic

            if win_rate < 50:

                coach_message = (
                    "Your win rate is below 50%. "
                    "Focus on fewer but higher-conviction trades."
            )

            elif avg_holding > 6:

                coach_message = (
                    "You are holding positions for too long. "
                    "Review stop-loss discipline."
            )

            else:

                coach_message = (
                    "Good trading discipline. "
                "Maintain your current approach and continue monitoring risk."
        )
                
            losing_trades = df[df['Profit'] < 0]
            winning_trades = df[df['Profit'] > 0]

            if len(losing_trades) > 0 and len(winning_trades) > 0:

                avg_loser_hold = losing_trades['HoldingHours'].mean()
                avg_winner_hold = winning_trades['HoldingHours'].mean()

            if avg_loser_hold > avg_winner_hold:

                behaviour_message = (
                    f"⚠ Holding losers too long. "
                    f"Losing trades held {avg_loser_hold:.1f} hrs "
                    f"vs winners {avg_winner_hold:.1f} hrs."
            )

            else:

                behaviour_message = (
                    "✅ Good exit discipline detected."
            )
            
            sector_profit = df.groupby('Sector')['Profit'].sum()

            best_sector_name = sector_profit.idxmax()
            best_sector_profit = sector_profit.max()

            worst_sector_name = sector_profit.idxmin()
            worst_sector_profit = sector_profit.min()

            best_sector = (
                f"{best_sector_name} "
                f"(₹{best_sector_profit})"
            )

            worst_sector = (
                f"{worst_sector_name} "
                f"(₹{worst_sector_profit})"
            )

            sector_analysis = sector_profit.to_dict()
            fig = px.bar(
                x=sector_profit.index,
                y=sector_profit.values,
                labels={
                    'x': 'Sector',
                    'y': 'Profit'
                },
                title='Profit by Sector'
            )

            sector_chart = fig.to_html(
                full_html=False
            )
            
            question = request.form.get('question')

            if question:

                if "lose" in question.lower():

                    chat_response = (
                        f"Most losses came from "
                        f"{worst_sector_name} sector. "
                        f"You are also holding losing trades "
                        f"longer than winning trades."
                    )

                elif "best" in question.lower():

                    chat_response = (
                        f"Your strongest sector is "
                        f"{best_sector_name}."
                    )

                else:

                    chat_response = (
                        "Review your risk management and "
                        "focus on sectors where you perform best."
                    )
                # Strategy Analysis

            strategy_profit = df.groupby('Strategy')['Profit'].sum()

            best_strategy_name = strategy_profit.idxmax()
            best_strategy_profit = strategy_profit.max()

            worst_strategy_name = strategy_profit.idxmin()
            worst_strategy_profit = strategy_profit.min()

            best_strategy = (
                f"{best_strategy_name} "
                f"(₹{best_strategy_profit})"
            )

            worst_strategy = (
                f"{worst_strategy_name} "
                f"(₹{worst_strategy_profit})"
            )
            fig2 = px.pie(
                values=strategy_profit.values,
                names=strategy_profit.index,
                title="Profit Distribution by Strategy"
            )

            strategy_chart = fig2.to_html(
                full_html=False
            )

            # Companion Chat

            if question:

                q = question.lower()

                if "lose" in q:

                    chat_response = (
                        f"Most losses came from {worst_sector_name} sector."
                    )

                elif "best sector" in q:

                    chat_response = (
                        f"Your best sector is {best_sector_name}."
                    )

                elif "best strategy" in q:

                    chat_response = (
                        f"Your best strategy is {best_strategy_name}."
                    )

                elif "improve" in q:

                    chat_response = (
                        "Reduce exposure to losing sectors and cut losing trades earlier."
                    )

                else:

                    chat_response = (
                        "Focus on profitable sectors and maintain discipline."
                    )
            # Best Stock
            best_row = df.loc[df['Profit'].idxmax()]
            best_stock = f"{best_row['Stock']} (₹{best_row['Profit']})"

            # Worst Stock
            worst_row = df.loc[df['Profit'].idxmin()]
            worst_stock = f"{worst_row['Stock']} (₹{worst_row['Profit']})"

            # Table
            data = df.to_html(
                classes='table table-striped',
                index=False
            )

    return render_template(
        "index.html",
        data=data,
        total_profit=round(total_profit, 2) if total_profit is not None else None,
        win_rate=round(win_rate, 2) if win_rate is not None else None,
        best_stock=best_stock,
        worst_stock=worst_stock,
        avg_holding=avg_holding,
        coach_message=coach_message,
        behaviour_message=behaviour_message,
        sector_analysis=sector_analysis,
        best_sector=best_sector,
        worst_sector=worst_sector,
        chat_response=chat_response,
        sector_chart=sector_chart,
        best_strategy=best_strategy,
        worst_strategy=worst_strategy,
        improvement=improvement,
        profit_factor=profit_factor,
        strategy_chart=strategy_chart,
        total_trades=total_trades,
        risk_rating=risk_rating,
        previous_profit=previous_profit,
        behavior_results=behavior_results,
        health_score=health_score,
    )

if __name__ == "__main__":
    app.run(debug=True)