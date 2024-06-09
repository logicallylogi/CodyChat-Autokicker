chrome.runtime.onInstalled.addListener(() => {
    let context = 'page'
    let actions = ["Mute 5m", "Mute 15m", "Kick 30m", "Kick 1h", "Kick 2h", "Ghost 2h"]
    const actionMenu = chrome.contextMenus.create({
        title: "Action ->",
        id: "action"
    })
    for (const action of actions) {
        chrome.contextMenus.create({
            title: action,
            contexts: [context],
            parentId:actionMenu,
            id: "" + action.toLowerCase().replaceAll(" ", "-")
        })
    }
})
//fetch("https://www.chat-avenue.com/boys/system/action/action.php", {
//   "headers": {
//     "accept": "*/*",
//     "accept-language": "en-US,en;q=0.9",
//     "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
//     "sec-ch-ua": "\"Chromium\";v=\"121\", \"Not A(Brand\";v=\"99\"",
//     "sec-ch-ua-mobile": "?0",
//     "sec-ch-ua-platform": "\"Linux\"",
//     "sec-fetch-dest": "empty",
//     "sec-fetch-mode": "cors",
//     "sec-fetch-site": "same-origin",
//     "x-requested-with": "XMLHttpRequest",
//     "cookie": "_ga=GA1.1.160249606.1708247283; PHPSESSID=cac40f6f62cde4672e2ee66dc4a5299a; bc_userid=3303219; bc_utk=8eced4d07da4bf4fe09af9e91e409490b86b7f9c; _ga_7XWWTPFBB6=GS1.1.1708271460.6.1.1708274133.0.0.0"
//   },
//   "referrerPolicy": "no-referrer",
//   "body": "token=ae4a620eef8aa97bd0d6eca4736281a9&cp=chat&kick=4771627&delay=120&reason=%09%0AGuestJake4455%0918%2F02+10%3A33%09Hmu+for+sc",
//   "method": "POST"
// });
chrome.contextMenus.onClicked.addListener((ev, tab) => {
    chrome.tabs.sendMessage(ev.menuItemId, tab.id)
});