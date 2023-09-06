'use strict';
// element toggle function
const elementToggleFunc = function (elem) { elem.classList.toggle("active"); }

// sidebar variables
const sidebar = document.querySelector("[data-sidebar]");
const sidebarBtn = document.querySelector("[data-sidebar-btn]");

// sidebar toggle functionality for mobile
sidebarBtn.addEventListener("click", function () { 
  elementToggleFunc(sidebar); 
});

// page navigation variables
const navigationLinks = document.querySelectorAll("[data-nav-link]");
const pages = document.querySelectorAll("[data-page]");

// add event to all nav link
for (let i = 0; i < navigationLinks.length; i++) {
  navigationLinks[i].addEventListener("click", function () {

    for (let i = 0; i < pages.length; i++) {
      if (this.innerHTML.toLowerCase() === pages[i].dataset.page) {
        pages[i].classList.add("active");
        navigationLinks[i].classList.add("active");
        window.scrollTo(0, 0);
      } else {
        pages[i].classList.remove("active");
        navigationLinks[i].classList.remove("active");
      }
    }
   
  });
}

// get total number of rows of the table
const table = document.querySelector("[data-table]");
const tableRows = table.rows.length - 1;
const totalContactsNum = document.querySelector("#total-contacts-num");
// set total number of rows of the table
totalContactsNum.textContent = tableRows;

// add another table data in each row
for (let i = 1; i <= tableRows; i++) {
  const tableData = document.createElement("td");
  table.rows[i].appendChild(tableData);

  // add delete and edit buttons to each of this table data
  tableData.innerHTML = `
  <button class="btn btn-danger btn-sm" data-delete-btn aria-label="delete contact button" data-toggle="modal" data-target="#delContact" data-toggle="tooltip" data-placement="left" title="Delete contact">
    <i class="fas fa-trash-alt"></i>
  </button>
  <button class="btn btn-primary btn-sm" data-edit-btn data-toggle="modal" data-target="#editContact" aria-label="edit contact button" data-toggle="tooltip" data-placement="left" title="Edit contact">
    <i class="fas fa-edit"></i>
  </button>
  <button class="btn btn-success btn-sm" data-send-sms-btn data-toggle="modal" data-target="#send-message" aria-label="send message button" data-toggle="tooltip" data-placement="left" title="Send message">
    <i class="fas fa-paper-plane"></i>
  </button>
  `;

  $(document).ready(function(){
    $('[data-toggle="tooltip"]').tooltip();
  });
  
  // add edit button event
  const editBtn = tableData.querySelector("[data-edit-btn]");
  editBtn.addEventListener("click", function () {
    const contactName = table.rows[i].cells[1].textContent;
    const contactEmail = table.rows[i].cells[2].textContent;
    const contactPhone = table.rows[i].cells[3].textContent;
    const updateContactBtn = document.querySelector("#updateContact");

    const editContactModal = document.querySelector("#editContact");
    const editContactForm = document.querySelector("#edit-contact-form");
    const editContactName = editContactForm.querySelector("#edit-contact-name");
    const editContactPhone = editContactForm.querySelector("#edit-contact-phone");
    const editContactEmail = editContactForm.querySelector("#edit-contact-email");

    editContactName.value = contactName;
    editContactPhone.value = contactPhone;
    editContactEmail.value = contactEmail;

    editContactModal.setAttribute("data-contact-index", i);

    updateContactBtn.addEventListener("click", function () {
      table.rows[i].cells[1].textContent = editContactName.value;
      table.rows[i].cells[2].textContent = editContactEmail.value;
      table.rows[i].cells[3].textContent = editContactPhone.value;
    }
    );

  }
  );
}

// update table when search input is changed
const searchInput = document.querySelector("#contacts-search-bar");
searchInput.addEventListener("input", function () {
  const searchInputValue = this.value.toLowerCase();
  const tableRows = table.rows.length - 1;
  let tableRowsCounter = 0;

  for (let i = 1; i <= tableRows; i++) {
    const contactName = table.rows[i].cells[0].textContent.toLowerCase();
    const contactPhone = table.rows[i].cells[1].textContent.toLowerCase();
    const contactEmail = table.rows[i].cells[2].textContent.toLowerCase();

    if (contactName.includes(searchInputValue) || contactPhone.includes(searchInputValue) || contactEmail.includes(searchInputValue)) {
      table.rows[i].classList.remove("hide");
      tableRowsCounter++;
    } else {
      table.rows[i].classList.add("hide");
    }
  }

  totalContactsNum.textContent = tableRowsCounter;
});

// write index of each row in the data-index attribute innerHTML
for (let i = 1; i <= tableRows; i++) {
  table.rows[i].setAttribute("data-index", i);
  table.rows[i].cells[0].innerHTML = i;
}


// stats section
const totalContactsStatNum = document.querySelector("#total-contacts-stat-num");

// set total number of contacts every 1 second
setInterval(function () {
  totalContactsStatNum.textContent = table.rows.length - 1;
}, 1000);

// scroll to top button
const scrollToTopBtn = document.querySelector("[data-scroll-top-btn]");
// add active class to scroll to top button when scrolling
window.addEventListener("scroll", function () {
  if (window.scrollY > 100) {
    scrollToTopBtn.classList.add("active");
  } else {
    scrollToTopBtn.classList.remove("active");
  }
});
// scroll to top button functionality
scrollToTopBtn.addEventListener("click", function () {
  window.scrollTo(0, 0);
});
