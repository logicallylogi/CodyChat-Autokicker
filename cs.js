// Prepare to sift through data
const message = {}
const author = {}

// Get all the elements together
const messageElement = document.querySelector('div.my_text:hover')
const messageTextElement = messageElement.querySelector('div.chat_message')
const messageRoot = messageElement.parentElement
const authorElement = messageRoot.querySelector('div.chat_avatar')

// Start collecting the data
message.content = messageTextElement.textContent
message.timestamp = messageElement.querySelector('div.btable > div.cdate').textContent
author.avatar = authorElement.getAttribute("data-av")
author.cover = authorElement.getAttribute("data-cover")
author.age = authorElement.getAttribute("data-age")
author.country = authorElement.getAttribute("data-country")
author.gender = authorElement.getAttribute("data-gender")
author.rank = authorElement.getAttribute("data-rank")

// Do some "polyfills"
switch (author.gender) {
    case 1:
        author.gender = "M"
        break;
    case 2:
        author.gender = "F"
        break;
    default:
        author.gender = ""
        break;
}

switch (author.rank) {
    case 50:
        author.rank = "VIP"
        break;
    case 1:
        author.rank = "User"
        break;
    case 0:
        author.rank = "Guest"
        break;
    default:
        author.rank = ""
        break;
}

const messageReason = `${author.rank} ${author.username} ${author.gender}${author.age}${author.country} said ` +
    `"${message.content}" at ${message.timestamp}====*====*====\n\nAvatar: ${author.avatar}\nBackground: ${author.cover}`

chrome.runtime.onMessage.addListener((msg) => {

})