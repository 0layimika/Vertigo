const searchBtn = document.querySelectorAll(".search-btn");
const closeSearchBtn = document.querySelector(".closeSearch");
const searchMenu = document.querySelector(".search-box");
const menuOpen = document.querySelector(".menu-btn");
const menuClose = document.querySelector(".menu-close");
const mobileNav = document.querySelector(".mobile-nav");
const overlayS = document.querySelector(".overlay-search");
const overlayN = document.querySelector(".overlay-nav");
const qtyMinus = document.querySelectorAll(".qty-minus");
const qtyPlus = document.querySelectorAll(".qty-add");
const inputQty = document.querySelectorAll(".input-qty");
const updateCart = document.querySelectorAll(".update-btn");
const checkoutForm = document.getElementById("checkout-form");
const checkoutBtn = document.querySelector(".checkout-btn");

let overlayOpacity = 0.5;

const openMenu = (menuElement, overlay) => {
  menuElement.classList.remove("hidden");
  overlay.classList.remove("hidden");
  overlay.style.opacity = overlayOpacity;

  setTimeout(() => {
    menuElement.classList.remove("-translate-x-full");
    menuElement.classList.add("translate-x-0");
  }, 10);
};

const closeMenu = (menuElement, overlay) => {
  menuElement.classList.remove("translate-x-0");
  menuElement.classList.add("-translate-x-full");
  overlay.style.opacity = 0;
  setTimeout(() => {
    menuElement.classList.add("hidden");
    overlay.classList.add("hidden");
  }, 700);
};

const toggleSearchMenu = () => {
  const isHidden = searchMenu.classList.contains("hidden");
  isHidden ? openMenu(searchMenu, overlayS) : closeMenu(searchMenu, overlayS);
  if (!mobileNav.classList.contains("hidden")) {
    closeMenu(mobileNav, overlayN);
  }
};

const toggleMobileMenu = () => {
  const isHidden = mobileNav.classList.contains("hidden");
  isHidden ? openMenu(mobileNav, overlayN) : closeMenu(mobileNav, overlayN);
  if (!searchMenu.classList.contains("hidden")) {
    closeMenu(searchMenu, overlayS);
  }
};

searchBtn.forEach((btn) => {
  btn.addEventListener("click", toggleSearchMenu);
});
closeSearchBtn.addEventListener("click", () => {
  closeMenu(searchMenu, overlayS);
});

menuOpen.addEventListener("click", toggleMobileMenu);
menuClose.addEventListener("click", toggleMobileMenu);

qtyMinus.forEach((minus, index) => {
  minus.addEventListener("click", () => {
    if (parseInt(inputQty[index].value) > 1) {
      inputQty[index].value = parseInt(inputQty[index].value) - 1;
      updateCart[index].style.backgroundColor = "black";
      updateCart[index].classList.add("cursor-pointer");
    }
  });
});

qtyPlus.forEach((plus, index) => {
  plus.addEventListener("click", () => {
    inputQty[index].value = parseInt(inputQty[index].value) + 1;
    updateCart[index].style.backgroundColor = "black";
    updateCart[index].classList.add("cursor-pointer");
  });
});

updateCart.forEach((btn, index) => {
  btn.addEventListener("click", () => {
    btn.style.backgroundColor = "grey";
    updateCart[index].classList.remove("cursor-pointer");
  });
});

const currentPageURL = window.location.href;
if (currentPageURL === "http://127.0.0.1:8000/store/checkout/") {
  checkoutBtn.addEventListener("click", function (event) {
    const inputFields = form.querySelectorAll("input[required]");
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
}

const labels = document.querySelectorAll(".size");
console.log(labels);
labels.forEach((lbl) => {
  lbl.addEventListener("click", function () {
    console.log(this);
    var radioInput = this.querySelector('input[type="radio"]');
    if (radioInput) {
      console.log(this);
      radioInput.checked = true;
    }
  });
});

const sizeLabels = document.querySelectorAll(".size");
sizeLabels.forEach((label) => {
  label.addEventListener("change", function () {
    sizeLabels.forEach((l) => {
      l.parentElement.classList.remove("bg-black");
      l.parentElement.classList.remove("text-white");
    });
    if (label.checked) {
      label.parentElement.classList.add("bg-black");
      label.parentElement.classList.add("text-white");
    }
  });
});
