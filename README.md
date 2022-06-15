# jobcan-auto-attend

ジョブカンの出勤ボタンを自動で押します。

タスクスケジューラーやcronで毎朝実行するようにして使います。

APIを利用して休日判定をするので曜日指定せず毎朝実行でOKです。(APIがダウンしているorエラーを返す場合土日の判定だけ行います）

Pythonをインストール後
`pip install selenium` と `pip install webdriver-manager` してください。

urllib3も利用していますがseleniumかwebdriver-managerの依存で勝手にインストールされるようです。

* day.py
* jobcan.py
* call_python.bat

を同じフォルダにおいて使います。(call_python.batはwindowsの人のみ利用)
