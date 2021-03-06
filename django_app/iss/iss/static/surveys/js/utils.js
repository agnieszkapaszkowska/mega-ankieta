$(function() {

    $("#editor textarea").focus();

    $("#edit_panel").click(function() {
        $("#change_view_panel").removeClass();
        $("#change_view_panel").addClass("glyphicon glyphicon-edit");
        $(this).addClass("active");
        $(".editor-panel").show();
        $(".editor-panel").css("width", "100%");
        $(".image-panel").hide();
        $(".linedwrap").css("width", "100%");
        editor.resize();
    });

    $("#both_panels").click(function() {
        $("#change_view_panel").removeClass();
        $("#change_view_panel").addClass("glyphicon glyphicon-adjust");
        $(this).addClass("active");
        $(".image-panel").show();
        $(".editor-panel").show();
        $(".image-panel").css("width", "50%");
        $(".editor-panel").css("width", "50%");
        editor.resize();
    });

    $("#view_panel").click(function() {
        $("#change_view_panel").removeClass();
        $("#change_view_panel").addClass("glyphicon glyphicon-eye-open");
        $(this).addClass("active");
        $(".editor-panel").hide();
        $(".imgae-panel").show();
        $(".image-panel").css("width", "100%");
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
                }
                else {
                    $("#errors").val('');
                    iss.js = data.survey;
                    $(".panel-body #image").empty();
                    eval(data.survey);
                }
            },
            error: function(data) {
                $("#errors").val('error');
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
                iss.code = code;
                if (data.error != '') {
                    $("#errors").val(data.error);
                    $("#modal_validation_error").modal();
                }
                else {
                    $("#errors").val('');
                    $(".panel-body #image").empty();
                    iss.js = data.survey;
                    eval(data.survey);
                    saveSurvey();
                }
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
            $("#view").trigger("click");
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



    

