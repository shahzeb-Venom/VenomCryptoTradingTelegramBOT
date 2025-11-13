# 🚀 Setup Guide - 15 Minutes to Live Bot

Follow these exact steps to deploy your Venom Crypto Trading Bot.

---

## 📋 What You'll Need

- [ ] Telegram account
- [ ] GitHub account (free) - https://github.com
- [ ] Replit account (free) - https://replit.com
- [ ] 15 minutes of your time

---

## 🎯 STEP 1: Get Telegram Credentials (5 min)

### 1.1 Get API_ID and API_HASH

1. Open browser: **https://my.telegram.org/auth**
2. Enter your phone number (with country code): `+1234567890`
3. Click "Next"
4. Check Telegram app for verification code
5. Enter code on website
6. Click "API Development Tools"
7. Fill the form:
   - **App title:** `Venom Bot`
   - **Short name:** `venombot`
   - **Platform:** Select `Other`
8. Click "Create application"

**📝 WRITE DOWN:**
```
API_ID: _____________ (number like 12345678)
API_HASH: _____________ (string like 1a2b3c4d...)
```

### 1.2 Create Your Bot

1. Open Telegram app
2. Search: `@BotFather`
3. Send command: `/newbot`
4. Bot name: `Your Crypto Bot` (or any name you want)
5. Bot username: `your_crypto_bot` (must end with 'bot')
6. Copy the token provided

**📝 WRITE DOWN:**
```
BOT_TOKEN: _____________ (like 110201543:AAH...)
```

### 1.3 Create/Setup Your Channel

1. Create new Telegram channel (or use existing)
2. Name it whatever you want
3. Make it Public or Private
4. Go to Channel Settings → Administrators
5. Click "Add Administrator"
6. Search for your bot username
7. Add it and grant "Post Messages" permission
8. Forward any message from your channel to: `@userinfobot`
9. Copy the channel ID from bot's reply

**📝 WRITE DOWN:**
```
YOUR_CHANNEL_ID: _____________ (like -1001234567890)
```

### 1.4 Get Source Channel IDs

For each signal channel you want to monitor:
1. Forward a message from that channel to `@userinfobot`
2. Copy the channel ID

**📝 WRITE DOWN:**
```
SOURCE_CHANNELS: _____________,-_____________,-_____________
(comma-separated, like: -1002529586843,-1002148968919,-1001263225860)
```

---

## 📦 STEP 2: Upload to GitHub (3 min)

### 2.1 Create Repository

1. Go to: **https://github.com/new**
2. Repository name: `venom-crypto-bot`
3. Description: `Crypto trading signals Telegram bot`
4. Select: **Public**
5. ✅ Check "Add a README file"
6. Click "Create repository"

### 2.2 Upload Project Files

1. Click "Add file" → "Upload files"
2. Drag and drop all 10 files:
   - main.py
   - utils.py
   - keep_alive.py
   - requirements.txt
   - .env.example
   - .gitignore
   - README.md
   - CONFIG.md
   - SETUP.md
   - TROUBLESHOOTING.md
3. Commit message: `Initial bot setup`
4. Click "Commit changes"

✅ **Verify:** All files visible in your repository

---

## 🖥️ STEP 3: Deploy to Replit (5 min)

### 3.1 Import from GitHub

1. Go to: **https://replit.com**
2. Sign in (you can use GitHub account)
3. Click **"Create Repl"** button
4. Select **"Import from GitHub"** tab
5. GitHub URL: `https://github.com/YOUR_USERNAME/venom-crypto-bot`
   - Replace `YOUR_USERNAME` with your actual GitHub username
6. Click "Import from GitHub"
7. Wait 30 seconds for import to complete

### 3.2 Add Secrets (CRITICAL STEP)

1. In Replit, find left sidebar
2. Click **"Tools"**
3. Click **"Secrets"** (lock icon)
4. Add each secret one by one:

**Secret #1:**
- Key: `API_ID`
- Value: [your API_ID from step 1.1]
- Click "Add new secret"

**Secret #2:**
- Key: `API_HASH`
- Value: [your API_HASH from step 1.1]
- Click "Add new secret"

**Secret #3:**
- Key: `BOT_TOKEN`
- Value: [your BOT_TOKEN from step 1.2]
- Click "Add new secret"

**Secret #4:**
- Key: `YOUR_CHANNEL_ID`
- Value: [your channel ID from step 1.3]
- Click "Add new secret"

**Secret #5:**
- Key: `SOURCE_CHANNELS`
- Value: [your source channels from step 1.4]
- Click "Add new secret"

**Optional Secret #6:**
- Key: `CHANNEL_NAMES`
- Value: `-1001234:Channel Name,-1005678:Another Name`
- Click "Add new secret"

**Optional Secret #7 (skip if you don't need it):**
- Key: `PHONE_NUMBER`
- Value: `+1234567890`
- Click "Add new secret"

---

## ▶️ STEP 4: Run Your Bot (1 min)

### 4.1 Start the Bot

1. Click the big green **"Run"** button at top
2. Wait 1-2 minutes for dependencies to install
3. Watch console for messages

**✅ SUCCESS - You should see:**
```
INFO - 🐍 Starting Venom Crypto Trading Bot...
INFO - ✅ Keep-alive server started
INFO - ✅ Posted menu to channel
INFO - 🚀 Bot is running and monitoring channels...
INFO - 📡 Monitoring 3 signal channels
INFO - 📢 Posting to channel: -1001234567890
```

**❌ ERROR - If you see problems:**
- Check all secrets are added correctly
- Verify no typos in keys
- Make sure channel ID has minus sign
- Read error message carefully

---

## ✅ STEP 5: Verify Everything Works (2 min)

### 5.1 Check Your Telegram Channel

