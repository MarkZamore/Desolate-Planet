// This is the same option as the vanilla "Do not show this screen again" checkbox.
ClientEvents.tick(() => {
  const options = Client.options
  if (options && !options.skipMultiplayerWarning) {
    options.skipMultiplayerWarning = true
  }
})
