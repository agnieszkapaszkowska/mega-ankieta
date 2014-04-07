//console.log(widget.element[0].childNodes[0].data);
test( "text_test1", function() {
	var txt = new iss.lib.widgets.Widget("text", {text: function(){ return "abc"}});
    	var widget = txt(function() { return true })('#qunit-fixture', null);
	equal( widget.element[0].childNodes[0].data, "abc", "Pased!" );
});

test( "checkbox_test1", function() {
	var chbox = new iss.lib.widgets.Widget("checkbox", {name: function() { return "c" }, data: function() { return [function() { return {id: function() { return "c1" }, text: function() { return "aaa" }, checked: function() { return false }}}, function() { return {id: function() { return "c2" }, text: function() { return "bbb" }, checked: function() { return true }}}]}, horizontal: function() { return false }, required: function() { return false }});

    	var widget = chbox(function() { return true })('#qunit-fixture', null);
	ok( widget.element[0].childNodes[1].childNodes[0].hasAttribute("checked"), "Pased!" );
});


test( "checkbox_test2", function() {
	var chbox = new iss.lib.widgets.Widget("checkbox", {resultVarName: "x", name: function() { return "c" }, data: function() { return [function() { return {id: function() { return "c1" }, text: function() { return "aaa" }, checked: function() { return false }}}, function() { return {id: function() { return "c2" }, text: function() { return "bbb" }, checked: function() { return true }}}]}, horizontal: function() { return false }, required: function() { return false }});

    	var widget = chbox(function() { return true })('#qunit-fixture', null);
	ok(equalArrays(iss.vars.x ,[1]), "Pased!" );
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

/*
	deepEqual( txt.text, "abc", "Passed!" );
	ok( txt.text == "abc", "Passed!" );
*/
