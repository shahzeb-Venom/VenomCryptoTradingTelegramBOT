# 🔧 Troubleshooting Guide

Solutions to common problems with your Venom Crypto Trading Bot.

---

## 🆘 Quick Fixes

Try these first for most problems:

1. ✅ **Restart the bot** (Stop → Run in Replit)
2. ✅ **Check all Secrets are added** (Tools → Secrets)
3. ✅ **Read the console logs** (shows exact errors)
4. ✅ **Verify bot is admin** in your channel
5. ✅ **Wait 2 minutes** after starting (dependencies install)

---

## ❌ Problem 1: Bot Won't Start

### Symptoms
- Replit shows errors immediately
- Console says "Missing environment variables"
- Bot crashes on startup

### Solutions

**A. Missing Secrets**

Check Tools → Secrets has all of these:
- `API_ID`
- `API_HASH`
- `BOT_TOKEN`
- `YOUR_CHANNEL_ID`
- `SOURCE_CHANNELS`

**B. Wrong Secret Format**

Secrets should look like this:
```
✅ CORRECT:
API_ID = 12345678
API_HASH = 1a2b3c4d5e6f...
BOT_TOKEN = 110201543:AAH...
YOUR_CHANNEL_ID = -1001234567890
SOURCE_CHANNELS = -1002529586843,-1002148968919

❌ WRONG (don't add quotes):
API_ID = "12345678"
API_HASH = '1a2b3c4d...'
```

**C. Invalid Credentials**

1. Go to https://my.telegram.org
2. Verify API_ID and API_HASH
3. Update in Replit Secrets
4. Restart bot

**D. Module Not Found**

Wait 2 minutes after clicking Run. Replit is installing dependencies.

Or manually install:
```bash
# In Replit Shell:
pip install -r requirements.txt
```

---

## ❌ Problem 2: Bot Starts But No Menu in Channel

### Symptoms
- Bot runs without errors
- Console says "running"
- But nothing appears in your channel

### Solutions

**A. Bot Not Admin**

1. Open your Telegram channel
2. Go to Settings → Administrators
3. Check if bot is in the list
4. If not, add it:
   - Click "Add Administrator"
   - Search for your bot
   - Grant "Post Messages" permission

**B. Wrong Channel ID**

1. Verify in Replit Secrets:
   - Key: `YOUR_CHANNEL_ID`
   - Must start with minus sign: `-1001234567890`
2. If wrong, update and restart bot

**C. Permission Issue**

1. Remove bot from channel completely
2. Re-add as administrator
3. Grant "Post Messages" permission
4. Restart Replit bot

---

## ❌ Problem 3: No Signals Being Forwarded

### Symptoms
- Bot running fine
- Menu works
- But no signals appear in your channel

### Solutions

**A. Source Channels Not Posting**

Signal channels don't post 24/7. Wait for actual signals.

Test by checking source channels manually in Telegram.

**B. Wrong Channel IDs**

1. Verify SOURCE_CHANNELS in Replit Secrets
2. Format: `-1002529586843,-1002148968919` (comma-separated, no spaces)
3. Each ID must start with minus sign
4. Update if wrong, restart bot

**C. Bot Can't Access Source Channels**

Your bot must be able to see messages in source channels.

Options:
- Source channels must be public, OR
- Bot must be a member of private channels

**D. Signal Format Mismatch**

Source channels may use different format.

Check a real signal from source channel, then edit `SIGNAL_PATTERNS` in main.py.

**E. Test Signal Detection**

Send a test message to one of your channels:
```
BUY Signal
BTCUSDT
Entry: 45000
Target 1: 46000
Target 2: 47000
Stop Loss: 44000
```

If this doesn't forward, check pattern matching.

---

## ❌ Problem 4: Buttons Don't Work

### Symptoms
- Menu appears
- Clicking buttons does nothing
- Or shows error

### Solutions

**A. Old Message**

1. Delete old menu messages from channel
2. Restart bot to post fresh menu
3. Try with new message

**B. Callback Timeout**

If button doesn't respond:
- Wait 5 seconds
- Try again
- Check console for errors

**C. Callback Error**

Check Replit console for:
```
ERROR - Error in callback_handler
```

