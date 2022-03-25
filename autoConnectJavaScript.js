last_height = document.body.scrollHeight;
const sleep = ms => new Promise(r => setTimeout(r, ms));
while (true) {
  window.scrollTo(0, document.body.scrollHeight);
  await sleep(2000);

  var connections = document.querySelectorAll(".artdeco-button--secondary");

  for(var i = 0; i < connections.length; i = i + 1) {
    connections[i].click();
  }

  new_height = document.body.scrollHeight;

  console.log("new_height: " + new_height + " last_height: " + last_height);

  if (new_height === last_height) {
    break;
  }
  last_height = new_height;
}