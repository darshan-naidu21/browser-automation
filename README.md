# 🚀 Subway Outlet Scraper – Agentic Web Automation  

## 📌 Overview  
This project automates the extraction of Subway outlet details from **[Subway Malaysia](https://subway.com.my/find-a-subway)**. It uses an **agentic browsing approach** powered by **GPT-4o Mini** and the **Browser Use framework** to interact with the website dynamically.  

## 🛠️ Key Features  

### ✅ **Agentic Web Scraping**  
- Filters outlets by **Kuala Lumpur**.  
- Scrapes the following details for each outlet:  
  - Name  
  - Full Address  
  - Operating Hours  
  - Waze Direction Link  

### ✅ **Handles Pagination**  
- Detects and navigates through multiple pages to collect all available outlets.  

### ✅ **Conversational Agent Control**  
- Uses an **LLM-powered agent** (`Agent` from `browser_use`) to interact with web elements dynamically.  

### ✅ **Memory & Logging**  
- Saves conversation logs to `"logs/conversation.json"` for debugging and auditing.  

## 🖥️ **Advanced Browser Automation with Browser Use**  
The project utilizes **Browser Use**, which makes websites accessible for AI agents by providing a powerful, yet simple interface for browser automation.

### 🔹 **Key Capabilities of BrowserUse**  

| Feature               | Description |
|----------------------|-------------|
| **Vision + HTML Extraction** | Enables AI to understand web pages by combining visual perception with structured HTML parsing. |
| **Multi-tab Management** | Automatically handles multiple tabs, allowing parallel tasks and complex workflows. |
| **Element Tracking** | Accurately tracks and replicates interactions using XPaths for precise automation. |
| **Custom Actions** | Supports additional automation steps like saving data, updating databases, and handling user inputs. |
| **Self-Correcting Mechanism** | Detects and recovers from errors dynamically, ensuring smooth and resilient automation. |

## ⚡ Tech Stack  

| Component       | Description |
|----------------|-------------|
| **LLM**        | GPT-4o Mini (via `langchain_openai.ChatOpenAI`) |
| **Agent**      | `Agent` from `browser_use` |
| **Web Scraping** | Agentic browsing with `Browser Use` |
| **Logging**    | Saves interactions for debugging |