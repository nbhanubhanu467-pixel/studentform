
document.getElementById("studentForm").addEventListener("submit", function(event) {

    const phone = document.querySelector('input[name="phone"]').value;

    if (phone.length !== 10 || !/^[0-9]{10}$/.test(phone)) {
        event.preventDefault();
        alert("Please enter a valid 10-digit phone number.");
    }

});
