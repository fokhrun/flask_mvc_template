
$(document).ready(function(){

    // Initialize Bootstrap popovers
    $('[data-toggle="popover"]').popover({
        trigger: "manual",  // Manual trigger to show/hide popover
        container: "body"   // Append popover to body to ensure proper positioning
    });

    function validateUserNameField() {
        var usernameValid = true;
        
        // Ensure username is at least 5 characters
        if ($("#username").val().length < 5) {
            $("#username").attr("data-content", "Username must be at least 5 characters long.").popover("show");
            usernameValid = false;
        }
        
        return usernameValid;
    };

    function validateEmailField() {
        var emailValid = true;
    
        // email validation: Ensure email is valid
        var emailRegex = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,6}$/;
        if (!emailRegex.test($("#email").val())) {
            $("#email").attr("data-content", "Please enter a valid email address.").popover("show");
            emailValid = false;
        }
        
        return emailValid;
    };

    function validatePasswordField(passwordId) {
        var passwordValid = true;
    
        // Ensure password is at least 8 characters
        if ($(passwordId).val().length < 3) {
            $(passwordId).attr("data-content", "Password must be at least 8 characters long.").popover("show");
            passwordValid = false;
        }
        
        return passwordValid;
    };

    function validateConfirmationPasswordField(passwordId, confirmationPasswordId) {
        var confirmPasswordValid = true;
    
        // Ensure passwords match
        if ($(passwordId).val() !== $(confirmationPasswordId).val()) {
            $(confirmationPasswordId).attr("data-content", "Passwords do not match.").popover("show");
            confirmPasswordValid = false;
        }
        
        return confirmPasswordValid;
    };

    $("#registration").submit(function(event){
        
        // Reset popovers
        $('[data-toggle="popover"]').popover("hide");

        var passwordId = "#password";
        var confirmationPasswordId = "#password2";
        
        var valid = validateUserNameField() 
            && validateEmailField() 
            && validatePasswordField(passwordId) 
            && validatePasswordField(confirmationPasswordId)
            && validateConfirmationPasswordField(passwordId, confirmationPasswordId);

        if (!valid) {
            event.preventDefault();
        }
    });

    $("#login").submit(function(event){
        
        // Reset popovers
        $('[data-toggle="popover"]').popover("hide");
        
        var valid = validateEmailField()

        if (!valid) {
            event.preventDefault();
        }
    });
});
