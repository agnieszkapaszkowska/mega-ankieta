$.widget("iss.checkboxWidget", $.iss.widget, {
    options: {
        questionWidget: null,
        condition: null,
        name: function() { return "" }, 
        data: function() { return [] },
        horizontal: function() {return false },
        required: function() {return false },
        resultVarName: null,
        tupleArgs: {
            id: function() { return "" }, 
            text: function() { return "" }, 
            checked: function() { return false }
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
            var checkbox = data[i]();
            this.updateTupleArgs(checkbox, this.options.tupleArgs);
            $('<label ' + (this.options.horizontal() ? 
                    '' : 'style="display:block;"') + '>'
                + '<input type="checkbox" name="'
                + this.options.name() + '" id="'
                + checkbox['id']() + '" '
                + (checkbox['checked']() ? 'checked' : '')
                + '>' + checkbox['text']() + '</label>')
                .appendTo(this.element);
        }
    },

    _setCallback: function(varName) {
        var element = this.element;
        function getChecked() {
            var checked = [];
            element.find("input:checked").each(function () { 
                checked.push($(this).attr("id")); 
            });
            return checked;
        }
        iss.vars[varName] = getChecked();
        var name = this.options.name();
        var questionWidget = this.options.questionWidget;
        $('input[name=' + name + ']').click(
            function() {
                iss.vars[varName] = getChecked();
                questionWidget.childChanged();
            });
    },
    
    validate: function() {
        if (this.options.required()
            && this.containsSubmitData
            && this.element.find("input:checked").length == 0) {
            this.element.addClass('erorr');
            return false;
        }
        return true;
    },

    insertSubmitData: function(submitData) {
        if(this.containsSubmitData) {
            var checked = [];
            this.element.find("input:checked").each(function () {
                checked.push($(this).attr("id"));
            });
            submitData[this.options.name()] = checked;
        }
    }
    
});

