# 🔍 Instagram Follower Checker

A simple script that returns a list of people you are **following**, but who are **not following you back** on Instagram.

---

## ❗ Why This Exists

Instagram does **not** provide an easy, reliable way to access follower/following lists through automation:

- ❌ **Unofficial APIs** (like `Instaloader`) often get blocked or rate-limited by Meta
- ❌ **Web scraping** is unreliable due to frequently changing tags, elements, and XPath
- ❌ **Official Instagram Graph API** only provides **counts**, not the actual lists of followers/following

---

## ✅ How It Works

This script uses the **data download** method provided by Instagram:

1. You request a copy of your Instagram data (via [this link](https://www.instagram.com/download/request/))
2. Once downloaded, the script parses your `followers.json` and `following.json` files
3. It compares the lists and returns users you follow who **don’t follow you back**

---

## 📦 Requirements

- Python 3.x
- Your downloaded Instagram data from [Instagram Data Download](https://www.instagram.com/download/request/)