If you see this, check main.py callback_handler() function.

---

## ❌ Problem 5: Charts Don't Open

### Symptoms
- Click chart button
- Nothing happens
- Or "Link broken" error

### Solutions

**A. Check URL Format**

Chart URLs should look like:
```
https://www.tradingview.com/chart/?symbol=BINANCE:BTCUSDT
```

**B. Test URL Manually**

Copy URL from bot message and paste in browser. Should open TradingView.

**C. Coin Name Issue**

Some exotic coins may not be on TradingView. Use major coins for testing.

---

## ❌ Problem 6: Bot Stops After Some Time

### Symptoms
- Bot runs fine initially
- Stops after 30-60 minutes
- Replit shows "inactive"

### Solutions

**A. Setup UptimeRobot** (Main Solution)

1. Get Replit URL from Webview tab
2. Go to https://uptimerobot.com
3. Sign up free
4. Add new monitor:
   - Type: HTTP(s)
   - URL: Your Replit URL
   - Interval: 5 minutes
5. Done! Bot stays alive 24/7

**B. Replit Always On** (Paid Alternative)

Pay $7/month for Replit "Always On" feature.

**C. Check Keep-Alive Server**

Console should show:
```
✅ Keep-alive server started on port 8080
```

If missing, check `keep_alive.py` file exists.

---

## ❌ Problem 7: Rate Limit Errors

### Symptoms
```
ERROR - FloodWaitError: Must wait X seconds
```

### Solutions

**A. This is Normal**

Telegram limits how fast bots can send messages. Bot will automatically wait and retry.

**B. Reduce Activity**

If happens often:
- Don't spam buttons
- Reduce number of source channels
- Add delays between operations

**C. Just Wait**

Bot handles this automatically. No action needed.

---

## ❌ Problem 8: Authentication Errors

### Symptoms
```
ERROR - Invalid API_ID or API_HASH
ERROR - Authentication failed
```

### Solutions

**A. Verify Credentials**

1. Go to https://my.telegram.org
2. Click "API Development Tools"
3. Check your application
4. Copy exact API_ID and API_HASH
5. Update in Replit Secrets
6. Restart bot

**B. No Spaces or Quotes**

```
✅ Correct: 12345678
❌ Wrong: 12345678 (with space)
❌ Wrong: "12345678" (with quotes)
```

**C. Wrong Type**

- API_ID must be NUMBER: `12345678`
- API_HASH must be STRING: `1a2b3c4d...`

---

## ❌ Problem 9: Module Import Errors

### Symptoms
```
ModuleNotFoundError: No module named 'telethon'
ModuleNotFoundError: No module named 'flask'
```

### Solutions

**A. Wait for Auto-Install**

After clicking Run, wait 2 full minutes. Replit is installing packages.

**B. Manual Install**

In Replit Shell (Tools → Shell):
```bash
pip install -r requirements.txt
```

**C. Check requirements.txt**

File should contain:
```
telethon==1.35.0
cryptg==0.4.0
python-dotenv==1.0.0
flask==3.0.0
```

---

## ❌ Problem 10: Signal Format Wrong

### Symptoms
- Signals post but look bad
- Missing information
- Poor formatting

### Solutions

**A. Adjust Parser**

Edit `parse_signal()` function in main.py to match your source format.

**B. Check Source Format**

Look at actual signals in source channel. Note the format:
- How are coins written? (BTC/USDT or BTCUSDT)
- How are targets marked? (TP1, Target 1, T1)
- How is entry written? (Entry:, Price:, @)

**C. Update Patterns**

Edit `SIGNAL_PATTERNS` in main.py:
```python
SIGNAL_PATTERNS = {
    'buy': r'\b(buy|long|YOUR_KEYWORD)\b',
    'coin': r'\b([A-Z]{2,10})(YOUR_FORMAT)\b',
    # ... adjust other patterns
}
```

---

## 🔍 Debugging Tips

### Read Console Logs

Logs tell you exactly what's wrong:

