window.onload = () => {
  console.log("회원가입 페이지");
};

const btn = document.getElementById("btn");

const onClickHandler = async (event) => {
  console.log("회원가입 버튼 클릭");
  const email = document.getElementById("email");
  const password = document.getElementById("password");

  const response = await fetch("http://127.0.0.1:8000/api/v1/users/", {
    headers: { "content-type": "application/json" },
    method: "POST",
    body: JSON.stringify({
      email: email.value,
      password: password.value,
    }),
  });
  console.log(response);
};

btn.addEventListener("click", onClickHandler);
