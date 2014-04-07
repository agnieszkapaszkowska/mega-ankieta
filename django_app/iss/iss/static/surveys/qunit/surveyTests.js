
test( "checkbox_test3", function() {
    iss.survey = new iss.lib.Survey();
    iss.survey.container = "#qunit-fixture";
	iss.survey.addWidget(function() {return iss.lib.widgets.Widget("checkbox", {resultVarName: "x", name: function() { return "c" }, data: function() { return [function() { return {id: function() { return "c1" }, text: function() { return "aaa" }, checked: function() { return false }}}, function() { return {id: function() { return "c2" }, text: function() { return "bbb" }, checked: function() { return true }}}]}, horizontal: function() { return false }, required: function() { return false }})});
    iss.survey.init();
	ok(equalArrays(iss.vars.x ,[1]), "Pased!" );
});

test( "checkbox_conditional_test", function() {
    iss.survey = new iss.lib.Survey();
    iss.survey.container = "#qunit-fixture";

    iss.survey.addWidgetConditional([{condition: function() {return function() {with (iss.vars) {return false }}()}, body: function() {
	iss.survey.addWidget(function() {return iss.lib.widgets.Widget("checkbox", {resultVarName: "y", name: function() { return "c" }, data: function() { return [function() { return {id: function() { return "c1" }, text: function() { return "aaa" }, checked: function() { return false }}}, function() { return {id: function() { return "c2" }, text: function() { return "bbb" }, checked: function() { return true }}}]}, horizontal: function() { return false }, required: function() { return false }})});}}]);
    iss.survey.init();
	equal($("#qunit-fixture").find("#c1").length, 0, "Pased!" );
});


function equalArrays(array1, array2) {
    for (var i = 0; i < array1.length; i++)
        if (array2.indexOf(array1[i]) == -1)
            return false;
    for (var i = 0; i < array2.length; i++)
        if (array1.indexOf(array2[i]) == -1)
            return false;
    return true;
}

test( "validation_test", function() {
    iss.survey = new iss.lib.Survey();
    iss.survey.container = "#qunit-fixture";

	iss.survey.addWidget(function() {return iss.lib.widgets.Widget("checkbox", {resultVarName: "x", name: function() { return "c" }, data: function() { return [function() { return {id: function() { return "c1" }, text: function() { return "aaa" }, checked: function() { return false }}}, function() { return {id: function() { return "c2" }, text: function() { return "bbb" }, checked: function() { return false }}}]}, horizontal: function() { return false }, required: function() { return true }})});
    iss.survey.init();
    var correct = iss.survey.gotoNext();
	ok(!correct, "Pased!" );
});

test( "input_test1", function() {
    iss.survey = new iss.lib.Survey();
    iss.survey.container = "#qunit-fixture";
    iss.survey.addWidget(function() {return iss.lib.widgets.Widget("textinput", {resultVarName: "input1", name: function() { return "input1" }, required: function() { return true }, placeholder: function() { return "" }, label: function() { return "" }})});iss.survey.init();
    $("input[name='input1']").val("Aaa");
    $("input[name='input1']").trigger("change");

    equal(iss.vars.input1, "Aaa", "Passed!");
});

test( "radio_validation_test", function() {
    iss.survey = new iss.lib.Survey();
    iss.survey.container = "#qunit-fixture";
    iss.survey.addWidget(function() {return iss.lib.widgets.Widget("radio", {resultVarName: "radio1", name: function() { return "radio1" }, data: function() { return [function() { return {id: function() { return "r1" }, text: function() { return "radio1" }}}, function() { return {id: function() { return "r2" }, text: function() { return "radio2" }}}]}, checkedIndex: function() { return -1 }, horizontal: function() { return false }, required: function() { return true }})});iss.survey.init();
    var correct = iss.survey.gotoNext();
    ok(!correct, "Passed!");
    equal(iss.vars.radio1, -1, "Passed!");
    $("#r1").trigger("click");
    $("#r1").trigger("click");
    correct = iss.survey.gotoNext();
    ok(correct, "Passed!");
    equal(iss.vars.radio1, 0, "Passed!");
});

/*
	deepEqual( txt.text, "abc", "Passed!" );
	ok( txt.text == "abc", "Passed!" );
*/
