$(function() {

    $("#editor textarea").focus();

    $("#edit_panel").click(function() {
        $(".toggle-button").removeClass("active");
        $(this).addClass("active");
        $(".fill").show();
        $(".fill").css("width", "100%");
        $(".filler").hide();
        $("#menu").css("margin-top", "0px");
        $(".linedwrap").css("width", "100%");
        editor.resize();
    });

    $("#both_panels").click(function() {
        $(".toggle-button").removeClass("active");
        $(this).addClass("active");
        $(".filler").show();
        $(".fill").show();
        $(".fill").css("width", "50%");
        $(".filler").css("width", "50%");
        $("#menu").css("margin-top", "0px");
        editor.resize();
    });

    $("#view_panel").click(function() {
        $(".toggle-button").removeClass("active");
        $(this).addClass("active");
        $(".fill").hide();
        $(".filler").show();
        $(".filler").css("width", "100%");
        $("#menu").css("margin-top", "62px");
        editor.resize();
    });

    $("#view").click(function(e) {
        e.preventDefault();
        var editor = ace.edit("editor");
        var code = editor.getSession().getValue();
        $.ajax({
            url: '.',
            method: 'POST',
            data: {
                type: '1',
                input: code,
                csrfmiddlewaretoken: csrfToken,
            },
            success: function(data) {
                if (data.error != '') {
                    $("#errors").val(data.error);
                    console.log(data.error);
                }
                else {
                    $("#errors").val('');
                    console.log(data.survey);
                    $("#html-survey").text(data.survey);
                    iss.js = data.survey;
                    $("#image .panel-body").empty();
                    eval(data.survey);
                }
            },
            error: function(data) {
                $("#errors").val('error');
                console.log('error');
            }
        });
    });

    $("#save").click(function(e) {
        e.preventDefault();
        var editor = ace.edit("editor");
        var code = editor.getSession().getValue();
        $.ajax({
            url: '.',
            method: 'POST',
            data: {
                type: '1',
                input: code,
                csrfmiddlewaretoken: csrfToken,
            },
            success: function(data) {
                if (data.error != '') {
                    $("#errors").val(data.error);
                    console.log(data.error);
                    $("#modal_validation_error").modal();
                }
                else {
                    $("#errors").val('');
                    console.log(data.survey);
                    $("#html-survey").text(data.survey);
                    $("#image .panel-body").empty();
                    iss.js = data.survey;
                    eval(data.survey);
                    saveSurvey();
                }
                iss.code = code;
            },
            error: function(data) {
                $("#modal_save_error").modal();
            }
        });
    });
});

    function saveSurvey() {
        if (iss.surveyName == undefined) {
            $("#choose_name_modal").modal();
            return;
        }
        saveToDatabase(false);
    }

    function saveToDatabase(ifNew) {
        $.ajax({
            url: '.',
            method: 'POST',
            data: {
                type: '2',
                new: ifNew ? '1' : '0',
                name: iss.surveyName,
                user: iss.user,
                code: iss.code,
                js: iss.js,
                csrfmiddlewaretoken: csrfToken,
            },
            success: function(data) {
                if (data.success == 1) {
                    console.log("Success!");
                    return;
                }
                $("#used_name_modal").modal();
            },
            error: function(data) {
                $("#modal_save_error").modal();
            }
        });
    }

        

