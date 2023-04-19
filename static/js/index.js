window.onload = () => {
  console.log("홈 페이지");
};

const payload = localStorage.getItem("payload");
const parsed_payload = JSON.parse(payload);

const container = document.getElementById("container");
const h3 = document.createElement("h3");

console.log(parsed_payload.email);

h3.innerText = parsed_payload.email;
container.appendChild(h3);
