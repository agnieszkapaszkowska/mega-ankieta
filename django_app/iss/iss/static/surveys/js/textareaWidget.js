$.widget("iss.textareaWidget", $.iss.widget, {
    options: {
        questionWidget: null,
        condition: null,
        name: function() { return '' },
        label: function() { return '' },
        placeholder: function() { return '' },
        required: function() { return true },
        resultVarName: null
    },

    _create: function() {
        this._super();
    },

    _setOption: function(key, value) {
        if (key == "label")
            this._setTextarea(value);
        if (key == "resultVarName" && value != null)
            this._setCallback(value);
        this._super(key, value);
    },

    _setTextarea: function(dataFun) {
        $('<label>' + this.options.label() + '</label><br/>')
            .appendTo(this.element);
        $('<textarea name="' + this.options.name()
            + '" placeholder="' + this.options.placeholder()
            + '"></textarea>').appendTo(this.element);
    },

    _setCallback: function(varName) {
        var element = this.element;
        var questionWidget = this.options.questionWidget;
        iss.vars[varName] = element.find('textarea').val();
        element.find('textarea').change(
            function() {
                iss.vars[varName] = element.find('textarea').val();
                questionWidget.childChanged();
            });
    },

    validate: function() {
        if (this.options.required()
            && this.element.is(":visible")
            && this.element.find('textarea').val().length == 0) {
            this.element.addClass("error");
            return false;
        }
        return true;
    },

    insertSubmitData: function(submitData) {
        if(this.containsSubmitData) {
            submitData[this.options.name()] = this.element
                .find("textarea").val();
        }
    }
});
