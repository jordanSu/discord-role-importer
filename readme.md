# Discord 身份組批次新增工具
English Version [here](#discord-role-importer)
## 如何使用
### 安裝套件
```bash
$ pip3 install -r requirements.txt
```
### 準備環境檔案
目錄下要創造一個名為 `.env` 的檔案，需要的變數有：
- BOT_TOKEN
    - Discord bot 的 token
- GUILD_ID
    - Guild (Server) 的 ID
- ROLE_LIST_FILE
    - 存放使用者名稱及欲新增身份組的檔案名稱 (須為 csv 檔)

`.env` 範例：
```env
BOT_TOKEN=YOUR_BOT_TOKEN_HERE
GUILD_ID=YOUR_GUILD_ID_HERE
```

`ROLE_LIST_FILE` 檔案內容範例 （csv 檔)
```csv
user1#6024,role1,
user2#6025,role2,role3,role4
```

### 執行
如果有在環境檔案 (.env) 中指定ROLE_LIST_FILE
```bash
$ python3 main.py
```
如果沒有在環境檔案 (.env) 中指定ROLE_LIST_FILE，則需在執行命令時給予檔案路徑
```bash
$ python3 main.py YOUR_ROLE_LIST_FILE_PATH
```

# Discord Role Importer
## How to use it
### Install dependencies
```bash
$ pip3 install -r requirements.txt
```
### Prepare environment file
You have to create a file named `.env`, and the required variables are:
- BOT_TOKEN
    - The token of discord bot
- GUILD_ID
    - The id of Guild (Server)
- ROLE_LIST_FILE
    - The file's name of the csv file which store usernames and roles list that you want to add (need to be a csv file)

`.env` example：
```
BOT_TOKEN=YOUR_BOT_TOKEN_HERE
GUILD_ID=YOUR_GUILD_ID_HERE
ROLE_LIST_FILE=YOUR_ROLE_LIST_FILE_HERE
```

`ROLE_LIST_FILE` file content example （csv file)
```csv
user1#6024,role1,
user2#6025,role2,role3,role4
```

### Execute this batch
If you have assign ROLE_LIST_FILE value in `.env`
```bash
$ python3 main.py
```
If you DID NOT assign ROLE_LIST_FILE value in `.env`, then you need to give file path when you execute it
```bash
$ python3 main.py YOUR_ROLE_LIST_FILE_PATH
```