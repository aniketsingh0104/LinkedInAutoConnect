// Get scroll height
last_height = document.body.scrollHeight;

// function to simulate sleep
const sleep = ms => new Promise(r => setTimeout(r, ms));

while (true) {
  // Scroll down to bottom
  window.scrollTo(0, document.body.scrollHeight);

  // wait for the page to load
  await sleep(2000);

  // find all accept buttons
  var all_accept_buttons = document.querySelectorAll(".artdeco-button--secondary");

  for(var i = 0; i < all_accept_buttons.length; i = i + 1) {
    // click on button
    all_accept_buttons[i].click();

    // wait for some time before accepting next request
    await sleep(500);
  }

  // Calculate new scroll height and compare with last scroll height
  new_height = document.body.scrollHeight;

  console.log("new_height: " + new_height + " last_height: " + last_height);

  // check if no other request is pending
  if (new_height === last_height) {
    break;
  }

  last_height = new_height;
}