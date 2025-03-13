const API_URL = "http://127.0.0.1:8000/api/";  // Update if needed

// Register User
document.getElementById("registerForm").addEventListener("submit", function (event) {
    event.preventDefault();
    let name = document.getElementById("reg_name").value;
    let password = document.getElementById("reg_password").value;

    fetch(API_URL + "add_user/", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ name, password })
    })
    .then(response => response.json())
    .then(data => alert("User Registered!"))
    .catch(error => console.error("Error:", error));
});

// Login User
document.getElementById("loginForm").addEventListener("submit", function (event) {
    event.preventDefault();
    let name = document.getElementById("login_name").value;
    let password = document.getElementById("login_password").value;

    fetch(API_URL + "login_user/", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ name, password })
    })
    .then(response => response.json())
    .then(data => {
        if (data.message) {
            alert("Login Successful!");
        } else {
            alert("Login Failed!");
        }
    })
    .catch(error => console.error("Error:", error));
});

// Fetch Users List
fetch(API_URL + "get_users/")
    .then(response => response.json())
    .then(users => {
        let userList = document.getElementById("userList");
        users.forEach(user => {
            let li = document.createElement("li");
            li.textContent = user.name;
            userList.appendChild(li);
        });
    })
    .catch(error => console.error("Error:", error));

// Forgot Password - Get Security Question
document.getElementById("forgotPasswordForm").addEventListener("submit", function (event) {
    event.preventDefault();
    let name = document.getElementById("forgot_name").value;

    fetch(API_URL + "forget_pass/", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ name })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById("securityQuestion").innerText = data.message;
        document.getElementById("securityAnswerContainer").style.display = "block";
    })
    .catch(error => console.error("Error:", error));
});

// Answer Security Question
document.getElementById("answerSecurityForm").addEventListener("submit", function (event) {
    event.preventDefault();
    let name = document.getElementById("forgot_name").value;
    let answer = document.getElementById("security_answer").value;

    fetch(API_URL + "answer_sec_question/", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ name, answer })
    })
    .then(response => response.json())
    .then(data => {
        if (data.message) {
            alert("Security Answer Correct!");
            document.getElementById("updatePasswordContainer").style.display = "block";
        } else {
            alert("Incorrect Answer!");
        }
    })
    .catch(error => console.error("Error:", error));
});

// Update Password
document.getElementById("updatePasswordForm").addEventListener("submit", function (event) {
    event.preventDefault();
    let name = document.getElementById("forgot_name").value;
    let new_pass = document.getElementById("new_password").value;

    fetch(API_URL + "update_password/", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ name, answer: new_pass })
    })
    .then(response => response.json())
    .then(data => alert("Password Updated Successfully!"))
    .catch(error => console.error("Error:", error));
});
 