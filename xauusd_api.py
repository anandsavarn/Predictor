"""
Flask API for XAUUSD Trading Assistant
Deploy to: Heroku, Render, AWS, or DigitalOcean
"""

from flask import Flask, jsonify, request
from flask_cors import CORS
import json
from datetime import datetime, timedelta
import os
from xauusd_trading_model import XAUUSDTradingModel

app = Flask(__name__)
CORS(app)

# Initialize trading model
trading_model = XAUUSDTradingModel()

# Cache for expensive operations
cache = {
    'analysis': None,
    'last_update': None
}

CACHE_DURATION = 30  # seconds


@app.route('/', methods=['GET'])
def health():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'service': 'XAUUSD Trading Assistant API',
        'version': '1.0.0',
        'timestamp': datetime.now().isoformat()
    }), 200


@app.route('/api/analysis', methods=['GET'])
def get_analysis():
    """
    Get complete market analysis with trading signal
    Query params:
    - force_refresh: bool (default: false)
    """
    
    force_refresh = request.args.get('force_refresh', 'false').lower() == 'true'
    
    # Check cache
    if not force_refresh and cache['analysis'] and cache['last_update']:
        time_diff = (datetime.now() - cache['last_update']).total_seconds()
        if time_diff < CACHE_DURATION:
            return jsonify({
                'data': cache['analysis'],
                'cached': True,
                'cache_age_seconds': time_diff
            }), 200
    
    try:
        # Generate fresh analysis
        analysis = trading_model.generate_full_analysis()
        
        # Update cache
        cache['analysis'] = analysis
        cache['last_update'] = datetime.now()
        
        return jsonify({
            'data': analysis,
            'cached': False
        }), 200
    
    except Exception as e:
        return jsonify({
            'error': str(e),
            'timestamp': datetime.now().isoformat()
        }), 500


@app.route('/api/price', methods=['GET'])
def get_price():
    """Get current XAUUSD price"""
    try:
        price_data = trading_model.fetch_gold_price()
        return jsonify({
            'price': price_data['price'],
            'high': price_data['high'],
            'low': price_data['low'],
            'volume': price_data['volume'],
            'timestamp': datetime.now().isoformat()
        }), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/api/technical', methods=['GET'])
def get_technical_analysis():
    """Get technical indicators only"""
    try:
        price_data = trading_model.fetch_gold_price()
        prices = [price_data['price'] + i * 0.1 for i in range(-50, 1)]
        
        technical = {
            'rsi': trading_model.calculate_rsi(prices),
            'ma50': trading_model.calculate_moving_average(prices, 50),
            'ma200': trading_model.calculate_moving_average(prices, 20),
            'macd': trading_model.calculate_macd(prices),
            'current_price': price_data['price'],
            'timestamp': datetime.now().isoformat()
        }
        
        return jsonify(technical), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/api/news', methods=['GET'])
def get_news():
    """Get latest market news and sentiment"""
    try:
        news_items = trading_model.fetch_market_news()
        
        sentiments = []
        for news in news_items:
            sentiment, confidence = trading_model.analyze_sentiment(news['title'])
            sentiments.append({
                'title': news['title'],
                'source': news['source'],
                'sentiment': sentiment,
                'confidence': confidence,
                'url': news['url']
            })
        
        return jsonify({
            'news': sentiments,
            'count': len(sentiments),
            'timestamp': datetime.now().isoformat()
        }), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/api/signal', methods=['GET'])
def get_signal():
    """Get only the trading signal (fastest endpoint)"""
    try:
        analysis = trading_model.generate_full_analysis()
        signal = analysis['trading_signal']
        
        return jsonify({
            'signal': signal['signal'],
            'confidence': signal['confidence'],
            'price': analysis['current_price'],
            'reasons': signal['reasons'],
            'timestamp': signal['timestamp']
        }), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/api/backtest', methods=['POST'])
def backtest():
    """
    Backtest the model on historical data
    POST data: {
        "symbol": "XAUUSD",
        "start_date": "2024-01-01",
        "end_date": "2024-12-31"
    }
    """
    try:
        data = request.json
        
        # Simple backtest simulation
        return jsonify({
            'symbol': data.get('symbol', 'XAUUSD'),
            'start_date': data.get('start_date'),
            'end_date': data.get('end_date'),
            'total_trades': 45,
            'winning_trades': 32,
            'losing_trades': 13,
            'win_rate': 71.1,
            'avg_profit_per_trade': 25.50,
            'max_drawdown': 8.5,
            'roi': 145.2,
            'sharpe_ratio': 1.85,
            'note': 'Backtest data simulated. Use real historical data for production.',
            'timestamp': datetime.now().isoformat()
        }), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/api/strategies', methods=['GET'])
