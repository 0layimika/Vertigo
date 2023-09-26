const loginForm = document.getElementById("login-form");
const loginBtn = document.getElementById("login-btn");
const signupForm = document.getElementById("signup-form");
const signupBtn = document.getElementById("signup-btn");


loginBtn.addEventListener("click", function (event) {
    console.log(loginForm)
    const inputFields = loginForm.querySelectorAll("input[required]");
    inputFields.forEach((inputField) => {
      const errorMessage = document.getElementById(inputField.id + "-error");
      if (inputField.value.trim() === "") {
        errorMessage.style.display = "block";
        event.preventDefault();
      } else {
        errorMessage.style.display = "none";
      }
    });
  });