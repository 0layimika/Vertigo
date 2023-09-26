const loginForm = document.getElementById("login-form");
const loginBtn = document.getElementById("login-btn");
const signupForm = document.getElementById("signup-form");
const signupBtn = document.getElementById("signup-btn");

loginBtn.addEventListener("click", (e) => {
  const inputFields = loginForm.querySelectorAll("input[required]");
  inputFields.forEach((inputField) => {
    const errorMessage = document.getElementById(inputField.id + "-error");
    if (inputField.value.trim() === "") {
      errorMessage.style.display = "block";
      e.preventDefault();
    } else {
      errorMessage.style.display = "none";
    }
  });
});

signupBtn.addEventListener("click", (e) => {
  const inputFields = signupForm.querySelectorAll("input[required]");
  inputFields.forEach((inputField) => {
    const errorMessage = document.getElementById(inputField.id + "-error");
    if (inputField.value.trim() === "") {
      errorMessage.style.display = "block";
      e.preventDefault();
    } else {
      errorMessage.style.display = "none";
    }
  });
});