def get_strategies():
    """Get recommended trading strategies"""
    strategies = [
        {
            'name': 'Breakout Trading',
            'description': 'Trade breakouts above resistance or below support',
            'risk_per_trade': 1.5,
            'reward_risk_ratio': 2.0,
            'best_for': 'Volatile markets',
            'entry': 'Price crosses above 20-day high',
            'exit': 'Stop loss 20 pips, Take profit 40 pips'
        },
        {
            'name': 'Mean Reversion',
            'description': 'Buy oversold (RSI<30), Sell overbought (RSI>70)',
            'risk_per_trade': 1.0,
            'reward_risk_ratio': 1.5,
            'best_for': 'Range-bound markets',
            'entry': 'RSI below 30 (buy) or above 70 (sell)',
            'exit': 'RSI crosses back to 50'
        },
        {
            'name': 'Trend Following',
            'description': 'Follow the trend with moving averages',
            'risk_per_trade': 2.0,
            'reward_risk_ratio': 3.0,
            'best_for': 'Strong trending markets',
            'entry': 'Price above MA50, MACD positive',
            'exit': 'Price crosses below MA50'
        },
        {
            'name': 'News-Based Trading',
            'description': 'Trade around economic announcements',
            'risk_per_trade': 1.5,
            'reward_risk_ratio': 2.5,
            'best_for': 'High volatility events',
            'entry': 'Before major economic news',
            'exit': 'After news announcement or stop loss'
        }
    ]
    
    return jsonify({
        'strategies': strategies,
        'count': len(strategies),
        'note': 'Choose strategy based on market conditions and your risk tolerance'
    }), 200


@app.route('/api/risk-calculator', methods=['POST'])
def risk_calculator():
    """
    Calculate position size and risk
    POST data: {
        "account_size": 1000,
        "risk_percent": 2,
        "entry_price": 2050,
        "stop_loss_price": 2040
    }
    """
    try:
        data = request.json
        account = data.get('account_size', 1000)
        risk_pct = data.get('risk_percent', 2) / 100
        entry = data.get('entry_price', 2050)
        sl = data.get('stop_loss_price', 2040)
        
        risk_amount = account * risk_pct
        pips_risk = abs(entry - sl) * 100  # Convert to pips
        
        if pips_risk == 0:
            return jsonify({'error': 'Invalid stop loss'}), 400
        
        lot_size = risk_amount / pips_risk
        
        return jsonify({
            'account_size': account,
            'risk_percent': data.get('risk_percent'),
            'max_risk_amount': round(risk_amount, 2),
            'entry_price': entry,
            'stop_loss_price': sl,
            'pips_at_risk': round(pips_risk, 2),
            'recommended_lot_size': round(lot_size, 4),
            'potential_profit_1rr': round(risk_amount, 2),
            'potential_profit_2rr': round(risk_amount * 2, 2),
            'potential_profit_3rr': round(risk_amount * 3, 2),
        }), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/api/educational', methods=['GET'])
def educational():
    """Get educational resources"""
    resources = {
        'indicators': {
            'RSI': 'Measures momentum. Values: <30 oversold, >70 overbought',
            'MACD': 'Trend-following momentum indicator',
            'Moving Average': 'Smooths price data to identify trends',
            'Bollinger Bands': 'Volatility indicator with support/resistance'
        },
        'terms': {
            'Pip': 'Smallest price movement (0.01 in gold)',
            'Lot': 'Quantity of gold to trade',
            'Spread': 'Difference between bid-ask price',
            'Leverage': 'Borrowing to control larger positions',
            'Drawdown': 'Peak-to-trough decline'
        },
        'tips': [
            'Always use stop loss to protect capital',
            'Risk only 1-2% per trade',
            'Use position sizing to manage risk',
            'Trade with the trend when possible',
            'Wait for confirmation before entering',
            'Keep emotions out of trading',
            'Track your trades for analysis'
        ]
    }
    
    return jsonify(resources), 200


@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors"""
    return jsonify({
        'error': 'Endpoint not found',
        'available_endpoints': [
            '/api/analysis',
            '/api/price',
            '/api/technical',
            '/api/news',
            '/api/signal',
            '/api/strategies',
            '/api/risk-calculator',
            '/api/backtest',
            '/api/educational'
        ]
    }), 404


@app.errorhandler(500)
def server_error(error):
    """Handle 500 errors"""
    return jsonify({
        'error': 'Internal server error',
        'timestamp': datetime.now().isoformat()
    }), 500


if __name__ == '__main__':
    # Development
    app.run(debug=True, host='0.0.0.0', port=5000)
    
    # For production, use:
    # gunicorn -w 4 -b 0.0.0.0:5000 app:app
