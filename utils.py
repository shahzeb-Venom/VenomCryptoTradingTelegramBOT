import re
from datetime import datetime
import logging

logger = logging.getLogger(__name__)

class SignalParser:
    """Enhanced signal parser with multiple format support"""
    
    PATTERNS = {
        'coin_pairs': [
            r'\b([A-Z]{2,10})(USDT|BTC|ETH|BUSD|USD|PERP)\b',
            r'\b([A-Z]{2,10})[/\-](USDT|BTC|ETH|BUSD|USD)\b',
            r'#([A-Z]{2,10})(USDT|BTC|ETH|BUSD)',
        ],
        'buy_signals': [
            r'\b(buy|long|entry|open\s*long)\b',
            r'🟢',
            r'📈.*entry',
        ],
        'sell_signals': [
            r'\b(sell|short|exit|open\s*short)\b',
            r'🔴',
            r'📉.*entry',
        ],
        'entry_price': [
            r'entry[:\s]*\$?(\d+\.?\d*)',
            r'entry\s*price[:\s]*\$?(\d+\.?\d*)',
            r'@\s*\$?(\d+\.?\d*)',
            r'price[:\s]*\$?(\d+\.?\d*)',
        ],
        'targets': [
            r'target\s*[0-9]?[:\s]*\$?(\d+\.?\d*)',
            r'tp\s*[0-9]?[:\s]*\$?(\d+\.?\d*)',
            r't[0-9][:\s]*\$?(\d+\.?\d*)',
            r'take\s*profit[:\s]*\$?(\d+\.?\d*)',
        ],
        'stop_loss': [
            r'stop\s*loss[:\s]*\$?(\d+\.?\d*)',
            r'sl[:\s]*\$?(\d+\.?\d*)',
            r'stoploss[:\s]*\$?(\d+\.?\d*)',
        ],
        'leverage': [
            r'leverage[:\s]*(\d+)[xX]',
            r'(\d+)[xX]\s*leverage',
            r'lev[:\s]*(\d+)x?',
        ]
    }
    
    @staticmethod
    def parse(text):
        """Parse signal from text"""
        if not text:
            return None
        
        text_clean = text.strip()
        text_lower = text_clean.lower()
        
        signal = {
            'type': None,
            'coin': None,
            'entry': None,
            'targets': [],
            'stop_loss': None,
            'leverage': None,
            'confidence': 0,
            'raw_text': text_clean
        }
        
        # Detect signal type
        buy_match = any(re.search(p, text_lower, re.IGNORECASE) 
                       for p in SignalParser.PATTERNS['buy_signals'])
        sell_match = any(re.search(p, text_lower, re.IGNORECASE) 
                        for p in SignalParser.PATTERNS['sell_signals'])
        
        if buy_match and not sell_match:
            signal['type'] = 'LONG'
            signal['confidence'] += 20
        elif sell_match and not buy_match:
            signal['type'] = 'SHORT'
            signal['confidence'] += 20
        
        # Extract coin
        for pattern in SignalParser.PATTERNS['coin_pairs']:
            match = re.search(pattern, text_clean, re.IGNORECASE)
            if match:
                signal['coin'] = match.group(0).upper()
                signal['confidence'] += 30
                break
        
        # Extract entry price
        for pattern in SignalParser.PATTERNS['entry_price']:
            match = re.search(pattern, text_lower)
            if match:
                signal['entry'] = match.group(1)
                signal['confidence'] += 20
                break
        
        # Extract targets
        for pattern in SignalParser.PATTERNS['targets']:
            matches = re.finditer(pattern, text_lower)
            for match in matches:
                target = match.group(1)
                if target not in signal['targets']:
                    signal['targets'].append(target)
        if signal['targets']:
            signal['confidence'] += 15
        
        # Extract stop loss
        for pattern in SignalParser.PATTERNS['stop_loss']:
            match = re.search(pattern, text_lower)
            if match:
                signal['stop_loss'] = match.group(1)
                signal['confidence'] += 15
                break
        
        # Extract leverage
        for pattern in SignalParser.PATTERNS['leverage']:
            match = re.search(pattern, text_lower)
            if match:
                signal['leverage'] = match.group(1)
                break
        
        # Return signal only if confidence is high enough
        if signal['confidence'] >= 50:
            return signal
        
        return None

