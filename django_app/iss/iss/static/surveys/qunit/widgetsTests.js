test( "text_test1", function() {
	var txt = new iss.lib.widgets.Widget("text", {text: function(){ return "abc"}});
    var widget = txt(function() { return true })('#qunit-fixture', null);
    //console.log(widget.element[0].childNodes[0].data);
	equal( widget.element[0].childNodes[0].data, "abc", "Pased!" );
});

/*
	deepEqual( txt.text, "abc", "Passed!" );
	ok( txt.text == "abc", "Passed!" );
*/
