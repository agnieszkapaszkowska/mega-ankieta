$.widget("iss.textinputWidget", $.iss.widget, {
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
            this._setTextinput(value);
        if (key == "resultVarName" && value != null)
            this._setCallback(value);
        this._super(key, value);
    },

    _setTextinput: function(dataFun) {
        $('<label>' + this.options.label() + '</label>')
            .appendTo(this.element);
        $('<input type="text" name="' + this.options.name()
            + '" placeholder="' + this.options.placeholder()
            + '"></input>').appendTo(this.element);
    },

    _setCallback: function(varName) {
        var element = this.element;
        var questionWidget = this.options.questionWidget;
        iss.vars[varName] = element.find('input').val();
        element.find('input').change(
            function() {
                iss.vars[varName] = element.find('input').val();
                questionWidget.childChanged();
            });
    },

    validate: function() {
        if (this.options.required()
            && this.element.is(":visible")
            && this.element.find('input').val().length == 0) {
            this.element.addClass("error");
            return false;
        }
        return true;
    }
});
