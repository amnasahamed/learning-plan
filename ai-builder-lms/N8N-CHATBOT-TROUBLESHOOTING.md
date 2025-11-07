# n8n Chatbot Integration Guide

This document explains how the n8n chatbot is integrated and how to troubleshoot if it's not appearing.

## How It Works

The n8n chat widget is integrated using the official n8n chat package loaded from CDN:

1. **Script Loading**: `@n8n/chat` package is loaded from CDN
2. **Initialization**: After script loads, `window.createChat()` is called
3. **Display**: Chat widget appears as a floating button in the bottom-right corner
4. **Communication**: Widget connects to your n8n webhook endpoint

## Integration Location

### Files Involved:
- `src/components/ChatWidget.tsx` - Chat widget component
- `src/app/layout.tsx` - Where ChatWidget is rendered
- **Webhook URL**: `https://n8n.themelon.in/webhook/be575669-d460-4f3a-be2c-0b8206552977/chat`

## Expected Behavior

When working correctly:
1. ✅ Chat button appears in bottom-right corner
2. ✅ Click opens chat interface
3. ✅ Initial greeting message appears
4. ✅ User can type messages and get responses from n8n

## Troubleshooting

### Issue 1: Chat Widget Not Appearing

**Symptoms:**
- No chat button visible on the page
- Console shows no errors

**Possible Causes & Solutions:**

#### A. Script Loading Failure

1. **Open Browser Console** (F12 or Right-click → Inspect → Console)

2. **Check for Errors:**
```
Failed to load n8n chat script
```

**Solution:**
- Check internet connection
- Verify CDN is accessible: https://cdn.jsdelivr.net/npm/@n8n/chat/dist/chat.bundle.es.js
- Check firewall/proxy settings

#### B. Script Loaded But Not Initialized

1. **Check Console Logs:**
```
n8n chat script loaded          ✅ Script loaded successfully
n8n chat widget initialized     ✅ Widget initialized
```

If you see "script loaded" but NOT "widget initialized":

**Solution:**
```javascript
// In browser console, manually initialize:
window.createChat({
  webhookUrl: 'https://n8n.themelon.in/webhook/be575669-d460-4f3a-be2c-0b8206552977/chat'
})
```

If this works, there's a timing issue in the code.

#### C. CSS Not Loading

**Check:** The chat button might be hidden by CSS

**Solution:**
1. Inspect element in bottom-right corner
2. Look for elements with `n8n-chat` in the class name
3. Check if `display: none` or `visibility: hidden` is applied

#### D. Z-Index Issue

**Check:** Chat button might be behind other elements

**Solution:**
Add to your global CSS (`src/app/globals.css`):
```css
/* Ensure chat widget appears on top */
[class*="n8n-chat"] {
  z-index: 999999 !important;
}
```

### Issue 2: Chat Button Appears But Doesn't Work

**Symptoms:**
- Chat button is visible
- Clicking doesn't open chat
- OR opens but doesn't send messages

**Possible Causes & Solutions:**

#### A. Webhook Not Accessible

1. **Test webhook accessibility:**

Open browser console and run:
```javascript
fetch('https://n8n.themelon.in/webhook/be575669-d460-4f3a-be2c-0b8206552977/chat', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({ action: 'sendMessage', message: 'test' })
})
  .then(r => r.text())
  .then(console.log)
  .catch(console.error)
```

Expected response: Some JSON response (not 403/404/500 error)

**If you get errors:**
- 403 Forbidden: Webhook has CORS restrictions or authentication required
- 404 Not Found: Webhook URL is incorrect or workflow is deactivated
- 500 Server Error: n8n workflow has an error

**Solution:**
1. Check n8n workflow is **activated**
2. Check webhook node configuration in n8n
3. Verify webhook URL is exactly correct
4. Check n8n workflow execution logs for errors

#### B. CORS Issues

**Symptoms:**
Console shows:
```
Access to fetch at 'https://n8n.themelon.in/...' has been blocked by CORS policy
```

**Solution:**
In your n8n workflow, ensure the webhook response includes CORS headers:
```javascript
// In n8n HTTP Response node or Function node
return [{
  json: {
    // your response data
  },
  headers: {
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Methods': 'GET, POST, OPTIONS',
    'Access-Control-Allow-Headers': 'Content-Type'
  }
}]
```

### Issue 3: Webhook URL Changed or Incorrect

If you need to update the webhook URL:

**Edit:** `src/components/ChatWidget.tsx`

Find this line:
```javascript
webhookUrl: 'https://n8n.themelon.in/webhook/be575669-d460-4f3a-be2c-0b8206552977/chat',
```

Change to your new webhook URL.

**Rebuild:**
```bash
npm run build
docker-compose up -d --build
```

## Verification Checklist

Use this checklist to verify the integration:

### Step 1: Visual Check
- [ ] Open your LMS in browser (http://localhost:737)
- [ ] Look for chat button in bottom-right corner
- [ ] Chat button should have n8n branding or custom icon

### Step 2: Console Check
Open browser console (F12) and verify:
- [ ] No JavaScript errors
- [ ] See: "n8n chat script loaded"
- [ ] See: "n8n chat widget initialized successfully"
- [ ] No CORS errors
- [ ] No 404/403 errors

### Step 3: Functionality Check
- [ ] Click chat button - interface opens
- [ ] See initial greeting message
- [ ] Type a test message
- [ ] Message sends (loading indicator appears)
- [ ] Response received from n8n

### Step 4: Network Check
Open Network tab (F12 → Network):
- [ ] See request to `chat.bundle.es.js` (status 200)
- [ ] See request to your webhook URL
- [ ] Webhook request returns valid response (not error)

## Manual Testing

### Test 1: Check if Script Loads

1. Open DevTools (F12)
2. Go to Console tab
3. Type:
```javascript
console.log(typeof window.createChat)
```

**Expected:** `function`
**If you see:** `undefined` → Script not loaded

### Test 2: Check if Widget Created

1. Open DevTools (F12)
2. Go to Console tab
3. Type:
```javascript
console.log(window.chatInitialized)
```

**Expected:** `true`
**If you see:** `undefined` or `false` → Widget not initialized

### Test 3: Force Initialize

If widget not appearing, try manual initialization:

```javascript
// In browser console
window.createChat({
  webhookUrl: 'https://n8n.themelon.in/webhook/be575669-d460-4f3a-be2c-0b8206552977/chat',
  initialMessages: ['Hello! How can I help you?'],
  i18n: {
    en: {
      title: 'AI Learning Assistant',
      subtitle: 'Ask me anything',
      inputPlaceholder: 'Type your message...',
    },
  },
})
```

If this works, there's a problem with automatic initialization.

## Advanced Debugging

### Enable Verbose Logging

Edit `src/components/ChatWidget.tsx` and add more logging:

```javascript
useEffect(() => {
  console.log('ChatWidget useEffect triggered')
  console.log('scriptLoaded:', scriptLoaded)
  console.log('window:', typeof window)
  console.log('window.createChat:', typeof window?.createChat)
  console.log('window.chatInitialized:', window?.chatInitialized)

  if (scriptLoaded && typeof window !== 'undefined') {
    // ... rest of code
  }
}, [scriptLoaded])
```

### Check Element Presence

In browser console:
```javascript
// Check if chat elements exist in DOM
document.querySelectorAll('[class*="n8n"]')

// Should return NodeList with chat elements
```

### Inspect Network Requests

1. Open DevTools → Network tab
2. Reload page
3. Filter by "chat" or "n8n"
4. Check all requests succeed (status 200)

## Common Issues & Quick Fixes

| Issue | Quick Fix |
|-------|-----------|
| Chat button not visible | Check browser console for errors |
| Script fails to load | Check internet connection, try VPN |
| 403 Forbidden on webhook | Verify webhook is activated in n8n |
| CORS error | Add CORS headers to n8n workflow response |
| Chat opens but no messages | Check n8n workflow is running |
| Messages not sending | Test webhook URL directly |

## Configuration Options

You can customize the chat widget in `src/components/ChatWidget.tsx`:

```javascript
window.createChat({
  // Required
  webhookUrl: 'YOUR_WEBHOOK_URL',

  // Optional customizations
  initialMessages: [
    'Hi! I can help you with the course.'
  ],

  i18n: {
    en: {
      title: 'Custom Title',
      subtitle: 'Custom Subtitle',
      footer: 'Custom Footer',
      getStarted: 'Start Chatting',
      inputPlaceholder: 'Ask me anything...',
    },
  },

  // Theme (if supported)
  theme: {
    primaryColor: '#2563eb',
  },
})
```

## Getting Help

If the chat widget still doesn't work:

1. **Check n8n Workflow:**
   - Is it activated?
   - Are there any errors in execution logs?
   - Is the webhook node configured correctly?

2. **Check Browser:**
   - Try different browser (Chrome, Firefox, Safari)
   - Disable ad blockers/extensions
   - Try incognito/private mode

3. **Check Network:**
   - Can you access https://n8n.themelon.in directly?
   - Are you behind a firewall/proxy?
   - Try from different network

4. **Collect Debug Info:**
   ```bash
   # Browser: Open Console (F12)
   # Copy all errors and logs

   # Server: Check Docker logs
   docker-compose logs ai-builder-lms | grep -i n8n
   ```

## Alternative: Using Different Chat Widget

If n8n chat widget doesn't work, you can integrate other chat solutions:

- **Tawk.to**: Free live chat widget
- **Crisp**: Modern customer chat
- **Chatwoot**: Open-source live chat
- **Custom**: Build your own with WebSocket

## Summary

The n8n chat widget should "just work" if:
1. ✅ n8n workflow is activated
2. ✅ Webhook URL is correct
3. ✅ No CORS restrictions
4. ✅ Script loads from CDN
5. ✅ No JavaScript errors

Most issues are caused by:
- 🔴 Deactivated n8n workflow
- 🔴 Wrong webhook URL
- 🔴 CORS restrictions
- 🔴 Network/firewall blocking
- 🔴 Browser extensions interfering

Follow the troubleshooting steps above to identify and fix the issue! 🚀
