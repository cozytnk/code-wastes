# めも

## settings.json

```json
{
    "workbench.startupEditor": "newUntitledFile",
    "extensions.ignoreRecommendations": true,
    "liveServer.settings.donotShowInfoMsg": true,

    // ファイル保存時に末尾の空白を削除
    "files.trimTrailingWhitespace": true,
    "[markdown]": {
        "files.trimTrailingWhitespace": false
    },

    "editor.wordWrap": "on",
  	
    // 制御文字の表示
    "editor.renderControlCharacters": true,
  
  	// タブ設定
    "[javascript]": {
        "editor.insertSpaces": true,
        "editor.tabSize": 2
    },

    // パンくずリストの表示
    "breadcrumbs.enabled": true,

    // settings for todohighlight
    "todohighlight.isEnable": true,
    "todohighlight.isCaseSensitive": true,
    "todohighlight.keywords": [
        // "TODO:", "FIXME:",
        "DEBUG:",
        "TBD:",
        "TBI:",
        { "text": "NOTE:", "color": "gray", "backgroundColor": "lightgreen", "overviewRulerColor": "grey" },
        { "text": "REF:", "color": "gray", "backgroundColor": "lightgreen", "overviewRulerColor": "grey" },
    ]

}
```

### REF
- [VisualStudioCodeでMarkdownの時だけ末尾の空白をトリミングしない方法 - Qiita - 2017/9/18](https://qiita.com/otera@github/items/d715f760aab2f6e88e67)

## keybindings.json

```json
// Place your key bindings in this file to override the defaults
[
    {
        "key": "cmd+d",
        "command": "editor.action.deleteLines",
        "when": "textInputFocus && !editorReadonly"
    },

    // tab操作
    {
        "key": "cmd+right",
        "command": "workbench.action.nextEditor"
    },
    {
        "key": "cmd+left",
        "command": "workbench.action.previousEditor"
    },

    // terminal操作
    {
        "key": "cmd+t",
        "command": "workbench.action.terminal.focus", // terminalが開かれていない場合は開く
        "when": "editorTextFocus"
    },
    {
        "key": "cmd+t",
        "command": "workbench.action.focusFirstEditorGroup",
        "when": "terminalFocus"
    },

    {
        "key": "cmd+alt+v",
        "command": "extension.pasteURL",
        "when": "editorTextFocus"
    }

]
```

### REF
- [Visual Studio Code Key Bindings](https://code.visualstudio.com/docs/getstarted/keybindings)
  - 覚書
    > ```json
    > {
    >   "key": "cmd+[Slash]",
    >   "command": "editor.action.commentLine",
    >   "when": "editorTextFocus"
    > }
    > ```

## extensions
- [Trailing Spaces](https://marketplace.visualstudio.com/items?itemName=shardulm94.trailing-spaces): 行末空白のハイライト
- [EvilInspector](https://marketplace.visualstudio.com/items?itemName=saikou9901.evilinspector): 全角空白のハイライト
- [indent-rainbow](https://marketplace.visualstudio.com/items?itemName=oderwat.indent-rainbow): インデントの色分けハイライト
- [Bracket Pair Colorizer 2](https://marketplace.visualstudio.com/items?itemName=CoenraadS.bracket-pair-colorizer-2): 括弧の色分けハイライト
- [TODO Highlight](https://marketplace.visualstudio.com/items?itemName=wayou.vscode-todo-highlight)
  - デフォルトで`TODO:`, `FIXME:`をハイライト
  - 追記: TODO
- [Paste URL](https://marketplace.visualstudio.com/items?itemName=kukushi.pasteurl): `[title](url)`としてurlをペースト
  - デフォルトでは`ctrl+p`じゃだめ
- [Paste JSON as Code](https://marketplace.visualstudio.com/items?itemName=quicktype.quicktype)
  - 未確認
- [Edit csv](https://marketplace.visualstudio.com/items?itemName=janisdd.vscode-edit-csv)
- [Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
- [Live Server](https://marketplace.visualstudio.com/items?itemName=ritwickdey.LiveServer)
- [live-p5](https://marketplace.visualstudio.com/items?itemName=filipesabella.live-p5)
- [Vetur](https://marketplace.visualstudio.com/items?itemName=octref.vetur): `.vue`ファイルのシンタックスハイライト等
- [WebVTT Language - Visual Studio Marketplace](https://marketplace.visualstudio.com/items?itemName=spaceribs.webvtt-language): `.vtt`ファイルのシンタックスハイライト等
- [PlantUML](https://marketplace.visualstudio.com/items?itemName=jebbs.plantuml)