class MessageFormatter:
    """Format messages for posting"""
    
    @staticmethod
    def format_signal(signal, source_name="Unknown"):
        """Format trading signal"""
        if not signal:
            return None
        
        # Header with emoji
        emoji = "🟢" if signal['type'] == 'LONG' else "🔴"
        message = f"{emoji} **{signal['type']} SIGNAL** {emoji}\n"
        message += "━━━━━━━━━━━━━━━━━━\n\n"
        
        # Coin
        if signal['coin']:
            message += f"💎 **Pair:** `{signal['coin']}`\n"
        
        # Leverage
        if signal['leverage']:
            message += f"⚡ **Leverage:** {signal['leverage']}x\n"
        
        # Entry
        if signal['entry']:
            message += f"📍 **Entry:** `${signal['entry']}`\n"
        
        # Targets
        if signal['targets']:
            message += f"\n🎯 **Targets:**\n"
            for i, target in enumerate(signal['targets'][:5], 1):
                message += f"  • T{i}: `${target}`\n"
        
        # Stop Loss
        if signal['stop_loss']:
            message += f"\n🛑 **Stop Loss:** `${signal['stop_loss']}`\n"
        
        # Footer
        message += f"\n━━━━━━━━━━━━━━━━━━\n"
        message += f"📡 **Source:** {source_name}\n"
        message += f"⏰ {datetime.now().strftime('%Y-%m-%d %H:%M:%S UTC')}\n"
        message += f"\n⚠️ **DYOR - Not Financial Advice**"
        
        return message
    
    @staticmethod
    def format_chart_link(coin):
        """Generate chart links"""
        if not coin:
            return {}
        
        # Extract base coin
        base = re.sub(r'(USDT|BTC|ETH|BUSD|USD|PERP|/.*)', '', coin)
        
        links = {
            'tradingview': f"https://www.tradingview.com/chart/?symbol=BINANCE:{base}USDT",
            'binance': f"https://www.binance.com/en/trade/{base}_USDT",
            'coingecko': f"https://www.coingecko.com/en/coins/{base.lower()}",
        }
        
        return links

class RateLimiter:
    """Simple rate limiter for Telegram API"""
    
    def __init__(self, max_per_minute=20):
        self.max_per_minute = max_per_minute
        self.requests = []
    
    async def wait_if_needed(self):
        """Wait if rate limit exceeded"""
        import asyncio
        from datetime import datetime, timedelta
        
        now = datetime.now()
        # Remove old requests
        self.requests = [r for r in self.requests if now - r < timedelta(minutes=1)]
        
        if len(self.requests) >= self.max_per_minute:
            wait_time = 60 - (now - self.requests[0]).seconds
            logger.warning(f"⏳ Rate limit reached, waiting {wait_time}s")
            await asyncio.sleep(wait_time)
            self.requests = []
        
        self.requests.append(now)

def validate_config():
    """Validate environment configuration"""
    import os
    
    required = ['API_ID', 'API_HASH', 'BOT_TOKEN', 'YOUR_CHANNEL_ID']
    missing = [key for key in required if not os.environ.get(key)]
    
    if missing:
        raise ValueError(f"Missing required environment variables: {', '.join(missing)}")
    
    # Validate types
    try:
        int(os.environ.get('API_ID'))
        int(os.environ.get('YOUR_CHANNEL_ID'))
    except (ValueError, TypeError):
        raise ValueError("API_ID and YOUR_CHANNEL_ID must be integers")
    
    logger.info("✅ Configuration validated successfully")
    return True