```
✅ Good logs:
INFO - ✅ Keep-alive server started
INFO - ✅ Posted menu to channel
INFO - 🚀 Bot is running...

❌ Error logs:
ERROR - Missing environment variable: API_ID
ERROR - Cannot post to channel: -1001234567890
ERROR - Invalid BOT_TOKEN
```

### Test Step by Step

1. Start bot → Check console
2. Look for menu in channel → Check permissions
3. Click buttons → Check callbacks work
4. Wait for signal → Check detection works
5. Verify signal posts → Check formatting

### Use Shell Commands

In Replit Shell (Tools → Shell):

```bash
# Check Python version
python --version

# Check if file exists
ls -la

# View file
cat main.py

# Test imports
python -c "import telethon; print('OK')"

# Check environment variables
python -c "import os; print(os.environ.get('API_ID'))"
```

---

## 🔐 Security Issues

### Bot Token Leaked?

**Fix:**
1. Go to @BotFather on Telegram
2. Send: `/mybots`
3. Select your bot
4. Choose "API Token"
5. Click "Revoke current token"
6. Copy new token
7. Update in Replit Secrets
8. Restart bot

### API Credentials Compromised?

**Fix:**
1. Go to https://my.telegram.org
2. Delete old application
3. Create new application
4. Get new API_ID and API_HASH
5. Update in Replit Secrets
6. Restart bot

---

## 🆘 Still Not Working?

### Emergency Reset

If nothing works, do a complete reset:

1. **Stop Bot**
   - Click Stop button in Replit

2. **Delete Session Files**
   - In Replit Files, find and delete:
     - `venom_bot_session.session`
     - `user_session.session`
     - Any `.session-journal` files

3. **Verify All Secrets**
   - Tools → Secrets
   - Check each one is correct
   - Remove and re-add if unsure

4. **Restart Clean**
   - Click Run button
   - Watch console carefully
   - Should start fresh

---

## 📊 Common Error Messages Explained

| Error | Meaning | Fix |
|-------|---------|-----|
| `Missing environment variable` | Secret not added | Add missing secret in Replit |
| `Invalid API_ID` | Wrong credentials | Check my.telegram.org |
| `Cannot post to channel` | Not admin or wrong ID | Verify bot is admin |
| `FloodWaitError` | Rate limit hit | Wait, bot auto-retries |
| `Module not found` | Package not installed | Wait or run pip install |
| `Connection timeout` | Network issue | Restart Replit |
| `Permission denied` | Missing channel permission | Add post permission |

---

## ✅ Prevention Checklist

Avoid future problems:

- [ ] Monitor console logs daily
- [ ] Check UptimeRobot status
- [ ] Test features after changes
- [ ] Keep backup of working code
- [ ] Don't edit multiple things at once
- [ ] Update dependencies carefully
- [ ] Document any customizations
- [ ] Test with one source channel first

---

## 📞 Getting Help

### Before Asking for Help

1. ✅ Read this entire guide
2. ✅ Check console logs
3. ✅ Verify all secrets
4. ✅ Restart bot
5. ✅ Test basic features
6. ✅ Wait 2+ minutes for install

### When Asking for Help

Provide:
- Exact error message from console
- What you were trying to do
- What you've already tried
- Screenshots (hide sensitive info!)
- Configuration (without secrets!)

---

## 💡 Pro Troubleshooting Tips

### 1. Isolate the Problem

- Test with ONE source channel
- Try simple test signal
- Check each feature separately

### 2. Compare Working vs Not Working

- What changed?
- What was working before?
- What did you modify?

### 3. Use Process of Elimination

- Remove customizations
- Go back to default code
- Add features back one by one

### 4. Check Similar Issues

- Search error message online
- Check Telethon documentation
- Look at Telegram Bot API docs

### 5. Take Breaks

- Step away for 10 minutes
- Come back with fresh eyes
- Often you'll spot the issue

---

## 🎯 Most Common Causes

90% of issues are:

1. ❌ Missing or wrong secrets (50%)
2. ❌ Bot not admin in channel (20%)
3. ❌ Wrong channel ID format (10%)
4. ❌ Not waiting for install (5%)
5. ❌ Typos in configuration (5%)

Check these first!

---

**Most problems have simple solutions. Stay calm, check logs, verify configuration!** 🔧

Good luck! 🍀