1. Open Telegram
2. Go to your channel
3. You should see a message from your bot with buttons

### 5.2 Test Features

Click each button to test:
- [ ] "📊 Live Trading Charts" - Shows coin menu
- [ ] "BTC/USDT" - Opens TradingView chart
- [ ] "📈 Trading Signals" - Shows alert
- [ ] "📰 Crypto News" - Shows news sources
- [ ] "🎯 Trading Strategies" - Shows strategy menu
- [ ] "ℹ️ Help" - Shows help info

All working? **Perfect!** ✅

---

## 🔄 STEP 6: Setup 24/7 Operation (5 min)

Replit free tier sleeps after inactivity. Use UptimeRobot to keep it awake.

### 6.1 Get Your Replit URL

1. In Replit, click **"Webview"** tab (next to Console)
2. Copy the URL from address bar
   - Format: `https://venom-crypto-bot.yourusername.repl.co`

### 6.2 Setup UptimeRobot

1. Go to: **https://uptimerobot.com**
2. Click "Sign Up" (free account)
3. Verify your email
4. Click "Add New Monitor"
5. Fill settings:
   - **Monitor Type:** `HTTP(s)`
   - **Friendly Name:** `Venom Bot`
   - **URL:** [paste your Replit URL]
   - **Monitoring Interval:** `5 minutes`
6. Click "Create Monitor"

✅ **Done!** Your bot will now run 24/7 for free.

---

## 🎉 Congratulations!

Your Venom Crypto Trading Bot is now:
- ✅ Running 24/7
- ✅ Monitoring signal channels
- ✅ Auto-posting signals to your channel
- ✅ Serving your community

---

## 📊 What Happens Next?

### Automatic Signal Forwarding

When a signal appears in source channels:
1. Bot detects it
2. Parses coin, entry, targets, stop-loss
3. Formats it professionally
4. Posts to your channel with chart link
5. Shows source attribution

**Example Signal:**
```
🟢 LONG SIGNAL 🟢
━━━━━━━━━━━━━━━━━━

💎 Pair: BTCUSDT
⚡ Leverage: 10x
📍 Entry: $45000

🎯 Targets:
  • T1: $45500
  • T2: $46000
  • T3: $46500

🛑 Stop Loss: $44500

━━━━━━━━━━━━━━━━━━
📡 Source: Evening Trader Group
⏰ Time: 2024-11-03 10:30:00 UTC

⚠️ DYOR - Not Financial Advice

[📈 Open TradingView Chart] (button)
```

---

## 🔍 Monitoring Your Bot

### Check Replit Console Regularly

**Good signs:**
```
✅ Posted signal: BTCUSDT - LONG from Channel Name
✅ Posted menu to channel
```

**Watch for:**
```
❌ Error forwarding signal
⏳ Rate limit reached, waiting...
```

### Check UptimeRobot Dashboard

- Shows uptime percentage
- Alerts if bot goes down
- Keeps bot alive automatically

---

## 🎨 Next Steps (Optional)

### Customize Your Bot

1. **Add more coins** to chart menu
   - Edit `CHART_MENU` in main.py

2. **Adjust signal patterns**
   - Edit `SIGNAL_PATTERNS` in main.py

3. **Change menu text**
   - Edit responses in `callback_handler()`

4. **Add more source channels**
   - Update `SOURCE_CHANNELS` secret in Replit

### Promote Your Channel

1. Add channel description
2. Pin welcome message
3. Post channel rules
4. Share link with community
5. Engage with members

---

## 🆘 Need Help?

### If Something Goes Wrong:

1. **Check Console Logs**
   - Shows exact error messages
   - Points to the problem

2. **Read Error Messages**
   - Console tells you what's wrong
   - Often says exactly how to fix it

3. **Check Configuration**
   - Verify all secrets in Replit
   - Double-check IDs and tokens
   - Make sure no typos

4. **Read Guides**
   - CONFIG.md - Configuration details
   - TROUBLESHOOTING.md - Problem solving
   - README.md - Complete documentation

5. **Restart Bot**
   - Click Stop button
   - Wait 5 seconds
   - Click Run button

---

## ✅ Final Checklist

Before you finish:

- [ ] Bot running in Replit (green "Running" indicator)
- [ ] Menu message appeared in your Telegram channel
- [ ] All buttons work when clicked
- [ ] Charts open correctly
- [ ] UptimeRobot is monitoring your bot
- [ ] No errors in Replit console
- [ ] SOURCE_CHANNELS are accessible
- [ ] Bot is admin in your channel

**All checked?** You're done! 🎉

---

## 💡 Pro Tips

1. **Start Small**
   - Begin with 1-2 source channels
   - Test thoroughly
   - Add more channels gradually

2. **Monitor First 24 Hours**
   - Check logs regularly
   - Verify signals posting correctly
   - Fix any issues quickly

3. **Test Everything**
   - Click all buttons
   - Open all charts
   - Verify all features work

4. **Keep Backups**
   - Download files from GitHub
   - Save your configuration
   - Document any changes

5. **Stay Updated**
   - Check Replit for errors
   - Monitor UptimeRobot status
   - Update dependencies monthly

---

## 🎯 Summary

**What you accomplished:**
1. ✅ Got all Telegram credentials
2. ✅ Created GitHub repository
3. ✅ Deployed to Replit
4. ✅ Configured all secrets
5. ✅ Bot running 24/7
6. ✅ Monitoring signal channels
7. ✅ Auto-posting to your channel

**Time spent:** ~15 minutes  
**Cost:** $0 (completely free)  
**Result:** Professional crypto signals bot! 🐍

---

**Welcome to automated crypto trading signals!** 🚀

Enjoy your bot and happy trading! 📈

*Remember: Always DYOR (Do Your Own Research). Not financial advice!*