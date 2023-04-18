window.onload = async () => {
  const data = await (
    await fetch("http://127.0.0.1:8000/api/v1/articles", { method: "GET" })
  ).json();

  const wrapper = document.getElementById("wrapper");
  const ul = document.createElement("ul");

  console.log(data);

  data.forEach((article) => {
    const li = document.createElement("li");
    li.classList.add("article");
    const id = document.createElement("h6");
    const title = document.createElement("h6");
    const content = document.createElement("p");
    id.innerText = article.id;
    title.innerText = article.title;
    content.innerText = article.content;
    li.append(id, title, content);
    ul.appendChild(li);
  });

  wrapper.appendChild(ul);
};
