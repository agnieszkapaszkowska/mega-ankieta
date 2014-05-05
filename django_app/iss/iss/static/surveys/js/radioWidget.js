$.widget("iss.radioWidget", $.iss.widget, {
    options: {
        questionWidget: null,
        condition: null,
        name: function() { return '' },
        data: function() { return [] },
        checkedIndex: function() { return -1 },
        horizontal: function() {return false },
        required: function() {return true },
        resultVarName: null,
        tupleArgs: {
            id: function() { return "" }, 
            text: function() { return "" }
        }
    },

    _create: function() {
        this._super();
    },

    _setOption: function(key, value) {
        if (key == "data")
            this._setData(value);
        if (key == "resultVarName" && value != null)
            this._setCallback(value);
        this._super(key, value);
    },

    _setData: function(dataFun) {
        this.element.find("label").remove();
        var data = dataFun();
        for (var i = 0; i < data.length; i++) {
            var radio = data[i]();
            this.updateTupleArgs(radio, this.options.tupleArgs);
            $('<label ' + (this.options.horizontal() ? 
                    '' : 'style="display:block;"') + '>'
                + '<input type="radio" name="'
                + this.options.name() + '" id="'
                + radio['id']() + '" '
                + (i == this.options.checkedIndex() ? 'checked' : '')
                + '>' + radio['text']() + '</label>')
                .appendTo(this.element);
        }
    },

    _setCallback: function(varName) {
        iss.vars[varName] = this.options.checkedIndex();
        var element = this.element;
        var questionWidget = this.options.questionWidget;
        element.find('input').click(
            function() {
                iss.vars[varName] = element.find('input')
                            .index(element.find('input:checked'));
                questionWidget.childChanged();
            });
    },
    
    validate: function() {
        if (this.options.required()
            && this.element.is(":visible")
            && this.element.find('input:checked').length == 0) {
            this.element.addClass('erorr');
            return false;
        }
        return true;
    },

    insertSubmitData: function(submitData) {
        if (this.containsSubmitData) {
            submitData[this.options.name()] = this.element
                .find("input:checked").attr("id");
        }
    }
    
});

