function populateList(element, list) {
  let templateEl = element.querySelector("li[data-type='template']");
  list.forEach((item) => {
    let li = templateEl.cloneNode();
    li.innerHTML = item;
    li.classList.remove("hidden");
    li.removeAttribute("data-type");
    element.appendChild(li);
  });
}

function clearLiElements(element) {
  let liElements = element.querySelectorAll("li:not([data-type='template'])");
  liElements.forEach((item) => {
    item.remove();
  });
}

function updateText(element, text) {
  element.innerHTML = text;
}

function disableButton(buttonElement) {
  buttonElement.disabled = true;
  updateText(buttonElement, "Loading...");
  buttonElement.classList.add("opacity-50", "cursor-not-allowed");
  buttonElement.classList.remove("hover:bg-blue-700");
}

function enableButton(buttonElement) {
  buttonElement.disabled = false;
  updateText(buttonElement, "Submit");
  buttonElement.classList.remove("opacity-50", "cursor-not-allowed");
  buttonElement.classList.add("hover:bg-blue-700");
}

async function fetchData(postData, headers) {
  let sortedListTitleEl = document
    .getElementById("sorted-list")
    .querySelector("div");
  updateText(sortedListTitleEl, "Loading...");
  const data = await fetch("/api/sort/", {
    method: "POST",
    body: JSON.stringify(postData),
    headers: headers,
  }).then((response) => {
    return response.json();
  });
  updateText(sortedListTitleEl, "Here are the words alphabetically sorted...");
  return data;
}

const formElement = document.getElementById("sort-form");
formElement.addEventListener("submit", async (event) => {
  event.preventDefault();
  const textareaElement = document.getElementById("textarea");
  // Create a list of words from the textarea values
  const wordList = textareaElement.value.trim().split("\n");
  // Provide the headers to the request
  const csrfToken = document.querySelector("input[name='csrfmiddlewaretoken']")
    .value;
  const headers = {
    Accept: "application/json",
    "Content-Type": "application/json",
    "X-CSRFToken": csrfToken,
  };
  let button = document.getElementById("submit");
  disableButton(button);
  // Clear the list items from any previous response
  // and then populate with the new items
  let sortedUl = document.getElementById("sorted-ul");
  // Get the data from the API endpoint
  clearLiElements(sortedUl);
  let sortedList = await fetchData(wordList, headers);
  populateList(sortedUl, sortedList);
  enableButton(button);
});
