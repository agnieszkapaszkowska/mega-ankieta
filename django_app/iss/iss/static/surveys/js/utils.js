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
                $("#modal_error .modal-body").html(
                    "<h3> Zapis zakończył się niepowodzeniem! </h3>" +
                    "<h4> Sprawdź połączenie z internetem. </h4>");
                $("#modal_error").modal();
            }
        });
    });

    $("#open-button").click(function(e) {
        function showError() {
            $("#modal_error .modal-body").html(
                "<h3> Nie znaleziono ankiet spełniających kryteria! </h3>" +
                "<h4> Spróbuj jeszcze raz. </h4>");
            $("#modal_error").modal();
        }

        e.preventDefault();
        
        var text = $("#search-survey").val();
        $.ajax({
            url: '.',
            method: 'POST',
            data: {
                type: '3',
                text: text,
                username: iss.user,
                csrfmiddlewaretoken: csrfToken,
            },
            success: function(data) {
                var suggestions = data.results.split(";");
                if (suggestions.length == 0 || suggestions[0].length == 0)
                    showError();
                else if (suggestions.length == 1)
                    openSurvey(suggestions[0]);
                else
                    showChooseSurveyModal(suggestions);
            },
            error: function(data) {
                showError();
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

function openSurvey(name) {
    console.log(name);
    $.ajax({
        url: '.',
        method: 'POST',
        data: {
            type: '4',
            name: name,
            csrfmiddlewaretoken: csrfToken,
        },
        success: function(data) {
            iss.surveyName = name;
            var editor = ace.edit("editor");
            editor.getSession().setValue(data.survey);
        },
        error: function(data) {
            $("#modal_error .modal-body").html(
                "<h3> Nie udało się otworzyć ankiety! </h3>" +
                "<h4> Sprawdź połączenie z internetem. </h4>");
            $("#modal_error").modal();
        }
    });
}
                    
function showChooseSurveyModal(suggestions) {
    $("#modal-suggestions .modal-body").empty();
    for (var i = 0; i < suggestions.length; i++) {
        $("<label style='display:block;'><input type='radio' name='suggestion' value='"
            + suggestions[i] + "' " + (i == 0 ? "checked" : "") + " />"
            + suggestions[i] + "</label>").appendTo(
                 $("#modal-suggestions .modal-body"));
    }
    $("#modal-suggestions .modal-footer button").click(function() {
        var checkedIndex = $("#modal-suggestions .modal-body").find('input').
            index($("#modal-suggestions .modal-body").find('input:checked'));

        openSurvey(suggestions[checkedIndex]);
    });
    $("#modal-suggestions").modal();
}



    

