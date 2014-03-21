test( "text_test1", function() {
	var txt = new iss.lib.widgets.TextWidget({text: function(){ return "abc"}});
	equal( $(txt), "abc", "Pased!" );
});

/*
	deepEqual( txt.text, "abc", "Passed!" );
	ok( txt.text == "abc", "Passed!" );
*/
