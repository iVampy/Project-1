function validateForm() {
	var quizz_1 = document.forms["Form"]["quizz_1"].value;
    var midterm_test = document.forms["Form"]["midterm_test"].value;
    var quizz_2 = document.forms["Form"]["quizz_2"].value;
    var exam = document.forms["Form"]["exam"].value;

    if (!quizz_1 || !midterm_test || !quizz_2 || !exam) {
    	alert("Please Fill All Required Fields");
    	return false;
    }
}