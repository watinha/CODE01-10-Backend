let button = document.querySelector('button'),
    p = document.querySelector('p');

button.addEventListener('click', () => {
  (async () => {
    let resp = await fetch('/hello'),
        data = await resp.json();
    p.innerHTML = data.message;
  })();
});


