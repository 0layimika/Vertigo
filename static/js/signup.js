const signupForm = document.getElementById("signup-form");
const signupBtn = document.getElementById("signup-btn");

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