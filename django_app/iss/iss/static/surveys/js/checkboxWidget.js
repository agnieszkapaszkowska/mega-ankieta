iss.lib.widgets.CheckboxWidget = function(options) {
    return iss.lib.widgets.Widget("checkbox", options);
}

$.widget("iss.checkboxWidget", $.iss.widget, {
    options: {
        name: '',
        data: function() { return [] },
        horizontal: function() {return false },
        required: function() {return false },
        resultVarName: null
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
                checked.push($(this).parent().index()); 
            });
            return checked;
        }
        iss.vars[varName] = getChecked();
        var name = this.options.name();
        $('input[name=' + name + ']').click(
            function() {
                iss.vars[varName] = getChecked();
            });
    },
    
    validate: function() {
        if (this.options.required()
            && this.element.find("input:checked").length == 0) {
            this.element.addClass('erorr');
            return false;
        }
        return true;
    },
    
});

